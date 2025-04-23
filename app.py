from flask import Flask, render_template, request, jsonify
import openai
import pyttsx3  # For text-to-speech
import threading  # To avoid run loop issues
# Initialize Flask
app = Flask(__name__)
# OpenAI API Key
openai_api_key = "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"

# Speak in a background thread to avoid 'run loop already started' error
def speak(text):
    def speak_thread(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=speak_thread, args=(text,)).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    try:
        client = openai.OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {e}"

    speak(reply)  # Assistant speaks the reply
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
