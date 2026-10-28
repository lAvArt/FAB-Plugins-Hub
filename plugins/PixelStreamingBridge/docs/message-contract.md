# Message Contract v1.0

This document defines the JSON contract for communication between the Web Client and the Unreal Engine Plugin. The envelope below has not changed in PSB 1.1.0.

## Principles
1.  **Versioned envelope**: Every message carries `"version": "1.0"`. Unreal checks it on inbound commands. With the project setting **Accept Raw Messages** on (the default), Unreal also accepts JSON without an envelope and wraps it into a command (see "Raw messages" below); turn the setting off to accept envelopes only.
2.  **String-based Routing**: the `name` field determines the handler.
3.  **Payloads are opaque by default**: PSB validates the envelope, not the payload. Payload checking is opt-in: load a message manifest and enable **Validate Against Manifest** (see section 4).
4.  **No Provider IO**: Provider-specifics (e.g. Eagle3D vs Arcware) are handled in the Web layer, not here.

## Namespacing
Naming conventions (PSB does not enforce them at runtime; the manifest tools check them):
- `psb.*`: **Reserved** for the Bridge's own messages (`psb.ping`, `psb.pong`, `psb.error`). The reference web templates also send domain commands under `psb.*` (for example `psb.camera.set_view`); those names are kept as they are because shipped builds parse them.
- `app.*`: **Recommended** for user application logic (e.g., `app.change_color`).
- Never rename a wire name a client already sends.


## 1. Command (Web -> Unreal)

Commands are requests sent from the Web Client to Unreal. Inbound envelopes must be of type `command`. With **Accept Raw Messages** off, any other type is answered with `INVALID_TYPE`; with it on (the default), a message that fails the envelope check is coerced into a command as described under "Raw messages".

### Schema
```json
{
  "version": "1.0",
  "type": "command",
  "name": "<command_name>",
  "payload": {
    // Arbitrary JSON object expected by the command handler
  },
  "requestId": "<optional correlation id>"
}
```

`requestId` is optional. The reference web client (`@psb-ui/psb-client`) adds one to every command. Unreal does not need it to route a command; since 1.1.0 it echoes it on replies (see section 3) and on `psb.error`.

### Example: Invocation
```json
{
  "version": "1.0",
  "type": "command",
  "name": "change_color",
  "payload": {
    "hex": "#FF0000",
    "target": "cube_01"
  }
}
```

### Raw messages
With **Accept Raw Messages** on (default), a message that is not a valid envelope is turned into a command instead of being rejected:
- an object with a `name` field: that name, with its `payload` (or the rest of the object);
- an object with a `command` field: that name, with the rest of the object as payload;
- an object with a single key: the key is the name, its value the payload;
- anything else: the command `psb.raw` with the whole object as payload.

---

## 2. Event (Unreal -> Web)

Events are asynchronous messages emitted from Unreal to the Web Client.

### Schema
```json
{
  "version": "1.0",
  "type": "event",
  "name": "<event_name>",
  "payload": {
    // Arbitrary JSON object
  }
}
```

### Example: State Change
```json
{
  "version": "1.0",
  "type": "event",
  "name": "color_changed",
  "payload": {
    "success": true,
    "new_color": "#FF0000"
  }
}
```

## 3. Replies (since 1.1.0)

A reply is an ordinary event that also carries the command's `requestId`, so the web client can match it to its request:

```json
{
  "version": "1.0",
  "type": "event",
  "name": "app.color_changed",
  "payload": { "ok": true },
  "requestId": "<the command's requestId>"
}
```

In Blueprint, a command handler receives the payload as `FPSBStructuredPayload`, which carries `CommandName` and `RequestId`; **Reply To Command Json** (on the PSB subsystem) emits the reply. With an empty event name it uses the command's `response` from the loaded manifest. The reference web client passes `requestId` to its event listeners.

## 4. Message manifest (optional, since 1.1.0)

