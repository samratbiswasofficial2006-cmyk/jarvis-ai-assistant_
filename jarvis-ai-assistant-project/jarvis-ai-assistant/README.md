# JARVIS AI Assistant

A beginner-friendly Python personal assistant inspired by futuristic voice assistants. It supports text commands out of the box, with optional voice input and spoken responses.

## Features

- Text-based command interface
- Optional speech recognition and text-to-speech
- Open websites and search the web
- Open Google Maps directions/search
- Tell the current date and time
- Safe basic calculator (no `eval`)
- Optional OpenAI-powered chat mode
- Clear setup instructions and modular source code

> This is an independent learning project. It is not affiliated with Marvel, Iron Man, or any commercial JARVIS product.

## Requirements

- Python 3.10+
- Internet connection for web search, Maps, and optional AI chat
- Microphone and speakers for optional voice mode

## Setup (Windows)

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open Command Prompt in the project folder.
4. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Start JARVIS:

```bash
python main.py
```

## Optional voice mode

Run:

```bash
python main.py --voice
```

Voice features use `SpeechRecognition`, `PyAudio`, and `pyttsx3`. Microphone support can require extra system setup. If voice dependencies are unavailable, use the normal text mode.

## Optional AI chat

Set your API key as an environment variable; do not paste it into source code.

PowerShell:

```powershell
$env:OPENAI_API_KEY="your-api-key"
python main.py
```

Command Prompt:

```cmd
set OPENAI_API_KEY=your-api-key
python main.py
```

Then type `ai: your question`. AI chat requires the optional `openai` package and an API account with API access.

## Example commands

- `help`
- `time`
- `date`
- `open youtube`
- `search Python tutorials`
- `maps coffee shops in Kolkata`
- `calculate 25 * (8 + 2)`
- `ai: Explain cloud computing in simple words`
- `exit`

## Project structure

```text
jarvis-ai-assistant/
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
└── src/
    ├── __init__.py
    ├── assistant.py
    ├── commands.py
    └── voice.py
```

## Roadmap

- [ ] Add a desktop GUI
- [ ] Add configurable wake-word support
- [ ] Add calendar and task integrations
- [ ] Add a customizable dashboard
- [ ] Explore a wearable / smart-glasses interface

## Contributing

Issues and pull requests are welcome. Keep API keys and personal data out of commits.

## License

MIT. See [LICENSE](LICENSE).
