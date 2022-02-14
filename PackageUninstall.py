import subprocess
from sys import stdout
import PackageInstall
import PackageCheck
import os

def CheckValid(a):
    green = "\033[1;32m" 
    red = "\033[1;31m"   
    yellow = "\033[1;33m"
    flag = 0

    if type(a) is list:
        for i in range(len(a)):
            if a[i] == '1':
                if PackageInstall.nmap_status == red:
                    flag = 1
                    break
            elif a[i] == '2':
                if PackageInstall.sqlmap_status == red:
                    flag = 1
                    break
            elif a[i] == '3':
                if PackageInstall.tor_status == red:
                    flag = 1
                    break
            elif a[i] == '4':
                if PackageInstall.searchsploit_status == red:
                    flag = 1
                    break
            elif a[i] == '5':
                if PackageInstall.wpscan_status == red:
                    flag = 1
                    break
            elif a[i] == '6':
                if PackageInstall.joomscan_status == red:
                    flag = 1
                    break
            elif a[i] == '7':
                if PackageInstall.nikto_status == red:
                    flag = 1
                    break
            elif a[i] == '8':
                if PackageInstall.gobuster_status == red:
                    flag = 1
                    break
            elif a[i] == '9':
                if PackageInstall.hydra_status == red:
                    flag = 1
                    break
            elif a[i] == '10':
                if PackageInstall.john_status == red:
                    flag = 1
                    break
            elif a[i] == '11':
                if PackageInstall.ettercap_status == red:
                    flag = 1
                    break
            elif a[i] == '12':
                if PackageInstall.set_status == red:
                    flag = 1
                    break
            elif a[i] == '13':
                if PackageInstall.msfvenom_status == red:
                    flag = 1
                    break
            elif a[i] == '14':
                if PackageInstall.slowloris_status == red:
                    flag = 1
                    break
            elif a[i] == '15':
                if PackageInstall.sniper_status == red:
                    flag = 1
                    break
    else:
        if a == 1:
            if PackageInstall.nmap_status == red:
                flag = 1
        elif a == 2:
            if PackageInstall.sqlmap_status == red:
                flag = 1
        elif a == 3:
            if PackageInstall.tor_status == red:
                flag = 1
        elif a == 4:
            if PackageInstall.searchsploit_status == red:
                flag = 1
        elif a == 5:
            if PackageInstall.wpscan_status == red:
                flag = 1
        elif a == 6:
            if PackageInstall.joomscan_status == red:
                flag = 1
        elif a == 7:
            if PackageInstall.nikto_status == red:
                flag = 1
        elif a == 8:
            if PackageInstall.gobuster_status == red:
                flag = 1
        elif a == 9:
            if PackageInstall.hydra_status == red:
                flag = 1
        elif a == 10:
            if PackageInstall.john_status == red:
                flag = 1
        elif a == 11:
            if PackageInstall.ettercap_status == red:
                flag = 1
        elif a == 12:
            if PackageInstall.set_status == red:
                flag = 1
        elif a == 13:
            if PackageInstall.msfvenom_status == red:
                flag = 1
        elif a == 14:
            if PackageInstall.slowloris_status == red:
                flag = 1
        elif a == 15:
            if PackageInstall.sniper_status == red:
                flag = 1

    return flag

