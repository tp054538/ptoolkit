import os
import PackageCheck
import multiprocessing

def packagestatus_check(package_status):
    global nmap_status, sqlmap_status, tor_status, searchsploit_status, joomscan_status, set_status, nikto_status, wpscan_status
    global gobuster_status, hydra_status, john_status, ettercap_status, msfvenom_status, slowloris_status, sniper_status, git_status
    green = "\033[1;32m" #green for installed
    red = "\033[1;31m"   #red for not installed
    yellow = "\033[1;33m" #yellow for upgradeable

    #nmap
    if 'Nmap Not Installed' in package_status:
        nmap_status = red
    elif 'Nmap Installed' in package_status:
        nmap_status = green
    elif 'Nmap Upgradeable' in package_status:
        nmap_status = yellow

    #sqlmap
    if 'SQLmap Not Installed' in package_status:
        sqlmap_status = red
    elif 'SQLmap Installed' in package_status:
        sqlmap_status = green
    elif 'SQLmap Upgradeable' in package_status:
        sqlmap_status = yellow
    
    #tor
    if 'Tor Not Installed' in package_status:
        tor_status = red
    elif 'Tor Installed' in package_status:
        tor_status = green
    elif 'Tor Upgradeable' in package_status:
        tor_status = yellow
    
    #searchsploit
    if 'SearchSploit Not Installed' in package_status:
        searchsploit_status = red
    elif 'SearchSploit Installed' in package_status:
        searchsploit_status = green
    elif 'SearchSploit Upgradeable' in package_status:
        searchsploit_status = yellow
    
    #joomscan
    if 'JoomScan Not Installed' in package_status:
        joomscan_status = red
    elif 'JoomScan Installed' in package_status:
        joomscan_status = green
    elif 'JoomScan Upgradeable' in package_status:
        joomscan_status = yellow

    #setoolkit
    if 'SEToolkit Not Installed' in package_status:
        set_status = red
    elif 'SEToolkit Installed' in package_status:
        set_status = green
    elif 'SEToolkit Upgradeable' in package_status:
        set_status = yellow
    
    #wpscan
    if 'WPscan Not Installed' in package_status:
        wpscan_status = red
    elif 'WPscan Installed' in package_status:
        wpscan_status = green
    elif 'WPscan Upgradeable' in package_status:
        wpscan_status = yellow 
    
    #nikto
    if 'Nikto Not Installed' in package_status:
        nikto_status = red
    elif 'Nikto Installed' in package_status:
        nikto_status = green
    elif 'Nikto Upgradeable' in package_status:
        nikto_status = yellow 
    
    #gobuster
    if 'GoBuster Not Installed' in package_status:
        gobuster_status = red
    elif 'GoBuster Installed' in package_status:
        gobuster_status = green
    elif 'GoBuster Upgradeable' in package_status:
        gobuster_status = yellow 
    
    #hydra
    if 'Hydra Not Installed' in package_status:
        hydra_status = red
    elif 'Hydra Installed' in package_status:
        hydra_status = green
    elif 'Hydra Upgradeable' in package_status:
        hydra_status = yellow 
    
    #john
    if 'JohnTheRipper Not Installed' in package_status:
        john_status = red
    elif 'JohnTheRipper Installed' in package_status:
        john_status = green
    elif 'JohnTheRipper Upgradeable' in package_status:
        john_status = yellow 

    #ettercap
    if 'Ettercap Not Installed' in package_status:
        ettercap_status = red
    elif 'Ettercap Installed' in package_status:
        ettercap_status = green
    elif 'Ettercap Upgradeable' in package_status:
        ettercap_status = yellow 

    #msfvenom
    if 'Metasploit Not Installed' in package_status:
        msfvenom_status = red
    elif 'Metasploit Installed' in package_status:
        msfvenom_status = green
    elif 'Metasploit Upgradeable' in package_status:
        msfvenom_status = yellow 
    
    #slowloris
    if 'Slowloris Not Installed' in package_status:
        slowloris_status = red
    elif 'Slowloris Installed' in package_status:
        slowloris_status = green
    
    #sn1per
    if 'Sn1per Installed' in package_status:
        sniper_status = green
    elif 'Sn1per Not Installed' in package_status:
        sniper_status = red
    
    #git
    if 'Git Not Installed' in package_status:
        git_status = red
    elif 'Git Installed' in package_status:
        git_status = green
    elif 'Git Upgradeable' in package_status:
        git_status = yellow 

