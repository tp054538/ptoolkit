import os
import subprocess
from module import tor

def slowloris_self_check():
    slowloris_checkstatus = subprocess.run("ls | grep slowloris", shell=True, stdout=subprocess.PIPE)
    slowloris_checkstatusd = slowloris_checkstatus.stdout.decode('ascii')
    if "slowloris" in slowloris_checkstatusd or "Slowloris" in slowloris_checkstatusd:
        return 1
    else:
        return 0

def slowloris_banner():
    if slowloris_target == "":
        slowloris_target_banner = "Without protocol (eg. aaa.com )"
    else:
        slowloris_target_banner = "\033[1;32m" + slowloris_target.strip() + "\033[00m"
    
    if slowloris_port_command == "":
        slowloris_port_banner = "Default = 80"
    else:
        slowloris_port_banner = "\033[1;32m" + slowloris_port_command.replace("-p","").strip() + "\033[00m"

    os.system("clear")
    print("""
                        Password Cracker (JohnTheRipper)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target            :   """+slowloris_target_banner+"""
    2. Port              :   """+slowloris_port_banner+"""
    3. Sockets           :   Use how many sockets in test
    4. HTTPS Mode        -   Use HTTPS for requests
    5. Proxy             -   Use Tor proxy to increase anonymity
    6. Verbose           -   Increase logging
    7. Random User Agent -   Use random user agent for each request

Command: \033[1;32m"""+slowloris_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
""")

def slowloris_main():
    global slowloris_final_command, slowloris_target, slowloris_port_command
    slowloris_target = ""
    slowloris_port_command = ""

    slowloris_select = ""
    while slowloris_select != "99":
        slowloris_final_command = "python3 ./slowloris/slowloris.py " + slowloris_port_command + slowloris_target
        slowloris_banner()
        slowloris_select = input("\nSelect: ").strip()
        #target
        if slowloris_select == "1":
            slowloris_target = input("\nTarget: ").strip()
            if slowloris_target == "" or " " in slowloris_target:
                slowloris_target = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if slowloris_target.startswith("http://") == True or slowloris_target.startswith("https://") == True:
                slowloris_target = slowloris_target.strip("http://").strip("https://")
                print("\n[*] Do not specify protocol infront of URL! http/https is auto removed.")
                useless = input("Enter any key to continue......")
            slowloris_target += " "
        #port
        elif slowloris_select == "2":
            try:
                slowloris_port = int(input("\nPort: ").strip())
                if slowloris_port < 1 or slowloris_port > 65535:
                    raise ValueError
            except ValueError:
                slowloris_port_command = ""
                print("\nError Port! Port 1 ~ 65535 only.")
                useless = input("Enter any key to continue......")
                continue
            slowloris_port_command = "-p " + str(slowloris_port) + " "



def main():
    print("\033[1;32m[+] Loading Slowloris Module\033[00m")
    if slowloris_self_check() == 1:
        slowloris_main()
    else:
        print("\n\033[1;31m[-] Slowloris is not installed!\033[00m")
        useless = input("Enter any key to continue......")