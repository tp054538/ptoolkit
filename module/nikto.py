import os
import subprocess
from module import tor

def nikto_self_check():
    nikto_statuscheck = subprocess.run("apt list 2>/dev/null | grep -E '^nikto/'", shell=True, stdout=subprocess.PIPE)
    nikto_statuscheckd = nikto_statuscheck.stdout.decode('ascii')
    if "installed" in nikto_statuscheckd or "upgradable" in nikto_statuscheckd:
        return 1
    else:
        return 0

def nikto_banner():
    if nikto_port_command != "":
        nikto_port_banner = "\033[1;32m" + nikto_port_command.strip().strip("-port").strip() + "\033[00m"
    else:
        nikto_port_banner = "Specify port to use (Unspecified -> port 80)"

    os.system("clear")
    print(type(nikto_port))
    print("""
                            Web Scanner (Nikto)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Host                 :   \033[1;32m"""+nikto_target+"""\033[00m

    2. Vhost                :   \033[1;32m"""+nikto_vhost+"""\033[00m
    3. Port                 :   """+nikto_port_banner+"""
    4. Proxy                -   Hide identity with Tor (Use of proxy will slow down the scanning)
    5. User Agent           :   Specify a User Agent (Not Specified -> use default)
    6. Ignore HTTP codes    :   Ignore HTTP codes as negative responses. (Use "," as seperator for multiple codes)

Mode:
    7. Database Check       -   Check syntax error on database and key files
    8. Evasion              -   Evade detection through encoding
    9. SSL                  -   Force using SSL
   10. No SSL               -   Disable SSL
   11. No DNS lookup        -   Disable DNS lookup
   12. verbose              -   Display more detailed information

Command: \033[1;32m"""+nikto_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
""")

def nikto_main():
    global nikto_final_command, nikto_target, nikto_vhost, nikto_port, nikto_port_command
    nikto_target_command = ""
    nikto_target = ""
    nikto_vhost_command = ""
    nikto_vhost = ""
    nikto_port_command = ""
    nikto_port = ""

    nikto_select = ""
    while nikto_select != "99":
        nikto_final_command = "nikto " + nikto_target_command + nikto_vhost_command + nikto_port_command
        nikto_banner()
        nikto_select = input("\nSelect: ")
        #target host ip
        if nikto_select == "1":
            nikto_target = input("\nHost: ").strip()
            if nikto_target == "":
                nikto_target_command = ""
                print("\n[*] Host cannot be empty!")
                useless = input("Enter any key to continue......")
                continue
            nikto_target_command = "-h " + nikto_target + " "
        #vhost
        elif nikto_select == "2":
            nikto_vhost = input("\nVirtual Host: ").strip()
            if nikto_vhost == "":
                nikto_vhost_command = ""
                print("\n[*] VHost is empty!")
                useless = input("Enter any key to continue......")
                continue
            nikto_vhost_command = "-vhost " + nikto_vhost + " "
        #port
        elif nikto_select == "3":
            nikto_port = input("\nPort: ").strip()
            if nikto_port == "":
                nikto_port_command = ""
                print("\n[*] Port is empty!")
                useless = input("Enter any key to continue......")
                continue
            try:
                nikto_port_int = int(nikto_port)
            except ValueError:
                nikto_port_command = ""
                print("\n[*] Numbers only!")
                useless = input("Enter any key to continue......")
                continue

            if nikto_port_int >= 1 and nikto_port_int <= 65535:
                nikto_port_command = "-port " + nikto_port + " "
            else:
                nikto_port_command = ""
                print("\n[*] Out of range! Port 1 - 65535 only!")
                useless = input("Enter any key to continue......")
                continue
        #use proxy
        elif nikto_select == "4":
            if tor.check_init() == 1:
                nikto_proxy_command = "-useproxy socks5://127.0.0.1:9050 "
            else:
                nikto_proxy_command = ""
                print("\n[*] Please activate Tor at main menu!")
                useless = input("Enter any key to continue......")
                continue

def main():
    print("\033[1;32m[+] Loading Nikto Module\033[00m")
    if nikto_self_check() == 1:
        nikto_main()
    else:
        print("\n\033[1;31m[-] Nikto is not installed!\033[00m")
        useless = input("Enter any key to continue......")
