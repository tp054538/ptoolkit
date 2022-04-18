#Written By: Foong Yew Joe (TP054538)
#Description: Use hydra to crack login on different services with dictionary attack
#First Written Date: 10 March 2022
#Last Edited: 18 April 2022

import os
import subprocess
from module.sniper_scan import check_file_exist

def hydra_self_check():
    hydra_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^hydra/'", shell=True, stdout=subprocess.PIPE)
    hydra_checkstatusd = hydra_checkstatus.stdout.decode('ascii')
    if "installed" in hydra_checkstatusd or "upgradable" in hydra_checkstatusd:
        return 1
    else:
        return 0

def hydra_check_supported_service(hydraservice):
    hydra_valid_service_list = []
    with open("module/config/hydra_supported_service") as file:
        valid_service = file.readlines()
        for line in valid_service:
            hydra_valid_service_list.append(line.replace("\n","").strip())
        file.close()
    #validate service input is supported
    for i in range(len(hydra_valid_service_list)):
        if hydraservice.strip() == hydra_valid_service_list[i].strip():
            return 1
    return 0

def hydra_password_provided_wordlist():
    os.system("clear")
    print("""
                         Password Wordlists (SecLists)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. xato-net-10-million-passwords-1000000.txt
    2. xato-net-10-million-passwords-100000.txt
    3. xato-net-10-million-passwords-10000.txt
    4. Most-Popular-Letter-Passes.txt
    5. 10-million-password-list-top-1000000.txt
    6. 10-million-password-list-top-100000.txt
    7. 10k-most-common.txt
    8. 100k-most-used-passwords-NCSC.txt
    9. elitehacker.txt    (leaked database)
   10. hotmail.txt          (leaked database)
   11. NordVPN.txt          (leaked database)

*for more wordlists, browse at ./Wordlists/Passwords/ directory
   99. Exit
""")
    wordlist_directory = os.getcwd() + "/Wordlists/Passwords/"
    hydra_wordlist_select = input("\nSelect: ").strip()
    if hydra_wordlist_select == "1":
        return wordlist_directory + "xato-net-10-million-passwords-1000000.txt"
    elif hydra_wordlist_select == "2":
        return wordlist_directory + "xato-net-10-million-passwords-100000.txt"
    elif hydra_wordlist_select == "3":
        return wordlist_directory + "xato-net-10-million-passwords-10000.txt"
    elif hydra_wordlist_select == "4":
        return wordlist_directory + "Most-Popular-Letter-Passes.txt"
    elif hydra_wordlist_select == "5":
        return wordlist_directory + "Common-Credentials/10-million-password-list-top-1000000.txt"
    elif hydra_wordlist_select == "6":
        return wordlist_directory + "Common-Credentials/10-million-password-list-top-100000.txt"
    elif hydra_wordlist_select == "7":
        return wordlist_directory + "Common-Credentials/10k-most-common.txt"
    elif hydra_wordlist_select == "8":
        return wordlist_directory + "Common-Credentials/100k-most-used-passwords-NCSC.txt"
    elif hydra_wordlist_select == "9":
        return wordlist_directory + "Leaked-Databases/elitehacker.txt"
    elif hydra_wordlist_select == "10":
        return wordlist_directory + "Leaked-Databases/hotmail.txt"
    elif hydra_wordlist_select == "11":
        return wordlist_directory + "Leaked-Databases/NordVPN.txt"
    else:
        return ""

