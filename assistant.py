import webbrowser
import datetime
import subprocess
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth


# Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="7ad20770da5243ce9c681c795d7d0893",
    client_secret="b847726d433d431da6f29c0403d5000f",
    redirect_uri="http://localhost:8888/callback",
    scope="user-read-playback-state user-modify-playback-state user-read-currently-playing"
))

# Get live weather using wttr.in
def get_weather_wttr(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Sorry, I couldn't fetch the weather right now."
    except Exception:
        return "Sorry, there was a problem getting the weather."

# Main personal assistant function
def personal_assistant(user_input):
    user_input = user_input.lower()

    # Google Maps directions
    if "get directions from" in user_input and "to" in user_input:
        try:
            parts = user_input.split("get directions from")[1].strip().split("to")
            origin = parts[0].strip().replace(" ", "+")
            destination = parts[1].strip().replace(" ", "+")
            url = f"https://www.google.com/maps/dir/{origin}/{destination}"
            webbrowser.open(url)
            return f"Getting directions from {origin.replace('+', ' ')} to {destination.replace('+', ' ')}."
        except Exception:
            return "Sorry, I couldn't get the directions. Please try again."

    # Weather
    if "weather in" in user_input:
        city = user_input.split("weather in")[-1].strip()
        return get_weather_wttr(city)

    if "what's the weather in" in user_input:
        city = user_input.split("what's the weather in")[-1].strip()
        return get_weather_wttr(city)

    # Translation
    if "translate" in user_input and "into" in user_input:
        try:
            translator = Translator()
            parts = user_input.split("translate")[1].strip().split("into")
            phrase = parts[0].strip()
            target_language = parts[1].strip()
            translated = translator.translate(phrase, dest=target_language.lower())
            return f"The translation is: {translated.text}"
        except Exception:
            return "Sorry, I couldn't translate that."

    # Open YouTube
    if "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    # Google search
    if "search google for" in user_input:
        query = user_input.split("search google for")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}."

    # Time and Date
    if "what time is it" in user_input or "tell me the time" in user_input:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {time_now}."

    if "what date is it" in user_input or "what's the date" in user_input:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."

    # Open Notepad (Windows)
    if "open notepad" in user_input:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."

    # Spotify controls
    if "play spotify" in user_input:
        sp.start_playback()
        return "Playing music on Spotify."

    if "pause spotify" in user_input:
        sp.pause_playback()
        return "Pausing Spotify."

    if "next song" in user_input:
        sp.next_track()
        return "Skipping to the next song."

    if "previous song" in user_input:
        sp.previous_track()
        return "Going to the previous song."

    if "play" in user_input and "on spotify" in user_input:
        query = user_input.split("play")[1].split("on spotify")[0].strip()
        results = sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            uri = results['tracks']['items'][0]['uri']
            sp.start_playback(uris=[uri])
            return f"Playing {query} on Spotify."
        else:
            return "I couldn't find that on Spotify."

    return None  # No matching personal command