The manifest is one list of every command and event a project uses: the wire name, the direction (`command` = web -> Unreal, `event` = Unreal -> web), a description, typed payload fields and, for a command, the event that answers it. It exists as an asset (`PSB Message Manifest`, a Data Asset) and as plain JSON (`*.psb.json`):

```json
{
  "version": "1.0",
  "messages": [
    {
      "name": "app.set_color",
      "direction": "command",
      "description": "Paint the car.",
      "fields": [
        { "name": "color", "type": "string", "required": true, "enum": ["red", "blue"] },
        { "name": "intensity", "type": "number", "required": false, "min": 0, "max": 1 }
      ],
      "response": "app.color_changed"
    }
  ]
}
```

Field types: `string`, `number`, `integer`, `boolean`, `string[]`, `number[]`, `object`. `enum` applies to strings; `min` / `max` to numbers, integers and each item of a `number[]`.

The manifest does not change the envelope. It is used to:
- **validate inbound payloads** when **Validate Against Manifest** is on (project setting, off by default). Only commands the manifest lists are checked; fields it does not list are allowed. An invalid command is not dispatched and is answered with `psb.error` (section 6);
- **reply** without repeating the event name (section 3);
- **generate** JSON Schemas, TypeScript typings, a commands reference, a DataTable and Blueprint handlers (editor tools, see `AI_ASSISTANT_GUIDE.md`).

Load it with the project setting **Default Manifest** (or **Manifest Json File**), the `Manifest` property of a PSBBootstrap, or **Load Manifest** on the subsystem.

## 5. Receiving commands in Unreal

PSB dispatches each valid command, in this order, to:
1. a C++ handler registered with `RegisterCommand` (one per name);
2. Blueprint handlers bound to that one name with **Bind Command** (subsystem) or **Bind PSB Command** (function library), since 1.1.0. Any number may listen; each receives `(CommandName, Payload)`, and typed getters (`Get String Field`, `Get Number Field`, `Get Integer Field`, `Get Bool Field`, `Get String Array`, `Get Number Array`, `Get Object Json`, `Has Field`) read the payload;
3. every listener of **On Command Received** and **On Command Received Structured** (all names).

`psb.ping` is answered by the Bridge itself with `psb.pong` and reaches none of them. A command nobody handles is answered with `psb.error` `COMMAND_NOT_FOUND`.

## 6. Error Handling

When PSB rejects a command (an invalid envelope while Accept Raw Messages is off, a payload that fails manifest validation, or a command nobody handles), it logs the reason in the Unreal Output Log (`LogPSB`) and emits an error event back to the web client. Input that is not JSON at all is only logged.

### Error Event Schema
```json
{
  "version": "1.0",
  "type": "event",
  "name": "psb.error",
  "payload": {
    "code": "INVALID_VERSION",
    "message": "Invalid or missing version. Expected '1.0'."
  }
}
```

> **Wire name discrepancy.** The Unreal plugin emits the event name **`psb.error`** (with a dot). Earlier versions of this document and the `@psb-ui/events` constant `PSB_EVENTS.ERROR` say `psb_error` (with an underscore), which Unreal has never sent. The emitted name is not changed, because shipped builds and pages may depend on it. Web clients should listen to `psb.error` (and may also listen to `psb_error` for safety).

Codes:
- envelope: `INVALID_JSON`, `INVALID_VERSION`, `INVALID_TYPE`, `MISSING_NAME`, `COMMAND_NOT_FOUND`;
- manifest validation (since 1.1.0): `MISSING_FIELD`, `INVALID_FIELD_TYPE`, `INVALID_FIELD_VALUE`, `FIELD_OUT_OF_RANGE`, `INVALID_DIRECTION` (an event name sent as a command).

Since 1.1.0 the payload may also carry `field` (the payload field at fault) and `command` (the command at fault), and the envelope carries the command's `requestId` when it had one. Existing fields are unchanged.