def hydra_username_provided_wordlist():
    os.system("clear")
    print("""
                          Username Wordlist (SecLists)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. cirt-default-usernames.txt
    2. xato-net-10-million-usernames-dup.txt
    3. CommonAdminBase64.txt
    4. sap-default-usernames.txt
    5. xato-net-10-million-usernames.txt
    6. mssql-usernames-nansh0u-guardicore.txt
    7. top-usernames-shortlist.txt

   99. Exit
""")
    wordlist_directory = os.getcwd() + "/Wordlists/Usernames/"
    hydra_wordlist_select = input("\nSelect: ").strip()
    if hydra_wordlist_select == "1":
        return wordlist_directory + "cirt-default-usernames.txt"
    elif hydra_wordlist_select == "2":
        return wordlist_directory + "xato-net-10-million-usernames-dup.txt"
    elif hydra_wordlist_select == "3":
        return wordlist_directory + "CommonAdminBase64.txt"
    elif hydra_wordlist_select == "4":
        return wordlist_directory + "sap-default-usernames.txt"
    elif hydra_wordlist_select == "5":
        return wordlist_directory + "xato-net-10-million-usernames.txt"
    elif hydra_wordlist_select == "6":
        return wordlist_directory + "mssql-usernames-nansh0u-guardicore.txt"
    elif hydra_wordlist_select == "7":
        return wordlist_directory + "top-usernames-shortlist.txt"
    else:
        return ""

def hydra_service_banner():
    hydra_service_banner_select = ""
    while hydra_service_banner_select != "99":
        os.system("clear")
        print("""
                          Hydra Supported Service
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. adam6500          2. asterisk        3. cisco        4. cisco-enable    
    5. cvs               6. firebird        7. ftp          8. ftps  
    9. http-head        10. http-get       11. http-post   12. https-head
   13. https-get        14. https-post                     15. http-get-form
   16. http-post-form   17. https-get-form                 18. https-post-form
   19. http-proxy       20. http-proxy-urlenum             21. icq
   22. imap             23. imaps          24. irc         25. ldap2
   26. ldap2s           27. ldap3          28. ldap3s      29. ldap3-crammd5
   30. ldap3-crammd5s   31. ldap3-digestmd5                32. ldap3-digestmd5s
   33. mssql            34. mysql          35. memcached   36. mongodb
   37. nntp             38. oracle-listener                39. oracle-sid
   40. pcanywhere       41. pcnfs          42. pop3        43. pop3s
   44. postgres         45. radmin2        46. rdp         47. redis
   48. rexec            49. rlogin         50. rpcap       51. rsh
   52. rtsp             53. s7-300         54. sip         55. smb
   56. smtp             57. smtps          58. smtp-enum   59. snmp
   60. socks5           61. ssh            62. sshkey      63. svn
   64. teamspeak        65. telnet         66. telnets     67. vmauthd
   68. vnc              69. xmpp

   99. \033[1;32mExit\033[00m
""")
        hydra_service_banner_select = input("\nSelect: ").strip()
        if hydra_service_banner_select == "1":
            return "adam6500"
        elif hydra_service_banner_select == "2":
            return "asterisk"
        elif hydra_service_banner_select == "3":
            return "cisco"
        elif hydra_service_banner_select == "4":
            return "cisco-enable"
        elif hydra_service_banner_select == "5":
            return "cvs"
        elif hydra_service_banner_select == "6":
            return "firebird"
        elif hydra_service_banner_select == "7":
            return "ftp"
        elif hydra_service_banner_select == "8":
            return "ftps"
        elif hydra_service_banner_select == "9":
            return "http-head"
        elif hydra_service_banner_select == "10":
            return "http-get"
        elif hydra_service_banner_select == "11":
            return "http-post"
        elif hydra_service_banner_select == "12":
            return "https-head"
        elif hydra_service_banner_select == "13":
            return "https-get"
        elif hydra_service_banner_select == "14":
            return "https-post"
        elif hydra_service_banner_select == "15":
            return "http-get-form"
        elif hydra_service_banner_select == "16":
            return "http-post-form"
        elif hydra_service_banner_select == "17":
            return "https-get-form"
        elif hydra_service_banner_select == "18":
            return "https-post-form"
        elif hydra_service_banner_select == "19":
            return "http-proxy"
        elif hydra_service_banner_select == "20":
            return "http-proxy-urlenum"
        elif hydra_service_banner_select == "21":
            return "icq"
        elif hydra_service_banner_select == "22":
            return "imap"
        elif hydra_service_banner_select == "23":
            return "imaps"
        elif hydra_service_banner_select == "24":
            return "irc"
        elif hydra_service_banner_select == "25":
            return "ldap2"
        elif hydra_service_banner_select == "26":
            return "ldap2s"
        elif hydra_service_banner_select == "27":
            return "ldap3"
        elif hydra_service_banner_select == "28":
            return "ldap3s"
        elif hydra_service_banner_select == "29":
            return "ldap3-crammd5"
        elif hydra_service_banner_select == "30":
            return "ldap3-crammd5s"
        elif hydra_service_banner_select == "31":
            return "ldap3-digestmd5"
        elif hydra_service_banner_select == "32":
            return "ldap3-digestmd5s"
        elif hydra_service_banner_select == "33":
            return "mssql"
        elif hydra_service_banner_select == "34":
            return "mysql"
        elif hydra_service_banner_select == "35":
            return "memcached"
        elif hydra_service_banner_select == "36":
            return "mongodb"
        elif hydra_service_banner_select == "37":
            return "nntp"
        elif hydra_service_banner_select == "38":
            return "oracle-listener"
        elif hydra_service_banner_select == "39":
            return "oracle-sid"
        elif hydra_service_banner_select == "40":
            return "pcanywhere"
        elif hydra_service_banner_select == "41":
            return "pcnfs"
        elif hydra_service_banner_select == "42":
            return "pop3"
        elif hydra_service_banner_select == "43":
            return "pop3s"
        elif hydra_service_banner_select == "44":
            return "postgres"
        elif hydra_service_banner_select == "45":
            return "radmin2"
        elif hydra_service_banner_select == "46":
            return "rdp"
        elif hydra_service_banner_select == "47":
            return "redis"
        elif hydra_service_banner_select == "48":
            return "rexec"
        elif hydra_service_banner_select == "49":
            return "rlogin"
        elif hydra_service_banner_select == "50":
            return "rpcap"
        elif hydra_service_banner_select == "51":
            return "rsh"
        elif hydra_service_banner_select == "52":
            return "rtsp"
        elif hydra_service_banner_select == "53":
            return "s7-300"
        elif hydra_service_banner_select == "54":
            return "sip"
        elif hydra_service_banner_select == "55":
            return "smb"
        elif hydra_service_banner_select == "56":
            return "smtp"
        elif hydra_service_banner_select == "57":
            return "smtps"
        elif hydra_service_banner_select == "58":
            return "smtp-enum"
        elif hydra_service_banner_select == "59":
            return "snmp"
        elif hydra_service_banner_select == "60":
            return "socks5"
        elif hydra_service_banner_select == "61":
            return "ssh"
        elif hydra_service_banner_select == "62":
            return "sshkey"
        elif hydra_service_banner_select == "63":
            return "svn"
        elif hydra_service_banner_select == "64":
            return "teamspeak"
        elif hydra_service_banner_select == "65":
            return "telnet"
        elif hydra_service_banner_select == "66":
            return "telnets"
        elif hydra_service_banner_select == "67":
            return "vmauthd"
        elif hydra_service_banner_select == "68":
            return "vnc"
        elif hydra_service_banner_select == "69":
            return "xmpp"
        else:
            return ""

