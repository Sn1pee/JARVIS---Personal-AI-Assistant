# 🧠 Jarvis - Voice Controlled Assistant with Open AI

Jarvis is a Python-based personal voice assistant that listens to your voice commands, responds using Google Text-to-Speech, performs web-based actions, and leverages Open AI to answer questions.

## 📋 Features

* Wake-word activation: responds to "Jarvis"
* Play specific songs via YouTube
* Open websites like Google, YouTube, LinkedIn
* Fetch top news headlines using NewsAPI
* AI-powered answers using ChatGPT
* Converts responses to speech using gTTS

## 🛠 Requirements

* Python 3.x
* Speech Recognition: `pip install SpeechRecognition`
* gTTS: `pip install gTTS`
* pyttsx3: `pip install pyttsx3`
* pygame: `pip install pygame`
* requests: `pip install requests`
* OpenAI SDK: `pip install openai`

## 📁 Folder Structure

```
jarvis-voice-assistant/
├── main.py            # Main assistant logic and command handling
├── client.py          # OpenAI API test script
├── musicLibrary.py    # Song dictionary with YouTube links
└── README.md          # Project overview and instructions
```

## 🚀 How to Use

### 1. Install Required Libraries

Install the required Python packages:

```bash
pip install SpeechRecognition gTTS pyttsx3 pygame requests google-generativeai
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

* Speak "Jarvis" to activate the assistant.
* Give a command after the wake word (e.g., "open google", "play skyfall", "news", "what is coding?").

## 🔍 Example Commands

* "Jarvis" → (wake word)
* "Open Google"
* "Play Skyfall"
* "News"
* "What is the capital of Japan?"

## 📈 How It Works

* Listens for wake word using `speech_recognition`
* Handles actions:
  - Web actions via `webbrowser`
  - Music using predefined links
  - News using NewsAPI
  - Conversations via OpenAI
* Speaks response using `gTTS` and `pygame`

## 🧠 AI Integration (OpenAI)

* Uses ChatGPT's `client` to generate responses
* model = `openai/gpt4.1`
* Works for both factual and conversational queries

## 🎵 Music Library Sample

```python
music = {
    "skyfall" : "https://www.youtube.com/watch?v=DeumyOzKqgI",
    "perfect" : "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
}
```

## ✨ Tips

* Use a good mic for accurate wake-word detection
* Ensure stable internet for API calls
* Add more keywords and commands as needed

---

Enjoy your very own Jarvis! 🤖🎤
