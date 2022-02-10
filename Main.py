import os
import PackageCheck
import PackageInstall
import PackageUpdate

def prRed(printinput):
    print("\033[91m{}\033[00m".format(printinput))
def prYellow(printinput):
    print("\033[93m{}\033[00m".format(printinput))

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
    prYellow("Version: 1.0")

def main_menu():
    print("""
                                    Main Menu

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Install Tools            6. Reconnaissance               10. Exit

    2. Update Tools             7. Scanning

    3. Uninstall Tools          8. Exploitation

    4. Tor Proxy                9. Maintaining Access
    """)

if __name__ == '__main__':  
    if (RoE() == "1"):
        #package_status = PackageCheck.self_check()
        selection = 0
        while(selection != 10):
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
            
        print("Exiting...")
        exit()
    else:
        print("Exiting.............")
        exit()