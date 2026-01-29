# Generic Web UI Template

This template provides a production-ready starting point for building custom Pixel Streaming interfaces using Next.js and React.

## Features
- **Full PSB Integration**: Pre-configured with `@psb-ui/provider`.
- **Responsive Design**: Built with Tailwind CSS.
- **Connection Handling**: Automatic connection management and status display.
- **Overlay System**: Example overlay for "Click to Start" and "Loading" states.

## UI Showcase

The Generic Template features an adaptive UI that scales from desktop down to mobile:

| Desktop | Tablet | Mobile |
|---------|--------|--------|
| ![Desktop](./resources/WebUI_Generic_DesktopSize.png) | ![Tablet](./resources/WebUI_Generic_TabletSize.png) | ![Mobile](./resources/WebUI_Generic_MobileSize.png) |


## Getting Started

### 1. Prerequisites
- Node.js 18+
- pnpm (recommended) or npm

### 2. Installation
Navigate to the template directory and install dependencies:
```bash
cd psb-ui/templates/generic
pnpm install
```

### 3. Running Locally
Start the development server:
```bash
pnpm dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

## Configuration

The main configuration is handled in `app/layout.tsx` or `app/page.tsx` via the `PSBProvider`.

```tsx
<PSBProvider
  playerUrl="http://localhost:80" // Your Signalling Server URL
  iframeStyle={{ border: 'none' }}
  debug={true} // Enable for console logs
>
  {children}
</PSBProvider>
```

## Key Components

### PSBProvider
The context provider that manages the WebSocket connection and the Pixel Streaming iframe. Wrap your application root with this.

### usePSB Hook
Access the bridge API from any component.

```tsx
import { usePSB } from '@psb-ui/provider';

export function MyComponent() {
  const { sendCommand, status } = usePSB();

  return (
    <button onClick={() => sendCommand('my_command', { foo: 'bar' })}>
      Send Command
    </button>
  );
}
```

### usePSBEvent Hook
Listen for specific events from Unreal Engine.

```tsx
import { usePSBEvent } from '@psb-ui/provider';

usePSBEvent('my_event', (payload) => {
  console.log('Received:', payload);
});
```