def MenuPrint():
    green = "\033[1;32m" #green for installed
    red = "\033[1;31m"   #red for not installed
    white = "\033[1;37m"
    purple = "\033[1;35m"
    yellow = "\033[1;33m"

    prGreen("\n[+] Loading Uninstall Module")
    PackageInstall.packagestatus_check(PackageCheck.self_check()) #self check everytime to get latest package status up to date in loop

    if PackageInstall.nmap_status == yellow or PackageInstall.nmap_status == green:       
        nmap_local_status = green
    elif PackageInstall.nmap_status == red:
        nmap_local_status = red

    if PackageInstall.sqlmap_status == yellow or PackageInstall.sqlmap_status == green:
        sqlmap_local_status = green
    elif PackageInstall.sqlmap_status == red:
        sqlmap_local_status = red

    if PackageInstall.tor_status == yellow or PackageInstall.tor_status == green:
        tor_local_status = green
    elif PackageInstall.tor_status == red:
        tor_local_status = red

    if PackageInstall.searchsploit_status == yellow or PackageInstall.searchsploit_status == green:
        searchsploit_local_status = green
    elif PackageInstall.searchsploit_status == red:
        searchsploit_local_status = red

    if PackageInstall.wpscan_status == yellow or PackageInstall.wpscan_status == green:
        wpscan_local_status = green
    elif PackageInstall.wpscan_status == red:
        wpscan_local_status = red
    
    if PackageInstall.joomscan_status == yellow or PackageInstall.joomscan_status == green:
        joomscan_local_status = green
    elif PackageInstall.joomscan_status == red:
        joomscan_local_status = red

    if PackageInstall.nikto_status == yellow or PackageInstall.nikto_status == green:
        nikto_local_status = green
    elif PackageInstall.nikto_status == red:
        nikto_local_status = red

    if PackageInstall.gobuster_status == yellow or PackageInstall.gobuster_status == green:
        gobuster_local_status = green
    elif PackageInstall.gobuster_status == red:
        gobuster_local_status = red

    if PackageInstall.hydra_status == yellow or PackageInstall.hydra_status == green:
        hydra_local_status = green
    elif PackageInstall.hydra_status == red:
        hydra_local_status = red
    
    if PackageInstall.john_status == yellow or PackageInstall.john_status == green:
        john_local_status = green
    elif PackageInstall.john_status == red:
        john_local_status = red

    if PackageInstall.ettercap_status == yellow or PackageInstall.ettercap_status == green:
        ettercap_local_status = green
    elif PackageInstall.ettercap_status == red:
        ettercap_local_status = red
    
    if PackageInstall.set_status == yellow or PackageInstall.set_status == green:
        set_local_status = green
    elif PackageInstall.set_status == red:
        set_local_status = red

    if PackageInstall.msfvenom_status == yellow or PackageInstall.msfvenom_status == green:
        msfvenom_local_status = green
    elif PackageInstall.msfvenom_status == red:
        msfvenom_local_status = red
    
    if PackageInstall.slowloris_status == green:
        slowloris_local_status = green
    elif PackageInstall.slowloris_status == red:
        slowloris_local_status = red
    
    if PackageInstall.sniper_status == green:
        sniper_local_status = green
    elif PackageInstall.sniper_status == red:
        sniper_local_status = red

    os.system('clear')
    print("""
                                Uninstall Packages

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    """+white+" 1. "+ nmap_local_status +"Nmap"+white+"       2. "+sqlmap_local_status+"SQLmap"+white+"      3. "+tor_local_status+"Tor"+white+"        4. "+searchsploit_local_status+"Searchsploit"+white+"   5. "+wpscan_local_status+"WPscan")
    print("\n")
    print(white+"     6. "+joomscan_local_status+"JoomScan"+white+"   7. "+nikto_local_status+"Nikto"+white+"       8. "+gobuster_local_status+"GoBuster"+white+"   9. "+hydra_local_status+"Hydra"+white+"         10. "+john_local_status+"John")
    print("\n")
    print(white+"    11. "+ettercap_local_status+"Ettercap"+white+"  12. "+set_local_status+"SEToolkit"+white+"  13. "+msfvenom_local_status+"MSFvenom"+white+"  14. "+slowloris_local_status+"Slowloris"+white+"     15. "+sniper_local_status+"Sn1per")
    print("\n")
    print(white+"    99. "+purple+"Back to Main Menu"+white+"       111. "+purple+"Batch Uninstall Packages")
    print("\033[0;37m"+"\n*Red colour   = Not Installed Packages")
    print("*Green colour = Installed Packages")
    print("\n")

def prRed(printinput):   print("\033[91m{}\033[00m".format(printinput))
def prGreen(printinput): print("\033[92m{}\033[00m".format(printinput))

def UninstallPackage(uninstall_input):
    selection = str(uninstall_input)
    dictionary = {"1" : "nmap", "2" : "sqlmap", "3" : "tor", "4" : "exploitdb", "5" : "wpscan", "6" : "joomscan", "7" : "nikto", "8": "gobuster", "9" : "hydra",
    "10" : "john", "11" : "ettercap-common", "12" : "set" , "13" : "metasploit-framework", "14" : "slowloris", "15" : "Sn1per"}

    if CheckValid(uninstall_input) == 0:
        if selection != '14' and selection != '15':
            prRed("\n[+]Start Uninstalling "+dictionary[selection])
            os.system("sudo apt remove "+dictionary[selection])
            useless = input("\nProcess Completed. Enter any key to continue......")
        elif selection == '14':
            prRed("\n[+] Start removing slowloris.")
            os.system("rm -R slowloris -f")
            useless = input("\nSlowloris removed. Enter any key to continue......")
        elif selection == '15':
            prRed("\n[+] Start removing Sn1per.")
            os.system('cd Sn1per; echo "y" > y.txt ; sudo ./uninstall.sh < y.txt') #pass "y" to uninstall prompt
            os.system("rm -R Sn1per -f")
            useless = input("\nSn1per removed. Enter any key to continue......")           
        
    else:
        if selection == '14':
            prRed("\n[+] Slowloris is not installed. Operation Aborted.")
            useless = input("Enter any key to continue......")
        elif selection == '15':
            prRed("\n[+] Sn1per is not installed. Operation Aborted.")
            useless = input("Enter any key to continue.......")
        else:
            prRed("\n[+] "+dictionary[selection]+" is not installed. Operation Aborted.")
            useless = input("Enter any key to continue......")


