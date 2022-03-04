import os
import subprocess

def hydra_self_check():
    hydra_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^hydra/'", shell=True, stdout=subprocess.PIPE)
    hydra_checkstatusd = hydra_checkstatus.stdout.decode('ascii')
    if "installed" in hydra_checkstatusd or "upgradable" in hydra_checkstatusd:
        return 1
    else:
        return 0

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
        hydra_port_banner = "Specify if the service is not running on default port"
    else:
        hydra_port_banner = "\033[1;32m" + hydra_port_command.replace("-s","").strip() + "\033[00m"
    
    if hydra_webform_command == "":
        hydra_webform_banner = "For http(s)-get(post)-form only"
    else:
        hydra_webform_banner = "\033[1;32m" + hydra_webform_command.replace("\"","").strip() + "\033[00m"

    os.system("clear")
    print("""
                          Network Logon Cracker (Hydra)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target       : \033[1;32m"""+hydra_target_command+"""\033[00m
    2. Service      : \033[1;32m"""+hydra_service_command+"""\033[00m

    3. Port         : """+hydra_port_banner+"""
    4. Web Form     : """+hydra_webform_banner+"""


    x.Quit once found positive -f   


Command: \033[1;32m"""+hydra_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
    """)


def hydra_main():
    global hydra_final_command, hydra_target_command, hydra_service_command, hydra_port_command, hydra_webform_command

    hydra_target_command = ""
    hydra_service_command = ""
    hydra_port_command = ""
    hydra_webform_command = ""
    hydra_cookie_command = ""

    hydra_select = ""
    while hydra_select != "99":
        hydra_final_command = "hydra " + hydra_target_command + hydra_service_command + hydra_webform_command + hydra_port_command 
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
            print("\n[*] Type manually or enter \"service\" to view and select Hydra-supported services.")
            hydra_service = input("Service: ").strip()
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
            hydra_service_command = hydra_service + " "
        #port
        elif hydra_select == "3":
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
        elif hydra_select == "4":
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


def main():
    print("\033[1;32m[+] Loading Hydra Module\033[00m")
    if hydra_self_check() == 1:
        hydra_main()
    else:
        print("\n\033[1;31m[-] Hydra is not installed!\033[00m")
        useless = input("Enter any key to continue......")