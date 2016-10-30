#          Mandatory pretty ASCII art.
#  .oooooo.             .o8        o8o      .
# d8P'  `Y8b           "888        `"'    .o8
#888      888 oooo d8b  888oooo.  oooo  .o888oo
#888      888 `888""8P  d88' `88b `888    888
#888      888  888      888   888  888    888
#`88b    d88'  888      888   888  888    888 .
# `Y8bood8P'  d888b     `Y8bod8P' o888o   "888"
#                                         0xAmir
def main():
    import requests
    import subprocess
    import os
    import configparser
    from pyfiglet import Figlet
    import colorama
    from colorama import Fore
    from time import sleep, strftime
    colorama.init()

    try:
        if not os.path.isdir("data"):
            os.makedirs("data")
            intro = Figlet(font='slant')
            print Fore.GREEN + intro.renderText("Wizard")
            print "It appears that this is the first time you're running orbit. \nlet's start configuring."
            parser = configparser.SafeConfigParser()
            parser.add_section("Personal")
            parser.set('Personal', 'phone no', raw_input("Phone no: "))
            parser.set('Personal', 'passwd', raw_input("Password: "))
            parser.add_section("env")
            parser.set("env", "enable_logs", "True")
            parser.set("env", "log_name", "orbit_log.txt")
            parser.set("env", "interval", "10")
            with open("./data/orbit_config.ini", "w") as confwrt:
                parser.write(confwrt)
            print Fore.GREEN + "Config file added, Any future modifications should be made from the file itself."
    except(IOError, OSError):
        print("[!]FATAL: Could not create/open necessary files.")
        exit(-1)

    try:
        cfg_reader = configparser.SafeConfigParser()
        cfg_reader.read("./data/orbit_config.ini")
    except (IOError, OSError) as e:
        print("[!]FATAL: "+repr(e)+"\nCould not read config file")
        exit(-1)


    try:
        phone_no = cfg_reader.get("Personal", "phone no")
        password = cfg_reader.get("Personal", "passwd")
        retriever_post = {"draw":"3",
                        "columns[0][data]":"0",
                         "columns[0][name]":"",
                        "columns[0][searchable]":"true",
                        "columns[0][orderable]":"true",
                        "columns[0][search][value]":"",
                        "columns[0][search][regex]":"false",
                        "columns[1][data]":"1",
                        "columns[1][name]":"",
                        "columns[1][searchable]":"true",
                        "columns[1][orderable]":"true",
                        "columns[1][search][value]":"",
                        "columns[1][search][regex]":"false",
                        "columns[2][data]":"2",
                        "columns[2][name]":"",
                        "columns[2][searchable]":"true",
                        "columns[2][orderable]":"true",
                        "columns[2][search][value]":"",
                        "columns[2][search][regex]":"false",
                        "order[0][column]":"1",
                        "order[0][dir]":"desc",
                        "start":"0",
                        "length":"100",
                        "search[value]":"",
                        "search[regex]":"false"}
        retriever_post["search[value]"] = password
        sms_endpoint = "https://receive-a-sms.com/employee-grid-data.php"
        log_name = cfg_reader.get("env", "log_name")
        interval = cfg_reader.get("env", "interval")
        enable_logs = cfg_reader.get("env", "enable_logs")

    except configparser.Error as cfg_e:
        print("[!]FATAL: "+repr(cfg_e))
        exit(-1)


    while 1:
        try:
            res = requests.post(sms_endpoint, data=retriever_post)
            last_comm = open("./data/last_comm.txt", "a+")
            record = res.json()["data"][0]

            if record[1] in phone_no and record[2].split(" ")[0] == password and record[0] != last_comm.read():
                command = record[2].split(" ")[1]
                if "nt" in os.name:
                    subprocess.Popen("start /B "+os.getcwd()+"\\modules\\"+command+".py", creationflags=subprocess.CREATE_NEW_CONSOLE,shell=True)
                else:
                    subprocess.Popen("python "+os.getcwd()+"\/modules\/"+command+".py &", preexec_fn=os.setpgrp, shell=True)
                if enable_logs:
                    with open(log_name, "a") as logwrt:
                        logwrt.write("Command: " + command + " At: " + strftime("%d-%m-%Y ") + strftime("%H:%M:%S")+'\n')
                last_comm.truncate(0)
                last_comm.write(record[0])
                print Fore.GREEN + "[+]Executed!"
                continue
            else:
                raise Exception
        except (IOError, OSError) as file_e:
            print("[!]FATAL: " + repr(file_e))
            exit(-1)
        except Exception as e:
                print Fore.RED + "No (new) Commands/SMS's found, zZzZzZz... "
                sleep(int(interval))

    last_comm.close()
if __name__ == "__main__":
    main()