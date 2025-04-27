# AI Personal Voice Assistant

## Project Overview
This project is a personal AI voice assistant that can interact with users through both text and voice input via a web interface. It uses OpenAI GPT-4 for natural conversation and supports a wide range of voice commands such as opening websites, controlling Spotify music, checking the weather, translating text, taking and reading notes, and providing directions using Google Maps.

Originally, the project was intended to run fully on a Raspberry Pi 5. However, due to significant technical difficulties with audio drivers and API reliability on the Pi, the project was moved to a Windows PC where development was completed successfully.

---

## Features
- Natural language conversation using GPT-4
- Voice and text input via web browser
- Text-to-speech responses
- Open websites (e.g., YouTube, Google)
- Smart search inside YouTube, Amazon, Google, Wikipedia
- Spotify music control (play, pause, next track, play specific artist)
- Real-time weather lookup (using wttr.in)
- Live text translation between languages (using Google Translate API)
- Take notes and read notes aloud
- Google Maps driving directions between locations
- Light/Dark mode toggle for the web UI

---

## Technologies Used
- **Python 3.11** – Backend development
- **Flask** – Web framework
- **HTML, CSS, Bootstrap 5** – Frontend
- **OpenAI GPT-4 API** – Conversation engine
- **SpeechRecognition API** – Voice input
- **Web Speech API (JavaScript)** – Browser microphone input
- **pyttsx3** – Text-to-speech (TTS)
- **Spotipy** – Spotify Web API access
- **Requests** – Fetch weather and maps data
- **Googletrans** – Language translation
- **wttr.in** – Free weather service

---

## System Architecture
- **Frontend**: HTML/CSS/Bootstrap interface, mic input, Light/Dark mode
- **Backend**: Flask routes, command recognition, API calls
- **Assistant Logic**: Handles specific commands like opening apps, searching websites, music control, weather, directions
- **External APIs**: OpenAI, Spotify, wttr.in, Googletrans

---

## Installation and Setup
1. Install Python 3.11 from [python.org](https://www.python.org/).
   
2. Clone the repository:
   ```
   git clone https://github.com/Jamween/voice-assistant.git
   ```
3. Navigate to the project folder
   
4. Install the required Python libraries:
  ```
  pip install flask openai pyttsx3 spotipy googletrans==4.0.0-rc1 requests
  ```
5. Run the application:
```
  python app.py
  ```
6. Open your web browser and go to:
  ```
  http://127.0.0.1:5000
  ```