def hydra_banner():
    if hydra_port_command == "":
        hydra_port_banner = "Specify only if the service is not running on default port"
    else:
        hydra_port_banner = "\033[1;32m" + hydra_port_command.replace("-s","").strip() + "\033[00m"
    
    if hydra_webform_command == "":
        hydra_webform_banner = "For http(s)-get(post)-form only"
    else:
        hydra_webform_banner = "\033[1;32m" + hydra_webform_command.replace("\"","").strip() + "\033[00m"
    
    if hydra_username_command == "":
        hydra_username_banner = "Username / Username Wordlist"
    elif "-l" in hydra_username_command:
        hydra_username_banner = "\033[1;32m" + hydra_username_command.replace("-l","").strip() + "\033[00m" + " (username)"
    elif "-L" in hydra_username_command:
        hydra_username_banner = "\033[1;32m" + hydra_username_command.replace("-L","").strip() + "\033[00m" + " (username wordlist)"

    if hydra_password_command == "":
        hydra_password_banner = "Password / Password Wordlist"
    elif "-p " in hydra_password_command:
        hydra_password_banner = "\033[1;32m" + hydra_password_command.replace("-p","").strip() + "\033[00m" + " (password)"
    elif "-P " in hydra_password_command:
        hydra_password_banner = "\033[1;32m" + hydra_password_command.replace("-P","").strip() + "\033[00m" + " (password wordlist)"
    
    if hydra_speed_command == "":
        hydra_speed_banner = "\033[1;32m" + "16 (Default)" + "\033[00m"
    else:
        hydra_speed_banner = "\033[1;32m" + hydra_speed_command.replace("-t","").strip() + "\033[00m"
    
    if hydra_exit_found_flag == 1:
        hydra_exit_found_color = "\033[1;32m" + "Exit when a pair of correct credential is found"
    else:
        hydra_exit_found_color = "\033[00m" + "Exit when a pair of correct credential found (Default = Test all values in wordlist)"

    if hydra_ssl_flag == 1:
        hydra_ssl_color = "\033[1;32m"
    else:
        hydra_ssl_color = "\033[00m"
    
    if hydra_verbose_flag == 1:
        hydra_verbose_color = "\033[1;32m"
    else:
        hydra_verbose_color = "\033[00m"

    os.system("clear")
    print("""
                          Network Logon Cracker (Hydra)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target       : \033[1;32m"""+hydra_target_command+"""\033[00m
    2. Service      : \033[1;32m"""+hydra_service_command+"""\033[00m
    3. Username     : """+hydra_username_banner+"""
    4. Password     : """+hydra_password_banner+"""

    5. Port         : """+hydra_port_banner+"""
    6. Web Form     : """+hydra_webform_banner+"""
    7. Speed        : """+hydra_speed_banner+"""
    8. """+hydra_exit_found_color+"""\033[00m
    9. """+hydra_ssl_color+"""Perform SSL Connect\033[00m
   10. """+hydra_verbose_color+"""Verbose\033[00m

Command: \033[1;32m"""+hydra_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
    """)


def hydra_main():
    global hydra_final_command, hydra_target_command, hydra_service_command, hydra_port_command, hydra_webform_command, hydra_username_command, hydra_password_command, hydra_speed_command, hydra_exit_found_flag
    global hydra_ssl_flag, hydra_verbose_flag
    hydra_target_command = ""
    hydra_service_command = ""
    hydra_port_command = ""
    hydra_webform_command = ""
    hydra_cookie_command = ""
    hydra_username_command = ""
    hydra_username_single = ""
    hydra_username_wordlist = ""
    hydra_password_single = ""
    hydra_password_command = ""
    hydra_password_wordlist = ""
    hydra_speed_command = ""
    hydra_exit_found_flag = 0
    hydra_exit_found_command = ""
    hydra_verbose_flag = 0
    hydra_verbose_command = ""
    hydra_ssl_flag = 0
    hydra_ssl_command = ""

    hydra_select = ""
    while hydra_select != "99":
        hydra_output_command = ""
        hydra_final_command = "hydra " + hydra_username_command + hydra_password_command + hydra_speed_command + hydra_exit_found_command
        hydra_final_command += hydra_port_command + hydra_ssl_command + hydra_verbose_command + hydra_target_command + hydra_service_command + hydra_webform_command 
        hydra_banner()
        hydra_select = input("\nSelect: ").strip()
        #target
        if hydra_select == "1":
            hydra_target = input("Target IP / Hostname / Domain name: ").strip()
            if hydra_target == "" or " " in hydra_target:
                hydra_target_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            hydra_target_command = hydra_target + " "
        #service
        elif hydra_select == "2":
            print("\n[*] Type manually or enter \"\033[1;33mservice\033[00m\" to view and select Hydra-supported services.")
            hydra_service = input("Service: ").strip().lower()
            if hydra_service == "" or " " in hydra_service:
                hydra_service_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if hydra_service == "service" or hydra_service == "Service":
                hydra_service = hydra_service_banner()
                hydra_banner()
                if hydra_service == "":
                    hydra_service_command = ""
                    print("\n[*] No service selected!")
                    useless = input("Enter any key to continue......")
                    continue
            if hydra_check_supported_service(hydra_service) == 0:
                hydra_service_command = ""
                print("\n[*] Invalid service selected! Please check hydra-supported service first.")
                useless = input("Enter any key to continue......")
                continue
            hydra_service_command = hydra_service + " "
        #username
        elif hydra_select == "3":
            hydra_username_prompt = input("Type \"u\" for single username, \"w\" for username wordlist file. (u/w): ").strip()
            #single username
            if hydra_username_prompt == "u" or hydra_username_prompt == "U":
                hydra_username_single = input("\nUsername / Login name: ").strip()
                if hydra_username_single == "" or " " in hydra_username_single:
                    hydra_username_single = ""
                    hydra_username_command = ""
                    print("\n[*] Field is empty / contain space!")
                    useless = input("Enter any key to continue......")
                    continue
                hydra_username_wordlist = ""
            #wordlist
            elif hydra_username_prompt == "w" or hydra_username_prompt == "W":
                hydra_username_provided_prompt = input("Do you want to use provided wordlist? (y/n): ").strip()
                if hydra_username_provided_prompt == "y" or hydra_username_provided_prompt == "Y":
                    hydra_username_wordlist = hydra_username_provided_wordlist()
                    if hydra_username_wordlist == "":
                        hydra_username_command = ""
                        print("\n[*] No File Selected!")
                        useless = input("Enter any key to continue......")
                        continue
                else:
                    hydra_username_wordlist = input("\nWordlist Location: ").strip()
                    if hydra_username_wordlist == "" or " " in hydra_username_wordlist:
                        hydra_username_wordlist = ""
                        hydra_username_command = ""
                        print("\n[*] Field is empty / contain space!")
                        useless = input("Enter any key to continue......")
                        continue
                if check_file_exist(hydra_username_wordlist) != 1:
                    hydra_username_wordlist = ""
                    hydra_username_command = ""
                    print("\n[*] File not found!")
                    useless = input("Enter any key to continue......")
                    continue
                hydra_username_single = ""
            else:
                hydra_username_command = ""
                print("\n[*] Error! Enter \"w\" or \"u\" only.")
                useless = input("Enter any key to continue......")
                continue
            if hydra_username_single == "" and hydra_username_wordlist != "":
                hydra_username_command = "-L " + hydra_username_wordlist + " "
            elif hydra_username_single != "" and hydra_username_wordlist == "":
                hydra_username_command = "-l " + hydra_username_single + " "
        #password
        elif hydra_select == "4":
            hydra_password_prompt = input("Type \"p\" for single password, \"w\" for password wordlist file. (p/w): ").strip()
            #single username
            if hydra_password_prompt == "p" or hydra_password_prompt == "P":
                hydra_password_single = input("\nPassword: ").strip()
                if hydra_password_single == "" or " " in hydra_password_single:
                    hydra_password_single = ""
                    hydra_password_command = ""
                    print("\n[*] Field is empty / contain space!")
                    useless = input("Enter any key to continue......")
                    continue
                hydra_password_wordlist = ""
            #wordlist
            elif hydra_password_prompt == "w" or hydra_password_prompt == "W":
                hydra_password_provided_prompt = input("Do you want to use provided wordlist? (y/n): ").strip()
                if hydra_password_provided_prompt == "y" or hydra_password_provided_prompt == "Y":
                    hydra_password_wordlist = hydra_password_provided_wordlist() 
                    if hydra_password_wordlist == "":
                        hydra_password_command = ""
                        print("\n[*] No File Selected!")
                        useless = input("Enter any key to continue......")
                        continue
                else:
                    hydra_password_wordlist = input("\nWordlist Location: ").strip()
                    if hydra_password_wordlist == "" or " " in hydra_password_wordlist:
                        hydra_password_wordlist = ""
                        hydra_password_command = ""
                        print("\n[*] Field is empty / contain space!")
                        useless = input("Enter any key to continue......")
                        continue
                if check_file_exist(hydra_password_wordlist) != 1:
                    hydra_password_wordlist = ""
                    hydra_password_command = ""
                    print("\n[*] File not found!")
                    useless = input("Enter any key to continue......")
                    continue
                hydra_password_single = ""
            else:
                hydra_password_command = ""
                print("\n[*] Error! Enter \"w\" or \"p\" only.")
                useless = input("Enter any key to continue......")
                continue
            if hydra_password_single == "" and hydra_password_wordlist != "":
                hydra_password_command = "-P " + hydra_password_wordlist + " "
            elif hydra_password_single != "" and hydra_password_wordlist == "":
                hydra_password_command = "-p " + hydra_password_single + " "
        #port
        elif hydra_select == "5":
            hydra_port = input("\nPort: ").strip()
            if hydra_port == "" or " " in hydra_port:
                hydra_port = ""
                hydra_port_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            try:
                hydra_port_validate = int(hydra_port)
                if hydra_port_validate < 1 or hydra_port_validate > 65535:
                    raise ValueError
            except ValueError:
                hydra_port = ""
                hydra_port_command = ""
                print("\n[*] Port number invalid!")
                useless = input("Enter any key to continue......")
                continue
            hydra_port_command = "-s " + hydra_port + " " 
        #web form
        elif hydra_select == "6":
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nFormat -> URL:Parameters:Correct/Incorrect Strings")
            print("URL:user=^USER^&pass=^PASS^:F=incorrectstrings(S=correctstrings)")
            print("\n1. As above, \"user\" and \"pass\" are the data parameter name send to the server. ^USER^ and ^PASS^ are the placeholder for parameter value for hydra to brute force.")
            print("\n2. F= is the strings shown when an incorrect credentials entered. S= is the strings appeared after correct credentials. S= could be ignored if unknown.")
            print("\n3. Additionally, if the client send other parameters to the server other than username and password, you can add/change parameters name and values inside.")
            print("\nEg. \"/login.php:username=^USER^&password=^PASS^&Submit=Submit&Token=anc23FO3N5M:F=Failed\"")
            print("*Cookies will be prompted after this if required.")
            hydra_webform = input("\nWeb Form: ").strip()
            if hydra_webform == "":
                hydra_webform_command = ""
                print("\n[*] Field is empty!")
                useless = input("Enter any key to continue......")
                continue
            if ":" not in hydra_webform:
                hydra_webform_command = ""
                print("\n[*] No \":\" Used!")
                useless = input("Enter any key to continue......")
                continue
            if "^USER^" not in hydra_webform or "^PASS^" not in hydra_webform:
                hydra_webform = ""
                hydra_webform_command = ""
                print("\n[*] ^USER^ and ^PASS^ both must be used to test username and password values!")
                useless = input("Enter any key to continue......")
                continue
            if "=^USER^" not in hydra_webform.split(":")[1] or "=^PASS^" not in hydra_webform.split(":")[1]:
                hydra_webform = ""
                hydra_webform_command = ""
                print("\n[*] =^USER^ and =^PASS^ must be placed at the section after URL's \":\"!")
                useless = input("Enter any key to continue......")
                continue
            if hydra_webform.startswith("/") == False:
                hydra_webform = ""
                hydra_webform_command = ""
                print("\n[*] Start web form with \"/\" !")
                useless = input("Enter any key to continue......")
                continue
            if len(hydra_webform.split(":")) < 3:
                hydra_webform = ""
                hydra_webform_command = ""
                print("\n[*] Atleast two \":\" must be used to seperate URL, Parameters, and Incorrect/Correct String !")
                useless = input("Enter any key to continue......")
                continue
            if "F=" not in hydra_webform and "S=" not in hydra_webform:
                hydra_webform = ""
                hydra_webform_command = ""
                print("\n[*] F= and S= not found! At least one must be specified to determine whether the credentials is correct.")
                useless = input("Enter any key to continue......")
                continue
            hydra_cookie_prompt = input("\nIs cookie required? (y/n): ").strip()
            if hydra_cookie_prompt == "y" or hydra_cookie_prompt == "Y":
                hydra_cookie = input("\nCookie (use ; as seperator): ").strip()
                if hydra_cookie == "":
                    hydra_webform = ""
                    hydra_webform_command = ""
                    hydra_cookie_command = ""
                    print("\n[*] Field is empty!")
                    useless = input("Enter any key to continue......")
                    continue
                if "=" not in hydra_cookie:
                    hydra_webform = ""
                    hydra_webform_command = ""
                    hydra_cookie = ""
                    hydra_cookie_command = ""
                    print("\n[*] Error Cookie! No \"=\" Detected!")
                    useless = input("Enter any key to continue......")
                    continue
                hydra_cookie_command = ":H=Cookie\: " + hydra_cookie
            hydra_webform_command = "\"" + hydra_webform.strip() + hydra_cookie_command.strip() + "\" "
        #speed
        elif hydra_select == "7":
            try:
                hydra_speed = int(input("\nSpeed: ").strip())
                if hydra_speed < 1:
                    raise ValueError
            except ValueError:
                hydra_speed = 16
                hydra_speed_command = ""
                print("\n[*] Error Value!")
                useless = input("Enter any key to continue......")
                continue
            if hydra_speed != 16:
                hydra_speed_command = "-t " + str(hydra_speed) + " "
            else:
                hydra_speed_command = ""
        #exit once found
        elif hydra_select == "8":
            if hydra_exit_found_flag != 1:
                hydra_exit_found_flag = 1
                hydra_exit_found_command = "-f "
            else:
                hydra_exit_found_flag = 0
                hydra_exit_found_command = ""
        #SSL Connect
        elif hydra_select == "9":
            if hydra_ssl_flag != 1:
                hydra_ssl_flag = 1
                hydra_ssl_command = "-S "
            else:
                hydra_ssl_flag = 0
                hydra_ssl_command = ""
        #verbose
        elif hydra_select == "10":
            if hydra_verbose_flag != 1:
                hydra_verbose_flag = 1
                hydra_verbose_command = "-v "
            else:
                hydra_verbose_flag = 0
                hydra_verbose_command = ""
        #launch attack
        elif hydra_select == "90":
            #check required field is empty (1~4)
            if hydra_target_command == "":
                print("\n[*] Target is required!")
                useless = input("Enter any key to continue......")
                continue
            if hydra_service_command == "":
                print("\n[*] Service is required!")
                useless = input("Enter any key to continue......")
                continue
            if hydra_username_command == "":
                print("\n[*] Username / username wordlist is required!")
                useless = input("Enter any key to continue......")
                continue
            if hydra_password_command == "":
                print("\n[*] Password / password wordlist is required!")
                useless = input("Enter any key to continue......")
                continue
            if hydra_service_command.strip() == "http-get-form" or hydra_service_command.strip() == "http-post-form" or hydra_service_command.strip() == "https-get-form" or hydra_service_command.strip() == "https-post-form":
                if hydra_webform_command == "":
                    print("\n[*] Web Form is required for {}!".format(hydra_service_command))
                    useless = input("Enter any key to continue......")
                    continue
            #prompt for output
            hydra_output_prompt = input("\nDo you want to save result to file? (y/n)").strip()
            if hydra_output_prompt == "y" or hydra_output_prompt == "Y":
                hydra_filename = input("\nEnter a name for new file: ").strip().replace(" ","_")
                if hydra_filename == "":
                    print("\n[*] Field is empty!")
                    useless = input("Enter any key to continue......")
                    continue
                hydra_output_command = " -o ./result/" + hydra_filename
            #launch
            print("\033[1;32m[+] Starting Hydra......\033[00m")
            if hydra_output_command == "":
                os.system(hydra_final_command)
            else:
                os.system(hydra_final_command+hydra_output_command)
                print("\033[1;32m[+] File saved to {}\033[00m".format(hydra_output_command.replace("-o","").strip()))
            useless = input("[*] Process Completed! Enter any key to continue......")


def main():
    print("\033[1;32m[+] Loading Hydra Module\033[00m")
    if hydra_self_check() == 1:
        hydra_main()
    else:
        print("\n\033[1;31m[-] Hydra is not installed!\033[00m")
        useless = input("Enter any key to continue......")