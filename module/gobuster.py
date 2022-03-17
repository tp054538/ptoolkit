import os
import subprocess
from module import sniper_scan

def gobuster_self_check():
    gobuster_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^gobuster/'", shell=True, stdout=subprocess.PIPE)
    gobuster_checkstatusd = gobuster_checkstatus.stdout.decode('ascii')
    if "installed" in gobuster_checkstatusd or "upgradable" in gobuster_checkstatusd:
        return 1
    else:
        return 0

def gobuster_wordlist_select_func():
    os.system("clear")
    print("""
                Wordlists for Dir & File Brute Force (SecLists)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. directory-list-1.0.txt
    2. directory-list-2.3-big.txt
    3. directory-list-2.3-medium.txt
    4. directory-list-2.3-small.txt
    5. directory-list-lowercase-2.3-big.txt
    6. directory-list-lowercase-2.3-medium.txt
    7. directory-list-lowercase-2.3-small.txt
    8. dirsearch.txt

   99. Exit
""")
    wordlist_directory = os.getcwd() + "/Wordlists/Web-Discovery/"
    gobuster_wordlist_select = input("\nSelect: ").strip()
    if gobuster_wordlist_select == "1":
        return wordlist_directory + "directory-list-1.0.txt"
    elif gobuster_wordlist_select == "2":
        return wordlist_directory + "directory-list-2.3-big.txt"
    elif gobuster_wordlist_select == "3":
        return wordlist_directory + "directory-list-2.3-medium.txt"
    elif gobuster_wordlist_select == "4":
        return wordlist_directory + "directory-list-2.3-small.txt"
    elif gobuster_wordlist_select == "5":
        return wordlist_directory + "directory-list-lowercase-2.3-big.txt"
    elif gobuster_wordlist_select == "6":
        return wordlist_directory + "directory-list-lowercase-2.3-medium.txt"
    elif gobuster_wordlist_select == "7":
        return wordlist_directory + "directory-list-lowercase-2.3-small.txt"
    elif gobuster_wordlist_select == "8":
        return wordlist_directory + "dirsearch.txt"
    else:
        return ""

def gobuster_banner():
    if gobuster_wordlist_command == "":
        gobuster_wordlist_banner = ""
    else:
        gobuster_wordlist_banner = gobuster_wordlist_command.replace("-w","").strip()

    if gobuster_target_command == "":
        gobuster_target_banner = ""
    else:
        gobuster_target_banner = gobuster_target_command.replace("-u","").strip()
    
    if gobuster_cookie_command == "":
        gobuster_cookie_banner = ""
    else:
        gobuster_cookie_banner = gobuster_cookie_command.replace("-c","").replace("\"","").strip()
    
    if gobuster_positive_command == "":
        gobuster_positive_banner = "Specify positive HTTP status code (Default = 200,204,301,302,307,401,403)"
    else:
        gobuster_positive_banner = "\033[1;32m" + gobuster_positive_command.replace("-s","").strip() + "\033[00m"
    
    if gobuster_negative_command == "":
        gobuster_negative_banner = "Specify negative HTTP status codes (Default = 404)"
    else:
        gobuster_negative_banner = "\033[1;32m" + gobuster_negative_command.replace("-b","").strip() + "\033[00m"
    
    if gobuster_follow_redir_flag == 1:
        gobuster_follow_redir_color = "\033[1;32m"
    else:
        gobuster_follow_redir_color = "\033[00m"
    
    if gobuster_rua_flag == 1:
        gobuster_rua_color = "\033[1;32m"
    else:
        gobuster_rua_color = "\033[00m"
    
    if gobuster_ua_command == "":
        gobuster_ua_banner = "Use specified user agent for brute forcing"
    else:
        gobuster_ua_banner = "\033[1;32m" + gobuster_ua_command.replace("-a","").replace("\"","").strip() + "\033[00m"
    
    if gobuster_file_ext_command == "":
        gobuster_file_ext_banner = "Specify file extension to search for"
    else:
        gobuster_file_ext_banner = "\033[1;32m" + gobuster_file_ext_command.replace("-x","").strip() + "\033[00m"
    
    if gobuster_threads_command == "":
        gobuster_threads_banner = "Set maximum concurrent threads (Default = 10)"
    else:
        gobuster_threads_banner = "\033[1;32m" + gobuster_threads_command.replace("-t","").strip() + "\033[00m"
    
    if gobuster_verbose_flag == 1:
        gobuster_verbose_color = "\033[1;32m"
    else:
        gobuster_verbose_color = "\033[00m"
    
    if gobuster_queit_flag == 1:
        gobuster_queit_color = "\033[1;32m"
    else:
        gobuster_queit_color = "\033[00m"

    os.system("clear")
    print("""
                    Directory and Files Discovery (GoBuster)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target URL        : \033[1;32m"""+gobuster_target_banner+"""\033[00m
    2. Wordlist          : \033[1;32m"""+gobuster_wordlist_banner+"""\033[00m

    3. Cookie            : \033[1;32m"""+gobuster_cookie_banner+"""\033[00m
    4. Positive Codes    : """+gobuster_positive_banner+"""
    5. Negative Codes    : """+gobuster_negative_banner+"""
    6. """+gobuster_follow_redir_color+"""Follow redirect\033[00m   - Follow redirection
    7. """+gobuster_rua_color+"""Random User Agent\033[00m - Use random user agent for brute forcing
    8. User Agent        : """+gobuster_ua_banner+"""
    9. File Extension    : """+gobuster_file_ext_banner+"""
   10. Threads           : """+gobuster_threads_banner+"""
   11. """+gobuster_verbose_color+"""Verbose\033[00m           - Display more information
   12. """+gobuster_queit_color+"""Quiet\033[00m             - No display banner and lesser noise

Command: """+gobuster_final_command+"""

   90. Launch Attack
   99. Exit
""")
    