def printMenu():
    global green, red
    green = "\033[1;32m" #green for installed
    red = "\033[1;31m"   #red for not installed
    white = "\033[1;37m"
    purple = "\033[1;35m"
    yellow = "\033[1;33m"

    if nmap_status == yellow or nmap_status == green:       #to display green only instead of upgradeable yellow in install page
        nmap_local_status = green
    elif nmap_status == red:
        nmap_local_status = red

    if sqlmap_status == yellow or sqlmap_status == green:
        sqlmap_local_status = green
    elif sqlmap_status == red:
        sqlmap_local_status = red

    if tor_status == yellow or tor_status == green:
        tor_local_status = green
    elif tor_status == red:
        tor_local_status = red

    if searchsploit_status == yellow or searchsploit_status == green:
        searchsploit_local_status = green
    elif searchsploit_status == red:
        searchsploit_local_status = red

    if wpscan_status == yellow or wpscan_status == green:
        wpscan_local_status = green
    elif wpscan_status == red:
        wpscan_local_status = red
    
    if joomscan_status == yellow or joomscan_status == green:
        joomscan_local_status = green
    elif joomscan_status == red:
        joomscan_local_status = red

    if nikto_status == yellow or nikto_status == green:
        nikto_local_status = green
    elif nikto_status == red:
        nikto_local_status = red

    if gobuster_status == yellow or gobuster_status == green:
        gobuster_local_status = green
    elif gobuster_status == red:
        gobuster_local_status = red

    if hydra_status == yellow or hydra_status == green:
        hydra_local_status = green
    elif hydra_status == red:
        hydra_local_status = red
    
    if john_status == yellow or john_status == green:
        john_local_status = green
    elif john_status == red:
        john_local_status = red

    if ettercap_status == yellow or ettercap_status == green:
        ettercap_local_status = green
    elif ettercap_status == red:
        ettercap_local_status = red
    
    if set_status == yellow or set_status == green:
        set_local_status = green
    elif set_status == red:
        set_local_status = red

    if msfvenom_status == yellow or msfvenom_status == green:
        msfvenom_local_status = green
    elif msfvenom_status == red:
        msfvenom_local_status = red

    if slowloris_status == green:
        slowloris_local_status = green
    elif slowloris_status == red:
        slowloris_local_status = red

    if sniper_status == green:
        sniper_local_status = green
    elif sniper_status == red:
        sniper_local_status = red
    
    if git_status == yellow or git_status == green:
        git_local_status = green
    elif git_status == red:
        git_local_status = red


    os.system('clear')
    print("""
                                Install Packages

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    """+white+" 1. "+ nmap_local_status +"Nmap"+white+"       2. "+sqlmap_local_status+"SQLmap"+white+"      3. "+tor_local_status+"Tor"+white+"        4. "+searchsploit_local_status+"Searchsploit"+white+"   5. "+wpscan_local_status+"WPscan")
    print("\n")
    print(white+"     6. "+joomscan_local_status+"JoomScan"+white+"   7. "+nikto_local_status+"Nikto"+white+"       8. "+gobuster_local_status+"GoBuster"+white+"   9. "+hydra_local_status+"Hydra"+white+"         10. "+john_local_status+"John")
    print("\n")
    print(white+"    11. "+ettercap_local_status+"Ettercap"+white+"  12. "+set_local_status+"SEToolkit"+white+"  13. "+msfvenom_local_status+"MSFvenom"+white+"  14. "+slowloris_local_status+"Slowloris"+white+"     15. "+sniper_local_status+"Sn1per")
    print("\n")
    print(white+"    16. "+git_local_status+"Git"+white)
    print("\n")
    print(white+"    99. "+purple+"Back to Main Menu"+white+"        100. "+purple+"Update APT packages' information")
    print("\n")
    print(white+"   111. "+purple+"Batch Install Packages"+white)
    print("\033[0;37m"+"\n*Red colour   = Not Installed Packages")
    print("*Green colour = Installed Packages")
    print("\n")

    #install function
