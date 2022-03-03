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
                Wordlists for Dir & File Brute FOrce (SecLists)

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

    os.system("clear")
    print("""
                    Directory and Files Discovery (GoBuster)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target URL        : 
    2. Wordlist          : \033[1;32m"""+gobuster_wordlist_banner+"""\033[00m

    3. Cookie            : 
    4. Follow redirect   : 
    5. Positive Codes    : Treat the specified status codes as positive response
    6. Negative Codes    : Treat the specified status codes as negative response (Default = 404)
    7. Random User Agent - Use random user agent for brute forcing
    8. User Agent        : Use specified user agent for brute forcing
    8. Threads           : Set maximum concurrent threads (Default = 10)
    9. Verbose           - Display more information
   10. Queit             - No display banner and lesser noise

Command: """+gobuster_final_command+"""

   90. Launch Attack
   99. Exit
""")
    

def gobuster_main():
    global gobuster_final_command, gobuster_wordlist_command
    gobuster_wordlist_command = ""

    gobuster_select = ""
    while gobuster_select != "99":
        gobuster_final_command = "gobuster " + gobuster_wordlist_command
        gobuster_banner()
        gobuster_select = input("\nSelect: ").strip()
        #target url
        if gobuster_select == "1":
            gobuster_target = input("\nTarget URL (Specify https:// if the website is running on https): ").strip()
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

#user agent default gobuster/3.1.0

def main():
    print("\033[1;32m[+] Loading GoBuster Module\033[00m")
    if gobuster_self_check() == 1:
        gobuster_main()
    else:
        print("\n\033[1;31m[-] GoBuster is not installed!\033[00m")
        useless = input("Enter any key to continue......")