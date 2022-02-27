import os
import PackageCheck
import PackageInstall
import PackageUpdate
import PackageUninstall
from module import *


def prRed(printinput):
    print("\033[91m{}\033[00m".format(printinput))

def RoE():
    print("|----------------------------------------------------------------|")
    print("|----------------------------------------------------------------|")
    print("|                       RULES OF ENGAGEMENT                      |")
    print("|Please note that  this toolkit is intended for learning  purpose|")
    print("|only. Do not use this toolkit on unauthorised target. The author|")
    print("|will not be responsible for any  action  performed by the user. |")
    print("|Users will be responsible for their action carried out. Improper|")
    print("|usage of this tools might be illegal and authorities might take |")
    print("|legal actions against the  user. Please use  this tools at your |")
    print("|own risk!                                                       |")
    print("|                                                                |")
    print("|*****Please enter \"1\" if you agree with the statement above*****|")
    print("|----------------------------------------------------------------|")
    print("|----------------------------------------------------------------|")
    print("                                                                  ")
    Answer = input("Answer:")
    return Answer

def banner():
    prRed("""
                     --------------------------
          ------------------------------------------------
--------------------------------------------------------------------
  _______    ________                    __   __               _
 |    _  \  |        |                  |  | |  |       /\    | |
 |   / \  \ |________|                  |  | |  |  ___  \/  __| |__
 |  |   |  |   |  |    ___       ___    |  | |  | /  /  __ |__   __|
 |   \_/  /    |  |  /  _  \   /  _  \  |  | |  |/  /  |  |   | |
 |   ____/     |  | |  / \  | |  / \  | |  | |     \   |  |   | |
 |  |          |  | |  \_/  | |  \_/  | |  | |  |\  \  |  |   | |
 |__|          |__|  \_____/   \_____/  |__| |__| \__\ |__|   |_|
--------------------------------------------------------------------
          ------------------------------------------------
                     --------------------------
""")
    #prYellow("Version: 1.0")
    print("\033[0;33mVersion: 1.0           ", end='')
    if tor.check_init() == 1:
        PackageCheck.prGreen("Tor is running on socks5://127.0.0.1:9050")
    else:
        print("        Tor is not running\033[00m", end='')

def main_menu():
    print("""
                                    Main Menu

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Install Tools            5. Reconnaissance               10. Exit

    2. Update Tools             6. Scanning

    3. Uninstall Tools          7. Exploitation

    4. Tor Proxy                8. Maintaining Access
    """)

def recon_menu():
    recon_input = ""
    while recon_input != "99":
        os.system("clear")
        print("""
                              Reconnaissance Menu

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Vulnerability Search (Searchsploit)   2. OSINT/Recon (Sn1per)                

   99. Exit
    """)
        recon_input = input("Select: ")
        if recon_input == "1":
            searchsploit.main()
        elif recon_input == "2":
            sniper.main()

def scanning_menu():
    scanning_input = ""
    while scanning_input != "99":
        os.system("clear")
        print("""
                               Scanning Menu

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Port Scan (Nmap)                  2. Web/Vuln Scan (Sn1per)
    
    3. Wordpress Scanner (Wpscan)        4. Joomla scanner(JoomScan) 

    5. Nikto                             6. Host Discovery (Nmap)

   99. Exit
    """)
        scanning_input = input("Select: ")
        if scanning_input == "1":
            nmap.main()
        elif scanning_input == "2":
            sniper_scan.main()
        elif scanning_input == "3":
            wpscan.main()
        elif scanning_input == "4":
            joomla.main()
        elif scanning_input == "5":
            nikto.main()
        elif scanning_input == "6":
            host_nmap.main()

if __name__ == '__main__':  

    if (RoE() == "1"):
        #package_status = PackageCheck.self_check()
        selection = 0
        while(selection != 10):
            selection = 0       #initialize selection so it wont inherit from other module
            os.system('clear')
            banner()
            main_menu()
            try:
                selection = int(input("Selection: "))
            except ValueError:
                pass

            if selection == 1:
                PackageInstall.main()
            elif selection == 2:
                PackageUpdate.main()
            elif selection == 3:
                PackageUninstall.main()
            elif selection == 4:
                tor.main()
            elif selection == 5:
                recon_menu()
            elif selection == 6:
                scanning_menu()
        if tor.check_init() == 1:
            os.system("sudo service tor stop")
            
        print("Exiting...")
        exit()
    else:
        print("Exiting.............")
        exit()