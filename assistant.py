import webbrowser
import datetime
import subprocess

def personal_assistant(user_input):
    """
    Handles personal assistant voice/text commands like opening websites,
    apps, or giving system info.
    """
    user_input = user_input.lower()

    # Open websites
    if "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    if "search google for" in user_input:
        query = user_input.split("search google for")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}."

    # Time & date
    if "what time is it" in user_input or "tell me the time" in user_input:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {time_now}."

    if "what date is it" in user_input or "what's the date" in user_input:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."

    # Open local Windows apps
    if "open notepad" in user_input:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."

    return None  
