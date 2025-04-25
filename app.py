from flask import Flask, render_template, request, jsonify
import openai
import pyttsx3
import threading
import assistant  # Personal assistant commands

# Initialize Flask
app = Flask(__name__)

# OpenAI API Key
openai_api_key = "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" 

# Text-to-speech function
def speak(text):
    def speak_thread(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=speak_thread, args=(text,)).start()

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle incoming chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    # Check for personal assistant command
    personal_response = assistant.personal_assistant(user_input)
    if personal_response:
        speak(personal_response)
        return jsonify({'reply': personal_response})

    # Otherwise, call OpenAI GPT-4
    try:
        openai.api_key = openai_api_key  
        response = openai.ChatCompletion.create( 
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response['choices'][0]['message']['content']
    except Exception as e:
        reply = f"Error: {e}"

    speak(reply)
    return jsonify({'reply': reply})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
