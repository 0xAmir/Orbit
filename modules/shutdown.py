import os

if "nt" in os.name:
    os.system("shutdown -s -f -t 0")
else:
    os.system("shutdown") #need to be root for this one.