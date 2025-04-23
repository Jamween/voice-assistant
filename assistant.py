import webbrowser
import datetime
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="7ad20770da5243ce9c681c795d7d0893",
    client_secret="b847726d433d431da6f29c0403d5000f",
    redirect_uri="http://localhost:8888/callback",
    scope="user-read-playback-state user-modify-playback-state user-read-currently-playing"
))

def personal_assistant(user_input):
    """
    Handles custom voice/text commands before falling back to OpenAI GPT.
    Includes system commands, web actions, and Spotify control.
    """
    user_input = user_input.lower()

    # Open YouTube
    if "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    # Search Google
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

    # Open Notepad (Windows only)
    if "open notepad" in user_input:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."

    # Spotify playback controls
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

    # Search and play specific song on Spotify
    if "play" in user_input and "on spotify" in user_input:
        query = user_input.split("play")[1].split("on spotify")[0].strip()
        results = sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            uri = results['tracks']['items'][0]['uri']
            sp.start_playback(uris=[uri])
            return f"Playing {query} on Spotify."
        else:
            return "I couldn't find that on Spotify."

    # No matching command found
    return None