def prRed(printinput):   print("\033[91m{}\033[00m".format(printinput))
def prGreen(printinput): print("\033[92m{}\033[00m".format(printinput))
def installpackages(select):
    selection = str(select)
    dictionary = {"1" : "nmap", "2" : "sqlmap", "3" : "tor", "4" : "exploitdb", "5" : "wpscan", "6" : "joomscan", "7" : "nikto", "8": "gobuster", "9" : "hydra",
    "10" : "john", "11" : "ettercap-common", "12" : "set" , "13" : "metasploit-framework", "14" : "git clone https://github.com/gkbrk/slowloris.git", "15" : "git clone https://github.com/1N3/Sn1per", "16" : "git"}
    if select != 14 and select != 15:
        prRed("\n[+] Start installing "+dictionary[selection])
        os.system("sudo apt install "+dictionary[selection])
        useless = input("\n[+] Process Completed. Enter any key to continue......")
    else:
        if git_status == red:
            print("\n[*] Please install Git first before installing Sn1per.")
            input("Enter any key to continue......")
        else:
            if select == 14:
                prRed("[+] Start installing Slowloris")
            elif select == 15:
                prRed("[+] Start Installing Sn1per")
            os.system(dictionary[selection])
            if select == 15:
                os.system('cd Sn1per; echo "y" > y.txt; sudo ./install.sh < y.txt')
            useless = input("\n[+] Process Completed. Enter any key to continue......")

    #batch install function
def batch_install_packages(input_list):
    dictionary = {"1" : "nmap", "2" : "sqlmap", "3" : "tor", "4" : "exploitdb", "5" : "wpscan", "6" : "joomscan", "7" : "nikto", "8": "gobuster", "9" : "hydra",
    "10" : "john", "11" : "ettercap-common", "12" : "set" , "13" : "metasploit-framework", "14" : "git clone https://github.com/gkbrk/slowloris.git", "15" : "git clone https://github.com/1N3/Sn1per", "16" : "git"}

    if "14" in input_list or "15" in input_list:
        if "14" in input_list and "15" in input_list:
            if len(input_list) >= 3:
                command = "sudo apt install"
                for i in range(len(input_list)):
                    if input_list[i] != "14" and input_list[i] != "15":
                        command += " " + dictionary[input_list[i]]
                        prRed("[+] "+dictionary[input_list[i]]+" installation is starting......")
                command += " -y > /dev/null 2>&1"
                os.system(command)
            if git_status == red:
                print("\n[*] Please install Git first before installing Sn1per.")
                input("Enter any key to continue......")
            else:
                prRed("[+] Slowloris installation is starting......")
                prRed("[+] Sn1per installation is starting......")
                os.system(dictionary["14"])
                os.system(dictionary["15"])
                os.system('cd Sn1per; echo "y" > y.txt; sudo ./install.sh < y.txt')
                useless = input("\n[+] Process completed. Enter any key to continue......")

        elif "14" in input_list and "15" not in input_list:
            if len(input_list) >= 2:
                command = "sudo apt install"
                for i in range(len(input_list)):
                    if input_list[i] != "14":
                        command += " " + dictionary[input_list[i]]
                        prRed("[+] "+dictionary[input_list[i]]+" installation is starting......")
                command += " -y > /dev/null 2>&1"
                os.system(command)
            if git_status == red:
                print("\n[*] Please install Git first before installing Sn1per.")
                input("Enter any key to continue......")
            else:
                prRed("[+] Slowloris installation is starting......")
                os.system(dictionary["14"])
                useless = input("\n[+] Process completed. Enter any key to continue......")

        elif "14" not in input_list and "15" in input_list:
            if len(input_list) >= 2:
                command = "sudo apt install"
                for i in range(len(input_list)):
                    if input_list[i] != "15":
                        command += " " + dictionary[input_list[i]]
                        prRed("[+] "+dictionary[input_list[i]]+" installation is starting......")
                command += " -y > /dev/null 2>&1"
                os.system(command)
            if git_status == red:
                print("\n[*] Please install Git first before installing Sn1per.")
                input("Enter any key to continue......")
            else:
                prRed("[+] Sn1per installation is starting......")
                os.system(dictionary["15"])
                os.system('cd Sn1per; echo "y" > y.txt; sudo ./install.sh < y.txt')
                useless = input("\n[+] Process completed. Enter any key to continue......")

    else:
        command = "sudo apt install"
        for i in range(len(input_list)):
            command += " " + dictionary[input_list[i]]
        command += " -y > /dev/null 2>&1"

        for e in range(len(input_list)):
            prRed("[+] "+dictionary[input_list[e]]+" installation / update is starting......")

        os.system(command)
        useless = input("\n[+] Process Completed. Press any key to continue......")


