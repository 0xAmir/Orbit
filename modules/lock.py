import os

if "nt" in os.name:
    os.system("rundll32.exe user32.dll,LockWorkStation")
else:
    os.system("gnome-session-quit --logout --force") #if you're running KDE then replace that command with the KDE's