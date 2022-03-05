import os
import subprocess

def john_self_check():
    john_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^john/'", shell=True, stdout=subprocess.PIPE)
    john_checkstatusd = john_checkstatus.stdout.decode('ascii')
    if "installed" in john_checkstatusd or "upgradable" in john_checkstatusd:
        return 1
    else:
        return 0

def john_banner():
    os.system("clear")
    print("""
                        Password Cracker (JohnTheRipper)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. File :   

    2. Encoding
    3. Hash Format
    4. 

Command:

   90. Launch Attack
   99. Exit
""")

def john_main():

    john_select = ""
    while john_select != "99":
        john_banner()
        john_select = input("\nSelect: ").strip()


def main():
    print("\033[1;32m[+] Loading JohnTheRipper Module\033[00m")
    if john_self_check() == 1:
        john_main()
    else:
        print("\n\033[1;31m[-] JohnTheRipper is not installed!\033[00m")
        useless = input("Enter any key to continue......")
    