import os 
import subprocess

from PackageCheck import prGreen, prRed

def main_menu():
    print("""
                                      Tor

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. 2            6. Reconnaissance               99. Exit

    2. Update Tools             7. Scanning

    3. Uninstall Tools          8. Exploitation

    4. Tor Proxy                9. Maintaining Access
    """)

def main():
    prGreen("[+] Loading Tor Module")
    tor_1 = subprocess.run("apt list 2>/dev/null | grep -E '^tor/'", shell=True, stdout=subprocess.PIPE)
    tor_2 = tor_1.stdout.decode('ascii')
    if "installed" in tor_2:
        select = 0
        while select != 99:
            select = 0
            os.system("clear")
            main_menu()
            select = input("s:")
            select = int(select)
    else:
        prRed("\n[+] Tor is not installed! Please install Tor before accessing this page.")
        useless = input("Enter any Key to continue......")