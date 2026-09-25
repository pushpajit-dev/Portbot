<div align="center">

  <h1>Portbot</h1>

  <p><strong>Run unrestricted AI models entirely on your device.<br/>No cloud. No filters. No limits.</strong></p>

  <p>
    <strong>Developer:</strong> NoishiXzen &nbsp;|&nbsp;
    <strong>Contact:</strong> <a href="mailto:noishixzen@gmail.com">noishixzen@gmail.com</a> &nbsp;|&nbsp;
    <strong>More Apps:</strong> <a href="https://aivorygen.netlify.app">aivorygen.netlify.app</a>
  </p>

  [Overview](#overview) · [Features](#features) · [Quick Start](#quick-start) · [Local API](#local-api-server) · [More Apps](#more-apps) · [License](#license)

</div>

---

## Overview

**Portbot** is a powerful multiplatform application that runs open-source AI models directly on your device — **Android, iOS, Windows, macOS, and Linux** — with zero censorship, zero cloud dependency, and total privacy.

- **No API keys required**
- **No subscriptions or fees**
- **No content filters or guardrails**
- **100% offline & private:** Your conversations and prompts never leave your local device.

---

## Features

| Feature | Description |
|---------|-------------|
| **Zero Censorship** | Runs abliterated and uncensored models with no refusals or corporate safety filters |
| **Total Privacy** | All conversations stay strictly on-device. Nothing is sent to external servers |
| **Fully Offline** | Works anywhere without internet connection once models are downloaded |
| **Cross-Platform** | Seamless support for Android, iOS, Windows, macOS, and Linux |
| **Local OpenAI API** | Built-in HTTP server compatible with standard OpenAI SDKs and tools |
| **Model Library** | In-app catalog and custom GGUF model import via file or URL |
| **Chat History** | Fast local conversation management powered by Hive |
| **Hardware Acceleration** | Configurable CPU, Vulkan, and OpenCL acceleration layers |

---

## Quick Start

### Build and Run from Source

**Prerequisites:** [Flutter SDK](https://flutter.dev/docs/get-started/install) (3.11.4+)

```bash
# Clone the repository
git clone https://github.com/NoishiXzen/Portbot.git
cd Portbot

# Install dependencies
flutter pub get

# Run on your target platform
flutter run -d windows    # Windows
flutter run -d android    # Android device / emulator
flutter run -d macos      # macOS
flutter run -d linux      # Linux
flutter run -d chrome     # Web
```

### Building Release Artifacts

- **Android APK:**
  ```bash
  flutter build apk --release --target-platform android-arm64
  ```
- **Windows Executable:**
  ```bash
  flutter build windows --release
  ```
- **iOS IPA:**
  ```bash
  flutter build ipa --release
  ```

---

## Recommended Models

| Model | Size | Best For | Type |
|-------|------|----------|------|
| **Gemma 2 2B** | ~1.6 GB | Fast responses, low RAM devices | Uncensored |
| **Gemma 4 E4B Heretic** | ~5.3 GB | High-quality deep responses | Uncensored |
| **Dolphin 2.9 Llama 3 8B** | ~4.9 GB | Creative and general reasoning | Uncensored |
| **Phi-3.5 Mini 3.8B** | ~2.2 GB | Lightweight & analytical | Standard |

Models can be downloaded directly inside Portbot under the **Models** tab.

---

## Local API Server

Portbot includes a built-in **OpenAI-compatible REST API** so you can connect third-party clients, coding extensions, or custom scripts directly to your local models.

### Setup

1. Load a model in Portbot.
2. Navigate to **Settings → Local API Server** and turn it **ON**.
3. Point your client to `http://127.0.0.1:4891/v1`.

### Example Endpoints

```bash
# List loaded models
curl http://127.0.0.1:4891/v1/models

# Non-streaming chat completion
curl http://127.0.0.1:4891/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Explain quantum computing simply."}]}'

# Streaming chat completion
curl -N http://127.0.0.1:4891/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","stream":true,"messages":[{"role":"user","content":"Write a python script to scan open ports."}]}'
```

---

## More Apps & Contact

- **Developer:** NoishiXzen
- **Email:** [noishixzen@gmail.com](mailto:noishixzen@gmail.com)
- **Website & More Apps:** [https://aivorygen.netlify.app](https://aivorygen.netlify.app)

---

## License

Licensed under the **MIT License**.
