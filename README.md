# 🧠 Jarvis - Voice Controlled Assistant with OpenAI

**Jarvis** is a Python-based personal voice assistant that listens to your voice commands, performs web-based actions, plays music, fetches news, and provides AI-powered answers using the **OpenAI GPT-4.1 model**.

---

## 📋 Features

- 🎙️ Wake-word activation: responds to **"Jarvis"**
- 🎵 Play specific songs via YouTube
- 🌐 Open websites like Google, YouTube, LinkedIn
- 🗞️ Fetch top headlines using NewsAPI
- 🤖 AI-powered conversational responses using **OpenAI**
- 🗣️ Text-to-speech responses using **gTTS** and playback with **Pygame**

---

## 🛠 Requirements

- Python 3.x
- `SpeechRecognition`: `pip install SpeechRecognition`
- `gTTS`: `pip install gTTS`
- `pyttsx3`: `pip install pyttsx3`
- `pygame`: `pip install pygame`
- `requests`: `pip install requests`
- `openai`: `pip install openai`

---

## 📁 Folder Structure

```
jarvis-voice-assistant/
├── main.py            # Main assistant logic and voice interaction
├── client.py          # Test script for OpenAI integration
├── musicLibrary.py    # Music title to YouTube URL mapping
└── README.md          # Project overview and usage guide
```

---

## 🚀 How to Use

### 1. Install Dependencies

Run the following command:

```bash
pip install SpeechRecognition gTTS pyttsx3 pygame requests openai
```

### 2. Replace API Keys

Update the following in `main.py` and `client.py`:

- **Google OpenAI API key**:
  ```python
  api_key="YOUR_OpenAI_API_KEY"
  ```

- **NewsAPI key**:
  ```python
  newsapi = "YOUR_NEWS_API_KEY"
  ```

### 3. Run the Assistant

```bash
python main.py
```

- Say **"Jarvis"** to wake the assistant.
- Then issue a command like:
  - `"open google"`
  - `"play skyfall"`
  - `"news"`
  - `"what is quantum computing?"`

---

## 🔍 Example Commands

- "Jarvis" → (wake word)
- "Open YouTube"
- "Play Shape of You"
- "News"
- "What is machine learning?"

---

## 🧠 How It Works

- **Speech Recognition** detects voice commands and wake word
- **Webbrowser** module handles online navigation
- **Predefined music links** for direct playback via YouTube
- **NewsAPI** fetches latest news headlines (US by default)
- **OpenAI GPT-4.1** handles general questions or conversations
- **gTTS + Pygame** convert responses into spoken audio

---

## 💬 AI Integration (OpenAI)

- Uses `openai/chat.completions.create()` to interact with GPT-4.1
- Communicates through the [OpenAI-compatible endpoint](https://models.github.ai/inference)
- Responses are dynamic and context-aware

---

## 🎵 Sample Music Library

```python
music = {
    "no pressure": "https://www.youtube.com/watch?v=-ga08znuiLE",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI"
}
```

---

## ✨ Tips

- Use a clear microphone for better wake-word detection
- Add more custom voice commands inside `processCommand()` in `main.py`
- Modify the assistant's personality or instructions via the `system` message in `aiProcess()`

---

Enjoy building your own intelligent assistant with OpenAI! 🎙️🤖
