import os
import subprocess

def sniper_banner():
    os.system("clear")
    print("""
                            OSINT / Recon (Sn1per))

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1.     
    2.
    3.
    4.        

   99. Exit
    """)

def sniper_self_check():
    print("\033[1;32m[+] Loading Sn1per Module.\033[00m")
    sniper_statuscheck = subprocess.run("ls | grep Sn1per", shell=True, stdout=subprocess.PIPE)
    sniper_statuscheckd = sniper_statuscheck.stdout.decode('ascii')
    if "Sn1per" in sniper_statuscheckd:
        return 1
    else:
        return 0

def main():
    if sniper_self_check() == 1:
        sniper_select = ""
        while sniper_select != "99":
            sniper_banner()
            sniper_select = input("\nSelect: ")
    else:
        print("\n\033[1;31m[-] Sn1per is not installed!\033[00m")
        useless = input("Enter any key to continue......")
