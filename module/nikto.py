import os
import subprocess

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
    
    if nikto_proxy_command != "":
        nikto_proxy_banner = "\033[1;32m" + nikto_proxy_command.strip().replace("-useproxy","").strip() + "\033[00m"
    else:
        nikto_proxy_banner = "Hide identity with proxy (HTTP proxy only)"

    if nikto_ua_command != "":
        nikto_ua_banner = "\033[1;32m" + nikto_ua_command.replace("-useragent","").strip().strip("\"") + "\033[00m"
    else:
        nikto_ua_banner = "Specify a User Agent (Not Specified -> use default)"
    
    if nikto_ignore_command != "":
        nikto_ignore_banner = "\033[1;32m" + nikto_ignore_command.replace("-404code","").strip() + "\033[00m"
    else:
        nikto_ignore_banner = "Ignore HTTP codes as negative responses."
    
    if nikto_db_flag == 1:
        nikto_db_color = "\033[1;32m"
    else:
        nikto_db_color = "\033[00m"
    
    if nikto_evasion_flag == 1:
        nikto_evasion_color = "\033[1;32m"
    else:
        nikto_evasion_color = "\033[00m"
    
    if nikto_ssl_flag == 1:
        nikto_ssl_color = "\033[1;32m"
    else:
        nikto_ssl_color = "\033[00m"

    if nikto_nossl_flag == 1:
        nikto_nossl_color = "\033[1;32m"
    else:
        nikto_nossl_color = "\033[00m"

    if nikto_nodns_flag == 1:
        nikto_nodns_color = "\033[1;32m"
    else:
        nikto_nodns_color = "\033[00m"
    
    if nikto_verbose_flag == 1:
        nikto_verbose_color = "\033[1;32m"
    else:
        nikto_verbose_color = "\033[00m"

    os.system("clear")
    print("""
                            Web Scanner (Nikto)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Host                 :   \033[1;32m"""+nikto_target+"""\033[00m

    2. Vhost                :   \033[1;32m"""+nikto_vhost+"""\033[00m
    3. Port                 :   """+nikto_port_banner+"""
    4. Proxy                :   """+nikto_proxy_banner+"""
    5. User Agent           :   """+nikto_ua_banner+"""
    6. Ignore HTTP codes    :   """+nikto_ignore_banner+"""

Mode:
    7. """+nikto_db_color+"""Database Check\033[00m       -   Check syntax error on database and key files
    8. """+nikto_evasion_color+"""Evasion\033[00m              -   Evade detection through encoding
    9. """+nikto_ssl_color+"""SSL\033[00m                  -   Force using SSL
   10. """+nikto_nossl_color+"""No SSL\033[00m               -   Disable SSL
   11. """+nikto_nodns_color+"""No DNS lookup\033[00m        -   Disable DNS lookup (Host should be in IP Address)
   12. """+nikto_verbose_color+"""Verbose\033[00m              -   Display more detailed information

Command: \033[1;32m"""+nikto_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
""")

def nikto_main():
    global nikto_final_command, nikto_target, nikto_vhost, nikto_port, nikto_port_command, nikto_proxy_command, nikto_ua_command, nikto_ignore_command, nikto_db_flag, nikto_evasion_flag
    global nikto_ssl_flag, nikto_nossl_flag, nikto_nodns_flag, nikto_verbose_flag
    nikto_target_command = ""
    nikto_target = ""
    nikto_vhost_command = ""
    nikto_vhost = ""
    nikto_port_command = ""
    nikto_port = ""
    nikto_proxy_command = ""
    nikto_ua_command = ""
    nikto_ignore_command = ""
    nikto_db_flag = 0
    nikto_db_command = ""
    nikto_evasion_flag = 0
    nikto_evasion_command = ""
    nikto_ssl_command = ""
    nikto_ssl_flag = 0
    nikto_nossl_command = ""
    nikto_nossl_flag = 0
    nikto_nodns_flag = 0
    nikto_nodns_command = ""
    nikto_verbose_flag = 0
    nikto_verbose_command = ""

    nikto_select = ""
    while nikto_select != "99":
        nikto_output_command = ""
        nikto_final_command = "nikto " + nikto_target_command + nikto_vhost_command + nikto_port_command + nikto_evasion_command + nikto_verbose_command + nikto_db_command + nikto_ignore_command 
        nikto_final_command +=  nikto_ssl_command + nikto_nossl_command + nikto_nodns_command + nikto_proxy_command + nikto_ua_command
        nikto_banner()
        nikto_select = input("\nSelect: ")
        #target host ip
        if nikto_select == "1":
            nikto_target = input("\nHost: ").strip()
            if nikto_target == "" or " " in nikto_target:
                nikto_target = ""
                nikto_target_command = ""
                print("\n[*] Host cannot be empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            nikto_target_command = "-h " + nikto_target + " "
        #vhost
        elif nikto_select == "2":
            nikto_vhost = input("\nVirtual Host: ").strip()
            if nikto_vhost == "" or " " in nikto_vhost:
                nikto_vhost_command = ""
                nikto_vhost = ""
                print("\n[*] VHost is empty / contain spaces!")
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
            print("\n[*] Nikto only support http proxy. Socks proxies are unavailable.")
            nikto_proxy = input("Proxy (http://ip:port): ").strip()
            if nikto_proxy == "":
                nikto_proxy_command = ""
                print("\n[*] Field is empty!")
                useless = input("Enter any key to continue......")
                continue
            if nikto_proxy.startswith("http://"):
                if len(nikto_proxy.replace("http://","").split(":")) == 2:
                    nikto_proxy_command = "-useproxy " + nikto_proxy + " "
                else:
                    nikto_proxy_command = ""
                    print("\n[*] Invalid Format! Format -> http://server:port")
                    useless = input("Enter any key to continue......")
                    continue
            else:
                nikto_proxy_command = ""
                print("\n[*] Please use HTTP proxy only. Format -> http://server:port")
                useless = input("Enter any key to continue......")
                continue
        #user agent
        elif nikto_select == "5":
            nikto_user_agent = input("\nUser Agent: ").strip()
            if nikto_user_agent == "":
                nikto_ua_command = ""
                print("\n[*] Field is empty!")
                useless = input("Enter any key to continue......")
                continue
            nikto_ua_command = "-useragent \"" + nikto_user_agent + "\" "
        #ignore http status code (3digit number only)
        elif nikto_select == "6":
            nikto_ignore_code = input("\nIgnore HTTP status code (use , as seperator): ").strip()
            if nikto_ignore_code == "":
                nikto_ignore_command = ""
                print("\n[*] Field is empty!")
                useless = input("Enter any key to continue......")
                continue
            #multiple code validation
            if len(nikto_ignore_code) > 3:
                if "," in nikto_ignore_code:
                    nikto_ignore_list = nikto_ignore_code.split(",")
                    #check each value is integer and not empty
                    try:
                        for i in range(len(nikto_ignore_list)):
                            nikto_ignore_validate = int(nikto_ignore_list[i])
                    except ValueError:
                        nikto_ignore_command = ""
                        print("\n[*] Invalid Format/Value!")
                        useless = input("Enter any key to continue......")
                        continue
                    #check each value is 3 digit (http status code)
                    try:
                        for i in range(len(nikto_ignore_list)):
                            if len(nikto_ignore_list[i]) != 3:
                                raise ValueError
                    except ValueError:
                        nikto_ignore_command = ""
                        print("\n[*] Invalid HTTP code!")
                        useless = input("Enter any key to continue......")
                        continue
                    nikto_ignore_command = "-404code " + nikto_ignore_code + " "
                else:
                    nikto_ignore_command = ""
                    print("\n[*] Invalid Format! Use , as seperator.")
                    useless = input("Enter any key to continue......")
                    continue
            #handle single http code
            else:
                if len(nikto_ignore_code) == 3:
                    try:
                        nikto_ignore_validate = int(nikto_ignore_code)
                    except ValueError:
                        nikto_ignore_command = ""
                        print("\n[*] Invalid HTTP code!")
                        useless = input("Enter any key to continue......")
                        continue
                    nikto_ignore_command = "-404code " + nikto_ignore_code + " "
                else:
                    nikto_ignore_command = ""
                    print("\n[*] Invalid HTTP code!")
                    useless = input("Enter any key to continue......")
                    continue
        #database check
        elif nikto_select == "7":
            if nikto_db_flag != 1:
                nikto_db_flag = 1
                nikto_db_command = "-dbcheck "
            else:
                nikto_db_flag = 0
                nikto_db_command = ""
        #evasion
        elif nikto_select == "8":
            if nikto_evasion_flag != 1:
                nikto_evasion_flag = 1
                nikto_evasion_command = "-evasion 1 "
            else:
                nikto_evasion_flag = 0
                nikto_evasion_command = ""
        #ssl
        elif nikto_select == "9":
            if nikto_ssl_flag != 1:
                nikto_ssl_flag = 1
                nikto_ssl_command = "-ssl "
                nikto_nossl_flag = 0
                nikto_nossl_command = ""
            else:
                nikto_ssl_flag = 0
                nikto_ssl_command = ""
        #no ssl
        elif nikto_select == "10":
            if nikto_nossl_flag != 1:
                nikto_nossl_flag = 1
                nikto_nossl_command = "-nossl "
                nikto_ssl_flag = 0
                nikto_ssl_command = ""
            else:
                nikto_nossl_flag = 0
                nikto_nossl_command = ""
        #no dns lookup
        elif nikto_select == "11":
            if nikto_nodns_flag != 1:
                nikto_nodns_flag = 1
                nikto_nodns_command = "-nolookup "
            else:
                nikto_nodns_flag = 0
                nikto_nodns_command = ""
        #verbose
        elif nikto_select == "12":
            if nikto_verbose_flag != 1:
                nikto_verbose_flag = 1
                nikto_verbose_command = "-Display V "
            else:
                nikto_verbose_flag = 0
                nikto_verbose_command = ""

        #launch attack
        elif nikto_select == "90":
            if nikto_target_command != "":
                ###check nodnslookup and target hots
                if nikto_nodns_flag == 1:
                    if len(nikto_target.split(".")) == 4:
                        try:
                            nikto_check_target_ip = nikto_target.split(".")
                            for i in range(len(nikto_check_target_ip)):
                                nikto_check_target_ip_isint = int(nikto_check_target_ip[i])
                        except ValueError:
                            print("\n[*] IP Address Format Invalid! Using No DNS lookup with domain name will cause an error.")
                            nikto_nodns_error_prompt = input("Do you wish to continue? (y/n): ").strip()
                            if nikto_nodns_error_prompt == "n" or nikto_nodns_error_prompt == "N":
                                continue
                    else:
                        print("\n[*] Target is not IP Address. No DNS lookup enabled will cause an error.")
                        nikto_nodns_error_prompt = input("Do you wish to continue? (y/n): ")
                        if nikto_nodns_error_prompt == "n" or nikto_nodns_error_prompt == "N":
                            continue
                #save to file prompt
                nikto_output_prompt = input("\nDo you want to save result to file? (y/n): ").strip()
                if nikto_output_prompt == "y" or nikto_output_prompt == "Y":
                    nikto_output_filename = input("\nEnter a name for new file: ").strip()
                    if nikto_output_filename == "":
                        print("\n[*] File name is empty!")
                        useless = input("Enter any key to continue......")
                        continue
                    nikto_output_filename = nikto_output_filename.replace(" ","_")
                    nikto_output_command = " -output ./result/" + nikto_output_filename + ".txt"
                #command
                print("\033[1;32m[+] Starting Nikto......\033[00m")
                if nikto_output_command == "":
                    os.system(nikto_final_command.strip())
                else:
                    os.system(nikto_final_command.strip() + nikto_output_command)
                    print("\033[1;32m[+] File saved to {}\033[00m".format(nikto_output_command.replace("-output ", "").strip()))
                useless = input("[*] Process Completed! Enter any key to continue......")
            else:
                print("\n[*] Target is empty!")
                useless = input("Enter any key to continue......")
                continue

def main():
    print("\033[1;32m[+] Loading Nikto Module\033[00m")
    if nikto_self_check() == 1:
        nikto_main()
    else:
        print("\n\033[1;31m[-] Nikto is not installed!\033[00m")
        useless = input("Enter any key to continue......")
