import os
from re import S
import subprocess
from module import tor

def joomscan_self_check():
    joomscan_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^joomscan/'", shell=True, stdout=subprocess.PIPE)
    joomscan_checkstatusd = joomscan_checkstatus.stdout.decode('ascii')
    if "installed" in joomscan_checkstatusd or "upgradable" in joomscan_checkstatusd:
        return 1
    else:
        return 0

def joom_banner():
    #display green colour when selected
    if joom_enumerate_flag == 1:
        joom_enumerate_color = "\033[1;32m"
    else:
        joom_enumerate_color = "\033[00m"

    if joom_rua_flag == 1:
        joom_rua_color = "\033[1;32m"
    else:
        joom_rua_color = "\033[00m"
    
    if joom_user_agent == "":
        joom_user_agent_banner = "Specify the user agent for scanning"
    else:
        joom_user_agent_banner = "\033[1;32m" + joom_user_agent + "\033[00m"

    os.system("clear")
    print("""
                          Joomla Scanner (JoomScan)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target               :   \033[1;32m"""+joom_target+"""\033[00m
    2. """+joom_enumerate_color+"""Enumerate\033[00m            -   Enumerate installed components
    3. Proxy                :   Format is protocol://ip:port
    4. Timeout              :   Set timeout for the scanning
    5. Cookie               :   Format is cookiename=cookievalue;

    5. Set User Agent       :   """+joom_user_agent_banner+"""
    6. """+joom_rua_color+"""Random User Agent\033[00m    -   Use random user agent for each scan

Command: \033[1;32m"""+joom_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
    """)

def joom_main():
    global joom_final_command, joom_target, joom_enumerate_flag, joom_rua_flag, joom_user_agent
    joom_select = ""
    joom_target = ""
    joom_enumerate_flag = 0
    joom_rua_flag = 0
    joom_user_agent = ""

    joom_base_command = "joomscan "
    joom_target_command = ""
    joom_final_command = ""
    joom_enumerate_command = ""
    joom_rua_command = ""
    joom_useragent_command = ""

    while joom_select != "99":
        joom_final_command = joom_base_command + joom_target_command + joom_enumerate_command + joom_useragent_command + joom_rua_command

        joom_banner()
        joom_select = input("Select: ")
        #set target
        if joom_select == "1":
            joom_target = input("\nTarget URL: ").strip()
            if joom_target == "":
                joom_target_command = ""
                print("\n[*] Target cannot be empty!")
                useless = input("Enter any key to continue......")
                continue
            joom_target_command = "-u " + joom_target + " "
        #enumerate
        elif joom_select == "2":
            if joom_enumerate_flag != 1:
                joom_enumerate_flag = 1
                joom_enumerate_command = "--ec "
            else:
                joom_enumerate_flag = 0
                joom_enumerate_command = ""
        #proxy
        elif joom_select == "3":
            if tor.check_init() == 1:
                pass
            else:
                print("\n[*]Tor is not running!")
                joom_custom_proxy_prompt = input("Do you want to use a custom proxy other than tor? (y/n): ")
                if joom_custom_proxy_prompt == "y" or joom_custom_proxy_prompt == "Y":
                    joom_custom_proxy = input("\nEnter the proxy (protocol://ip:port): ").strip()
                    #####
        #Specify User Agent
        elif joom_select == "5":
            joom_user_agent = input("User Agent: ").strip()
            if joom_user_agent == "":
                joom_useragent_command = ""
                print("\n[*] User Agent cannot be empty!")
                useless = input("Enter any key to continue......")
                continue
            joom_useragent_command = "-a \"" + joom_user_agent + "\" "
            joom_rua_flag = 0
            joom_rua_command = ""
        #Random User Agent
        elif joom_select == "6":
            if joom_rua_flag != 1:
                joom_rua_flag = 1
                joom_rua_command = "-r "
                joom_useragent_command = ""
                joom_user_agent = ""
            else:
                joom_rua_flag = 0
                joom_rua_command = ""

def main():
    print("\033[1;32m[+] Loading JoomScan Module\033[00m")
    if joomscan_self_check() == 1:
        joom_main()
    else:
        print("\n\033[1;31m[-] JoomScan is not installed!\033[00m")
        useless = input("Enter any key to continue......")