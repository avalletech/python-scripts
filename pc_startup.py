import subprocess
from pathlib import Path

# Resolve current user dynamically — no hardcoded usernames
user_home = Path.home()
username = user_home.name

apps = [
    str(user_home / "AppData" / "Local" / "Discord" / "Update.exe --processStart Discord.exe"),
    r"C:\Program Files\Voicemod V3\Voicemod.exe",
    r"C:\Program Files\Elgato\StreamDeck\StreamDeck.exe"
]

for app in apps:
    try:
        subprocess.Popen(app, shell=True)
        print(f"Launched: {app}")
    except Exception as e:
        print(f"Failed to launch {app}: {e}")
