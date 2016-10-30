import os
import subprocess

if not os.path.isdir("./data"):
    print "[-]Please run Orbit.py first to configure for the first time.\n   Press Any Key To Exit."
    raw_input()
    exit(-1)
else:
    if "nt" in os.name:
        subprocess.Popen("start /B "+os.getcwd()+"\\orbit.py", creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
        print "[+]Orbit is now running in the background.\n   Press any key to close this window." #is it really?
        raw_input()
        exit(0)
    else:
        subprocess.Popen("nohup python " + os.getcwd() + "\/orbit.py &", shell=True)
        print "[+]Orbit is now running in the background.\n   Press any key to close this window."
        raw_input()
        exit(0)