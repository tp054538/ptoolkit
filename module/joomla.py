import os
import subprocess
from module import tor

def joomscan_self_check():
    joomscan_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^joomscan/'", shell=True, stdout=subprocess.PIPE)
    joomscan_checkstatusd = joomscan_checkstatus.stdout.decode('ascii')
    if "installed" in joomscan_checkstatusd or "upgradable" in joomscan_checkstatusd:
        return 1
    else:
        return 0

#check proxy format is xxx://xxx:port
def joom_proxy_validation(proxy):
    if "://" in proxy:
        proxy_list = proxy.split("://")
        if len(proxy_list) == 2:
            if ":" in proxy_list[1]:
                proxy_list2 = proxy_list[1].split(":")
                if len(proxy_list2) == 2:
                    try:
                        if int(proxy_list2[1]) >= 1 and int(proxy_list2[1]) <= 65535:
                            return 1
                        else:
                            return 0
                    except ValueError:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
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
    
    if joom_proxy_flag == 1:
        joom_proxy_banner = "\033[1;32m" + "SOCKS5://127.0.0.1:9050" + "\033[00m"
    elif joom_proxy_flag == 2:
        joom_proxy_banner = "\033[1;32m" + joom_custom_proxy + "\033[00m"
    else:
        joom_proxy_banner = "Format is protocol://ip:port"
    
    if joom_timeout_flag == 1:
        joom_timeout_banner = "\033[1;32m" + joom_timeout + "\033[00m"
    else:
        joom_timeout_banner = "Set timeout for the scanning"
    
    if joom_cookie_flag == 1:
        joom_cookie_banner = "\033[1;32m" + joom_cookie + "\033[00m"
    else:
        joom_cookie_banner = "Format is cookiename=cookievalue;"

    os.system("clear")
    print("""
                          Joomla Scanner (JoomScan)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target               :   \033[1;32m"""+joom_target+"""\033[00m
    2. """+joom_enumerate_color+"""Enumerate\033[00m            -   Enumerate installed components
    3. Proxy                :   """+joom_proxy_banner+"""
    4. Timeout              :   """+joom_timeout_banner+"""
    5. Cookie               :   """+joom_cookie_banner+"""

    6. Set User Agent       :   """+joom_user_agent_banner+"""
    7. """+joom_rua_color+"""Random User Agent\033[00m    -   Use random user agent for each scan

Command: \033[1;32m"""+joom_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
    """)

def joom_main():
    global joom_final_command, joom_target, joom_enumerate_flag, joom_rua_flag, joom_user_agent, joom_proxy_flag, joom_custom_proxy, joom_timeout_flag, joom_timeout, joom_cookie, joom_cookie_flag
    joom_select = ""
    joom_target = ""
    joom_enumerate_flag = 0
    joom_rua_flag = 0
    joom_proxy_flag = 0
    joom_timeout_flag = 0
    joom_cookie_flag = 0
    joom_user_agent = ""

    joom_base_command = "joomscan "
    joom_target_command = ""
    joom_final_command = ""
    joom_enumerate_command = ""
    joom_rua_command = ""
    joom_useragent_command = ""
    joom_proxy_command = ""
    joom_timeout_command = ""
    joom_cookie_command = ""

    while joom_select != "99":
        joom_final_command = joom_base_command + joom_target_command + joom_enumerate_command + joom_cookie_command + joom_proxy_command + joom_timeout_command + joom_useragent_command + joom_rua_command

        joom_banner()
        joom_select = input("Select: ")
        #set target
        if joom_select == "1":
            joom_target = input("\nTarget URL: ").strip()
            if joom_target == "" or " " in joom_target:
                joom_target_command = ""
                joom_target = ""
                print("\n[*] Target cannot be empty / contain spaces!")
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
                if joom_proxy_flag != 1:
                    joom_proxy_command = "--proxy SOCKS5://127.0.0.1:9050 "
                    joom_proxy_flag = 1
                else:
                    joom_proxy_flag = 0
                    joom_proxy_command = ""
            else:
                print("\n[*]Tor is not running!")
                joom_custom_proxy_prompt = input("Do you want to use a custom proxy other than tor? (y/n): ")
                if joom_custom_proxy_prompt == "y" or joom_custom_proxy_prompt == "Y":
                    joom_custom_proxy = input("\nEnter the proxy (protocol://ip:port): ").strip()
                    if joom_custom_proxy == "":
                        joom_proxy_command = ""
                        joom_proxy_flag = 0
                        print("\n[*] Target cannot be empty!")
                        useless = input("Enter any key to continue......")
                        continue
                    else:
                        if joom_proxy_validation(joom_custom_proxy) == 1:
                            joom_proxy_flag = 2
                            joom_proxy_command = "--proxy " + joom_custom_proxy + " "
                        else:
                            joom_proxy_command = ""
                            joom_proxy_flag = 0
                            print("\n[*] Invalid proxy format! Protocol://IP:port . Eg. SOCKS5://127.0.0.1:9050")
                            useless = input("Enter any key to continue......")
                            continue
                else:
                    joom_proxy_flag = 0
                    joom_proxy_command = ""
        #timeout
        elif joom_select == "4":
            joom_timeout = input("\nTimeout Seconds: ").strip()
            if joom_timeout == "":
                joom_timeout_command = ""
                joom_timeout_flag = 0
                print("\n[*] Timeout cannot be empty!")
                useless = input("Enter any key to continue......")
                continue
            try:
                joom_timeout_second = int(joom_timeout)
            except ValueError:
                joom_timeout_command = ""
                joom_timeout_flag = 0
                print("\n[*] Invalid! Please enter numbers only!")
                useless = input("Enter any key to continue......")
                continue
            joom_timeout_flag = 1
            joom_timeout_command = "--timeout " + joom_timeout + " "
        #cookie
        elif joom_select == "5":
            joom_cookie = input("\nCookie (Format -> cookiename=cookievalue): ").strip()
            if joom_cookie == "":
                joom_cookie_command = ""
                joom_cookie_flag = 0
                print("\n[*] Cookie cannot be empty!")
                useless = input("Enter any key to continue......")
                continue
            #validate cookie format
            if "=" in joom_cookie:
                joom_cookie_list = joom_cookie.split("=")
                for i in range(len(joom_cookie_list)):
                    if joom_cookie_list[i] == "":
                        joom_cookie_command = ""
                        joom_cookie_flag = 0
                        print("\n[*] Invalid Cookie!")
                        useless = input("Enter any key to continue......")
                        continue
                if joom_cookie[-1] != ";":
                    joom_cookie_command = ""
                    joom_cookie_flag = 0
                    print("\n[*] Add a \";\" at the end of cookie!")
                    useless = input("Enter any key to continue......")
                    continue
                else:
                    joom_cookie_flag = 1
                    joom_cookie_command = "--cookie \"" + joom_cookie + "\" "
            else:
                joom_cookie_command = ""
                joom_cookie_flag = 0
                print("\n[*] Invalid Format!")
                useless = input("Enter any key to continue......")
                continue
        #Specify User Agent
        elif joom_select == "6":
            joom_user_agent = input("\nUser Agent: ").strip()
            if joom_user_agent == "":
                joom_useragent_command = ""
                print("\n[*] User Agent cannot be empty!")
                useless = input("Enter any key to continue......")
                continue
            joom_useragent_command = "-a \"" + joom_user_agent + "\" "
            joom_rua_flag = 0
            joom_rua_command = ""
        #Random User Agent
        elif joom_select == "7":
            if joom_rua_flag != 1:
                joom_rua_flag = 1
                joom_rua_command = "-r "
                joom_useragent_command = ""
                joom_user_agent = ""
            else:
                joom_rua_flag = 0
                joom_rua_command = ""

        #Launch attack
        elif joom_select == "90":
            if joom_target != "":
                joom_output_flag = 0
                joom_output_prompt = input("\nDo you want to save the result to file? (y/n): ")
                if joom_output_prompt == "y" or joom_output_prompt == "Y":
                    joom_output_filename = input("Enter the new filename: ").strip()
                    if joom_output_filename != "":
                        joom_output_flag = 1
                        joom_output_filename = joom_output_filename.replace(" ","_")
                        joom_final_command += " > ./result/" + joom_output_filename
                    else:
                        joom_output_flag = 0
                        print("\n[*] Filename cannot be empty!")
                        useless = input("Enter any key to continue......")
                        continue
                print("\033[1;32m[+] Starting JoomScan......\033[00m")
                os.system(joom_final_command)
                if joom_output_flag == 1:
                    print("\033[1;32m[+] File saved to ./result/{}\033[00m".format(joom_output_filename))
                useless = input("[*] Process Completed! Enter any key to continue......")
            else:
                print("\n[*] Target cannot be empty!")
                useless = input("Enter any key to continue......")
                continue

def main():
    print("\033[1;32m[+] Loading JoomScan Module\033[00m")
    if joomscan_self_check() == 1:
        joom_main()
    else:
        print("\n\033[1;31m[-] JoomScan is not installed!\033[00m")
        useless = input("Enter any key to continue......")