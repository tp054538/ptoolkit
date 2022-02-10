import PackageInstall
import PackageCheck
import os



def update_menu():
    green = "\033[1;32m" #green for installed
    red = "\033[1;31m"   #red for not installed
    white = "\033[1;37m"
    purple = "\033[1;35m"
    yellow = "\033[1;33m"

    PackageInstall.packagestatus_check(PackageCheck.self_check()) #self check everytime to get latest package status up to date in loop

    if PackageInstall.nmap_status == yellow:       
        nmap_local_status = green
    elif PackageInstall.nmap_status == red or PackageInstall.nmap_status == green:
        nmap_local_status = red

    if PackageInstall.sqlmap_status == yellow:
        sqlmap_local_status = green
    elif PackageInstall.sqlmap_status == red or PackageInstall.sqlmap_status == green:
        sqlmap_local_status = red

    if PackageInstall.tor_status == yellow:
        tor_local_status = green
    elif PackageInstall.tor_status == red or PackageInstall.tor_status == green:
        tor_local_status = red

    if PackageInstall.searchsploit_status == yellow:
        searchsploit_local_status = green
    elif PackageInstall.searchsploit_status == red or PackageInstall.searchsploit_status == green:
        searchsploit_local_status = red

    if PackageInstall.wpscan_status == yellow:
        wpscan_local_status = green
    elif PackageInstall.wpscan_status == red or PackageInstall.wpscan_status == green:
        wpscan_local_status = red
    
    if PackageInstall.joomscan_status == yellow:
        joomscan_local_status = green
    elif PackageInstall.joomscan_status == red or PackageInstall.joomscan_status == green:
        joomscan_local_status = red

    if PackageInstall.nikto_status == yellow:
        nikto_local_status = green
    elif PackageInstall.nikto_status == red or PackageInstall.nikto_status == green:
        nikto_local_status = red

    if PackageInstall.gobuster_status == yellow:
        gobuster_local_status = green
    elif PackageInstall.gobuster_status == red or PackageInstall.gobuster_status == green:
        gobuster_local_status = red

    if PackageInstall.hydra_status == yellow:
        hydra_local_status = green
    elif PackageInstall.hydra_status == red or PackageInstall.hydra_status == green:
        hydra_local_status = red
    
    if PackageInstall.john_status == yellow:
        john_local_status = green
    elif PackageInstall.john_status == red or PackageInstall.john_status == green:
        john_local_status = red

    if PackageInstall.ettercap_status == yellow:
        ettercap_local_status = green
    elif PackageInstall.ettercap_status == red or PackageInstall.ettercap_status == green:
        ettercap_local_status = red
    
    if PackageInstall.set_status == yellow:
        set_local_status = green
    elif PackageInstall.set_status == red or PackageInstall.set_status == green:
        set_local_status = red

    if PackageInstall.msfvenom_status == yellow:
        msfvenom_local_status = green
    elif PackageInstall.msfvenom_status == red or PackageInstall.msfvenom_status == green:
        msfvenom_local_status = red

    os.system('clear')
    print("""
                                Update Packages

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    """+white+" 1. "+ nmap_local_status +"Nmap"+white+"       2. "+sqlmap_local_status+"SQLmap"+white+"      3. "+tor_local_status+"Tor"+white+"        4. "+searchsploit_local_status+"Searchsploit"+white+"   5. "+wpscan_local_status+"WPscan")
    print("\n")
    print(white+"     6. "+joomscan_local_status+"JoomScan"+white+"   7. "+nikto_local_status+"Nikto"+white+"       8. "+gobuster_local_status+"GoBuster"+white+"   9. "+hydra_local_status+"Hydra"+white+"         10. "+john_local_status+"John")
    print("\n")
    print(white+"    11. "+ettercap_local_status+"Ettercap"+white+"  12. "+set_local_status+"SEToolkit"+white+"  13. "+msfvenom_local_status+"MSFvenom")
    print("\n")
    print(white+"    99. "+purple+"Back to Main Menu"+white+"      100. "+purple+"Update APT packages' information")
    print("\n")
    print(white+"   111. "+purple+"Batch Update Packages")
    print("\033[0;37m"+"\n*Red colour   = Not Installed / Not Upgradeable Packages")
    print("*Green colour = Upgradeable Packages")
    print("\n")

def main():
    select = 0
    while select != 99:
        update_menu()
        try:
            select = int(input("Selection: "))
        except ValueError:
            pass
        if select >= 1 and select <= 13:
            PackageInstall.installpackages(select)

        elif select == 100:
            os.system('sudo apt update')
        else:
            print("\nPlease enter a valid operation!")
            useless = input("Enter any key to continue......")
            break