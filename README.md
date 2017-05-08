# Orbit
_Control your computer via SMS_  
  
Orbit is a Python script enabling you to send commands to your computer when you don't have an internet connection or when your machine is physically out of reach.  
  
# Usage  
Orbit can be ran as a normal script or as a daemon in the background listening for incoming commands from your sms's.  
it consists of a listener that sits on the desired machine, which will then execute a module from the modules directory, you can add your own modules there which will be executed by orbit once it receives its name in a text message (SMS).  
Orbit receives commands in the following syntax:  
`Password module_name`
The password can be specified in the wizard that runs the first time you use orbit and it can be changed later from the config file `orbit_config.ini`, along with the authorized phone number to take commands from.  

# Examples  

After configuring and running orbit on your machine, you can send it commands according to the aformentioned syntax as follows:  
`P@ssw0rd lock`  
This would cause orbit to verify the password in the SMS and execute the module *lock.py* which locks up the screen and asks for a password (if any already exists on the system).  
  
# WARNING
Some functions of orbit require root access/administrative rights, please mind your permissions especially if you were to set a setuid/setgid to avoid opening a privilege escalation vulnerability on your system.   
(`sudo chmod a-rw` recommended)