def BatchUninstallPackage(uninstall_input): 
    dictionary = {"1" : "nmap", "2" : "sqlmap", "3" : "tor", "4" : "exploitdb", "5" : "wpscan", "6" : "joomscan", "7" : "nikto", "8": "gobuster", "9" : "hydra",
    "10" : "john", "11" : "ettercap-common ettercap-graphical", "12" : "set" , "13" : "metasploit-framework"}

    if CheckValid(uninstall_input) == 1:
        print("\n[+] PToolkit cannot uninstall packages that are not installed on this machine!")
        useless = input("Enter any key to continue......")
    else:
        if "14" in uninstall_input or "15" in uninstall_input:
            if "14" in uninstall_input and "15" in uninstall_input:
                if len(uninstall_input) >= 3:
                    command = "sudo apt remove"
                    for i in range(len(uninstall_input)):
                        if uninstall_input[i] != "14" and uninstall_input[i] != "15":
                            command += " " + dictionary[uninstall_input[i]]
                            prRed("[+] "+dictionary[uninstall_input[i]]+" uninstallation is starting......")
                    command += " -y > /dev/null"
                    os.system(command)
                prRed("[+] Slowloris uninstallation is starting......")
                prRed("[+] Sn1per uninstallation is starting......")
                os.system('cd Sn1per; echo "y" > y.txt ; sudo ./uninstall.sh < y.txt')
                os.system("rm -R slowloris -f")
                os.system("rm -R Sn1per -f")
                useless = input("\n[+] Process Completed. Enter any key to continue......")

            elif "14" in uninstall_input and "15" not in uninstall_input:
                if len(uninstall_input) >= 2:
                    command = "sudo apt remove"
                    for i in range(len(uninstall_input)):
                        if uninstall_input[i] != "14":
                            command += " " + dictionary[uninstall_input[i]]
                            prRed("[+] "+dictionary[uninstall_input[i]]+" uninstallation is starting......")
                    command += " -y > /dev/null 2>&1"
                    os.system(command)
                prRed("[+] Slowloris uninstallation is starting......")
                os.system("rm -R slowloris -f")
                useless = input("\n[+] Process completed. Enter any key to continue......")
            
            elif "14" not in uninstall_input and "15" in uninstall_input:
                if len(uninstall_input) >= 2:
                    command = "sudo apt remove"
                    for i in range(len(uninstall_input)):
                        if uninstall_input[i] != "15":
                            command += " " + dictionary[uninstall_input[i]]
                            prRed("[+] "+dictionary[uninstall_input[i]]+" uninstallation is starting......")
                    command += " -y > /dev/null 2>&1"
                    os.system(command)
                prRed("[+] Sn1per uninstallation is starting......")
                os.system('cd Sn1per; echo "y" > y.txt ; sudo ./uninstall.sh < y.txt')
                os.system("rm -R Sn1per -f")
                useless = input("\n[+] Process completed. Enter any key to continue......")

        else:
            command = "sudo apt remove"
            for i in range(len(uninstall_input)):
                command += " " + dictionary[uninstall_input[i]]
            command += " -y > /dev/null"

            for j in range(len(uninstall_input)):
                prRed("[+] "+dictionary[uninstall_input[j]]+" uninstallation is starting......")
            os.system(command)
            useless = input("\n[+]Process completed. Enter any key to continue......")


def main():
    select = 0
    while select != 99:
        MenuPrint()
        select = 0
        try:
            select = int(input("Selection: "))
        except ValueError:
            pass

        if select >= 1 and select <= 15:
            if select == 11:
                prRed("\n[*] Caution! Ettercap is one of the dependencies of SET, removing Ettercap will cause SET to be not usable.")
                s = input("Do you wish to continue the operation? (y/n)")
                if s == "y" or s == "Y":
                    UninstallPackage(select)
                else:
                    continue
            UninstallPackage(select)

        elif select == 100:
            os.system('sudo apt update')
        
        elif select == 111:         #batch install selection
            batch_list = []
            print("Please enter the packages number to be uninstalled with a space between different number \nEg. 1 2 3 10 7\n")
            batch = input("Batch uninstall selection: ")
            batch_list = batch.strip().split() #strip() remove space infront and behind

            if batch_list:
                try:
                    for i in range(len(batch_list)):    #check list is between the valid numbers or not
                        if int(batch_list[i]) >= 1 and int(batch_list[i]) <= 15:
                            if int(batch_list[i]) == 11:
                                prRed("\n[*] Caution! Ettercap is one of the dependencies of SET, removing Ettercap will cause SET to be not usable.")
                                s = input("Do you wish to continue the operation? (y/n)")
                                if s == "y" or s == "Y":
                                    pass
                                else:
                                    raise KeyError
                            pass
                        else:
                            print("\nInput contains invalid value, please check again! (Valid input example: 1 2 5 10 7)")
                            raise AssertionError
                    BatchUninstallPackage(batch_list)
                except ValueError:
                    print("\nPlease enter numbers only!")
                    useless = input("Enter any key to continue......")
                    continue
                except AssertionError:
                    print("\nPlease enter numbers between 1 - 15 only")
                    useless = input("Enter any key to continue......")
                    continue
                except KeyError:
                    continue
                
            else:
                print("\nInvalid operation! Input is empty.")
                useless = input("Enter any key to continue......")
                continue

        elif select == 99:
            pass

        else:
            print("\nPlease enter a valid operation!")
            useless = input("Enter any key to continue......")