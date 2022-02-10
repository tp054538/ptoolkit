import os
import PackageCheck

def packagestatus_check(package_status):
    global nmap_status, sqlmap_status, tor_status, searchsploit_status, joomscan_status, set_status, nikto_status, wpscan_status
    global gobuster_status, hydra_status, john_status, ettercap_status, msfvenom_status
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

def printMenu():
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

    os.system('clear')
    print("""
                                Install Packages

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
    print("\033[0;37m"+"\n*Red colour   = Not Installed Packages")
    print("*Green colour = Installed Packages")
    print("\n")

def prRed(printinput):   print("\033[91m{}\033[00m".format(printinput))
def installpackages(select):
    selection = str(select)
    dictionary = {"1" : "nmap", "2" : "sqlmap", "3" : "tor", "4" : "exploitdb", "5" : "wpscan", "6" : "joomscan", "7" : "nikto", "8": "gobuster", "9" : "hydra",
    "10" : "john", "11" : "ettercap-common", "12" : "set" , "13" : "metasploit-framework"}
    prRed("\n[+]Start installing "+dictionary[selection])
    os.system("sudo apt install "+dictionary[selection])


def main():
    select = 0
    while select != 99:
        status = PackageCheck.self_check()
        packagestatus_check(status)
        printMenu()
        try:
            select = int(input("Selection: "))
        except ValueError:
            pass
        if select >= 1 and select <= 13:
            installpackages(select)
        elif select == 100:
            os.system('sudo apt update')
        else:
            print("\nPlease enter a valid operation!")
            useless = input("Enter any key to continue......")
            break