def main():
    select = 0
    print("\033[1;32m\n[+] Loading Install Module\033[00m")
    while select != 99:
        select = 0      # initialize to not inherit
        status = PackageCheck.self_check()
        packagestatus_check(status)
        printMenu()
        try:
            select = int(input("Selection: "))
        except ValueError:
            pass
        
        #selection
        if select >= 1 and select <= 16: 
            if select == 14:
                if slowloris_status == green:
                    prRed("[+] Slowloris is already installed. Installation process will not be executed.")
                    useless = input("Enter any key to continue......")  
                    continue
            if select == 15:
                if sniper_status == green:
                    prRed("[+] Sn1per is already installed. Installation process will not be executed.")
                    useless = input("Enter any key to continue......")        
                    continue              
            installpackages(select)

        elif select == 100:         #apt update selection
            os.system('sudo apt update')

        elif select == 111:         #batch install selection
            batch_list = []
            print("Please enter the packages number to be installed with a space between different number \nEg. 1 2 3 10 7\n")
            batch = input("Batch install selection: ")
            batch_list = batch.strip().split() #strip() remove space infront and behind

            if batch_list:
                try:
                    for i in range(len(batch_list)):    #check list is between the valid numbers or not
                        if int(batch_list[i]) >= 1 and int(batch_list[i]) <= 13:
                            pass
                        elif int(batch_list[i]) == 14:
                            if slowloris_status == green:
                                prRed("[+] Slowloris is already installed! Installation process will not be executed.")
                                raise KeyError
                        elif int(batch_list[i]) == 15:
                            if sniper_status == green:
                                prRed("[+] Sn1per is already installed! Installation process will not be executed.") 
                                raise KeyError
                        elif int(batch_list[i]) == 16:
                            pass
                        else:
                            print("\nInput contains invalid value, please check again! (Valid input example: 1 2 5 10 7)")
                            raise AssertionError
                    batch_install_packages(batch_list)
                except ValueError:
                    print("\nPlease enter numbers only!")
                    useless = input("Enter any key to continue......")
                    continue
                except AssertionError:
                    print("\nPlease enter numbers between 1 - 16 only")
                    useless = input("Enter any key to continue......")
                    continue
                except KeyError:
                    useless = input("Enter any key to continue......")
                    continue
                
            else:
                print("\nInvalid operation! Input is empty.")
                useless = input("Enter any key to continue......")
                continue

        elif select == 99:
            pass

        else:
            print("Invalid input!")
            useless = input("Enter any key to continue......")