def gobuster_main():
    global gobuster_final_command, gobuster_wordlist_command, gobuster_target_command, gobuster_cookie_command, gobuster_positive_command, gobuster_negative_command, gobuster_follow_redir_flag
    global gobuster_rua_flag, gobuster_ua_command, gobuster_file_ext_command, gobuster_threads_command, gobuster_verbose_flag, gobuster_queit_flag
    gobuster_wordlist_command = ""
    gobuster_target_command = ""
    gobuster_cookie_command = ""
    gobuster_positive_command = ""
    gobuster_negative_command = ""
    gobuster_follow_redir_flag = 0
    gobuster_follow_redir_command = ""
    gobuster_rua_flag = 0
    gobuster_rua_command = ""
    gobuster_ua_command = ""
    gobuster_file_ext_command = ""
    gobuster_threads_command = ""
    gobuster_verbose_flag = 0
    gobuster_verbose_command = ""
    gobuster_queit_flag = 0
    gobuster_queit_command = ""

    gobuster_select = ""
    while gobuster_select != "99":
        gobuster_output_command = ""
        gobuster_final_command = "gobuster dir " + gobuster_target_command + gobuster_wordlist_command + gobuster_cookie_command + gobuster_positive_command + gobuster_negative_command + gobuster_follow_redir_command
        gobuster_final_command += gobuster_file_ext_command + gobuster_rua_command + gobuster_ua_command + gobuster_threads_command + gobuster_verbose_command + gobuster_queit_command
        gobuster_banner()
        gobuster_select = input("\nSelect: ").strip()
        #target url
        if gobuster_select == "1":
            gobuster_target = input("\nTarget URL (Specify https:// if the website is running on https) or IP: ").strip()
            if gobuster_target == "" or " " in gobuster_target:
                gobuster_target = ""
                gobuster_target_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            gobuster_target_command = "-u " + gobuster_target + " "
        #wordlist -> check file exit & user can use provided wordlist
        elif gobuster_select == "2":
            gobuster_wordlist_prompt = input("\nDo you want to use provided wordlists? (y/n): ").strip()
            if gobuster_wordlist_prompt == "y" or gobuster_wordlist_prompt == "Y":
                gobuster_wordlist = gobuster_wordlist_select_func()
            else:
                gobuster_wordlist = input("\nWordlists Location: ").strip()
                if gobuster_wordlist == "" or " " in gobuster_wordlist:
                    gobuster_wordlist = ""
                    gobuster_wordlist_command = ""
                    print("\n[*] Field is empty / contain space!")
                    useless = input("Enter any key to continue......")
                    continue
            if sniper_scan.check_file_exist(gobuster_wordlist) != 1:
                    gobuster_wordlist = ""
                    gobuster_wordlist_command = ""
                    print("\n[*] File Not Found!")
                    useless = input("Enter any key to continue......")
                    continue
            gobuster_wordlist_command = "-w " + gobuster_wordlist + " "
        #cookie
        elif gobuster_select == "3":
            gobuster_cookie = input("\nCookie (Format is name=value, Eg. token=aJSIuM2N0D893) (use ; as seperator): \n").strip()
            if gobuster_cookie == "" or " " in gobuster_cookie:
                gobuster_cookie = ""
                gobuster_cookie_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if "=" not in gobuster_cookie:
                gobuster_cookie = ""
                gobuster_cookie_command = ""
                print("\n[*] Error Format! Format -> Cookiename=CookieValue")
                useless = input("Enter any key to continue......")
                continue
            gobuster_cookie_command = "-c \"" + gobuster_cookie + "\" "
        #positive code
        elif gobuster_select == "4":
            gobuster_positive_code = input("\nPositive Status Code (use , as seperator): ").strip().strip(",")
            if gobuster_positive_code == "" or " " in gobuster_positive_code:
                gobuster_positive_code = ""
                gobuster_positive_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            #validate status code format
            if len(gobuster_positive_code) < 3:
                gobuster_positive_code = ""
                gobuster_positive_command = ""
                print("\n[*] Error HTTP status code")
                useless = input("Enter any key to continue......")
                continue
            elif len(gobuster_positive_code) > 3:
                if "," not in gobuster_positive_code:
                    gobuster_positive_code = ""
                    gobuster_positive_command = ""
                    print("\n[*] Error format! Use \",\" as seperator for multiple status code.")
                    useless = input("Enter any key to continue......")
                    continue
                gobuster_positive_list = gobuster_positive_code.split(",")
                try:
                    for i in range(len(gobuster_positive_list)):
                        if len(gobuster_positive_list[i]) != 3:
                            raise ValueError
                        gobuster_positive_code_test = int(gobuster_positive_list[i])
                except ValueError:
                    gobuster_positive_code = ""
                    gobuster_positive_command = ""
                    print("\n[*] Error HTTP Status Code!")
                    useless = input("Enter any key to continue......")
                    continue
                #check duplicate
                if len(gobuster_positive_list) != len(set(gobuster_positive_list)):
                    gobuster_positive_code = ""
                    gobuster_positive_command = ""
                    print("\n[*] HTTP Status Code Duplicated!")
                    useless = input("Enter any key to continue......")
                    continue
            elif len(gobuster_positive_code) == 3:
                try:
                    gobuster_positive_test = int(gobuster_positive_code)
                except ValueError:
                    gobuster_positive_code = ""
                    gobuster_positive_command = ""
                    print("\n[*] Error HTTP Status Code!")
                    useless = input("Enter any key to continue......")
                    continue
            gobuster_negative_command = ""
            gobuster_positive_command = "-s " + gobuster_positive_code + " "
        #negative code
        elif gobuster_select == "5":
            gobuster_negative_code = input("\nNegative Status Code (use , as seperator): ").strip().strip(",")
            if gobuster_negative_code == "" or " " in gobuster_negative_code:
                gobuster_negative_code = ""
                gobuster_negative_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            #validate status code format
            if len(gobuster_negative_code) < 3:
                gobuster_negative_code = ""
                gobuster_negative_command = ""
                print("\n[*] Error HTTP status code")
                useless = input("Enter any key to continue......")
                continue
            elif len(gobuster_negative_code) > 3:
                if "," not in gobuster_negative_code:
                    gobuster_negative_code = ""
                    gobuster_negative_command = ""
                    print("\n[*] Error format! Use \",\" as seperator for multiple status code.")
                    useless = input("Enter any key to continue......")
                    continue
                gobuster_negative_list = gobuster_negative_code.split(",")
                try:
                    for i in range(len(gobuster_negative_list)):
                        if len(gobuster_negative_list[i]) != 3:
                            raise ValueError
                        gobuster_negative_code_test = int(gobuster_negative_list[i])
                except ValueError:
                    gobuster_negative_code = ""
                    gobuster_negative_command = ""
                    print("\n[*] Error HTTP Status Code!")
                    useless = input("Enter any key to continue......")
                    continue
                #check duplicate
                if len(gobuster_negative_list) != len(set(gobuster_negative_list)):
                    gobuster_negative_code = ""
                    gobuster_negative_command = ""
                    print("\n[*] HTTP Status Code Duplicated!")
                    useless = input("Enter any key to continue......")
                    continue
            elif len(gobuster_negative_code) == 3:
                try:
                    gobuster_negative_test = int(gobuster_negative_code)
                except ValueError:
                    gobuster_negative_code = ""
                    gobuster_negative_command = ""
                    print("\n[*] Error HTTP Status Code!")
                    useless = input("Enter any key to continue......")
                    continue
            gobuster_positive_command = ""
            gobuster_negative_command = "-b " + gobuster_negative_code + " "
        #follow redirect
        elif gobuster_select == "6":
            if gobuster_follow_redir_flag != 1:
                gobuster_follow_redir_flag = 1
                gobuster_follow_redir_command = "-r "
            else:
                gobuster_follow_redir_flag = 0
                gobuster_follow_redir_command = ""
        #random user agent
        elif gobuster_select == "7":
            if gobuster_rua_flag != 1:
                gobuster_rua_flag = 1
                gobuster_rua_command = "--random-agent "
                gobuster_ua_command = ""
            else:
                gobuster_rua_flag = 0
                gobuster_rua_command = ""
        #specify user agent
        elif gobuster_select == "8":
            gobuster_ua = input("\nUser Agent (Default = gobuster/3.1.0): ").strip()
            if gobuster_ua == "":
                gobuster_ua_command = ""
                print("\n[*] Field is empty!")
                useless = input("Enter any key to continue......")
                continue
            gobuster_ua_command = "-a \"" + gobuster_ua + "\" "
            gobuster_rua_flag = 0
            gobuster_rua_command = ""
        #file extension
        elif gobuster_select == "9":
            gobuster_file_ext = input("\nFile extension (use , as seperator for multiple extensions): ").strip().strip(",")
            if gobuster_file_ext == "" or " " in gobuster_file_ext:
                gobuster_file_ext = ""
                gobuster_file_ext_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            #check duplicate
            if "," in gobuster_file_ext:
                if len(gobuster_file_ext.split(",")) != len(set(gobuster_file_ext.split(","))):
                    gobuster_file_ext = ""
                    gobuster_file_ext_command = ""
                    print("\n[*] Duplicated file extension!")
                    useless = input("Enter any key to continue......")
                    continue
            gobuster_file_ext_command = "-x " + gobuster_file_ext + " "
        #threads
        elif gobuster_select == "10":
            try:
                gobuster_threads = int(input("Threads (Default = 10): ").strip())
                if gobuster_threads < 1:
                    raise ValueError
            except ValueError:
                gobuster_threads = ""
                gobuster_threads_command = ""
                print("\n[*] Positive numbers only!")
                useless = input("Enter any key to continue......")
                continue
            gobuster_threads_command = "-t " + str(gobuster_threads) + " "
        #verbose
        elif gobuster_select == "11":
            if gobuster_verbose_flag != 1:
                gobuster_verbose_flag = 1
                gobuster_verbose_command = "-v "
                gobuster_queit_flag = 0
                gobuster_queit_command = ""
            else:
                gobuster_verbose_flag = 0
                gobuster_verbose_command = ""
        #queit
        elif gobuster_select == "12":
            if gobuster_queit_flag != 1:
                gobuster_queit_flag = 1
                gobuster_queit_command = "-q "
                gobuster_verbose_flag = 0
                gobuster_verbose_command = ""
            else:
                gobuster_queit_flag = 0
                gobuster_queit_command = ""
        #launch attack
        elif gobuster_select == "90":
            if gobuster_target_command == "":
                print("\n[*] Target is empty!")
                useless = input("Enter any key to continue......")
                continue
            if gobuster_wordlist_command == "":
                print("\n[*] Wordlist is empty!")
                useless = input("Enter any key to continue......")
                continue
            gobuster_output_prompt = input("\nDo you want to save the result to a file? (y/n): ").strip()
            if gobuster_output_prompt == "y" or gobuster_output_prompt == "Y":
                gobuster_output_name = input("Enter a new filename: ").strip().replace(" ","_")
                if gobuster_output_name == "":
                    gobuster_output_command = ""
                    print("\n[*] Filename is empty!")
                    useless = input("Enter any key to continue......")
                    continue
                gobuster_output_command = "-o " +os.getcwd() + "/result/" + gobuster_output_name
            print("\033[1;32m[+] Starting GoBuster......\033[00m")
            os.system(gobuster_final_command+gobuster_output_command)
            if gobuster_output_command != "":
                print("\033[1;32m[+] File saved to {}\033[00m".format(gobuster_output_command.replace("-o","").strip()))
            useless = input("[*] Process Completed! Enter any key to continue......")

            
def main():
    print("\033[1;32m[+] Loading GoBuster Module\033[00m")
    if gobuster_self_check() == 1:
        gobuster_main()
    else:
        print("\n\033[1;31m[-] GoBuster is not installed!\033[00m")
        useless = input("Enter any key to continue......")