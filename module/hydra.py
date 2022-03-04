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

def hydra_banner():
    

    os.system("clear")
    print("""
                          Network Logon Cracker (Hydra)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target       : \033[1;32m"""+hydra_target_command+"""\033[00m
    2. Service      : \033[1;32m"""+hydra_service_command+"""\033[00m

    3. Port         : Specify if the service is not running on default port
    4. 


    x.Quit once found positive -f   


Command: \033[1;32m"""+hydra_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
    """)


def hydra_main():
    global hydra_final_command, hydra_target_command, hydra_service_command

    hydra_target_command = ""
    hydra_service_command = ""

    hydra_select = ""
    while hydra_select != "99":
        hydra_final_command = "hydra " + hydra_target_command + hydra_service_command
        hydra_banner()
        hydra_select = input("\nSelect: ").strip()
        if hydra_select == "1":
            hydra_target = input("Target IP / Hostname / Domain name: ").strip()
            if hydra_target == "" or " " in hydra_target:
                hydra_target_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            hydra_target_command = hydra_target + " "
        elif hydra_select == "2":
            print("\n[*] Type \"showservice\" to view all Hydra-supported services.")
            hydra_service = input("Service: ").strip()
            if hydra_service == "" or " " in hydra_service:
                hydra_service_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if hydra_service.startswith("showservi") == True:
                hydra_service_banner()
                hydra_service = ""
                hydra_banner()
                hydra_service = input("\nService: ").strip()
                if hydra_service == "" or " " in hydra_service:
                    hydra_service_command = ""
                    print("\n[*] Field is empty / contain space!")
                    useless = input("Enter any key to continue......")
                    continue
            hydra_service_command = hydra_service + " "


def main():
    print("\033[1;32m[+] Loading Hydra Module\033[00m")
    if hydra_self_check() == 1:
        hydra_main()
    else:
        print("\n\033[1;31m[-] Hydra is not installed!\033[00m")
        useless = input("Enter any key to continue......")