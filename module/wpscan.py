import os
import subprocess

def wpscan_self_check():
    print("\033[1;32m[+] Loading WpScan Module.\033[00m")
    wpscan_status_check = subprocess.run("apt list 2>/dev/null | grep -E '^wpscan/'", shell=True, stdout=subprocess.PIPE)
    wpscan_status_checkd = wpscan_status_check.stdout.decode('ascii')
    if "installed" in wpscan_status_checkd or "upgradable" in wpscan_status_checkd:
        return 1
    else:
        return 0

def wpscan_banner():
    os.system("clear")
    print("""
                          Wordpress Scanner (WPscan)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. URL: """+wpscan_url_target+"""

   99. Exit
    """)

def main():
    if wpscan_self_check() == 1:
        global wpscan_url_target
        wpscan_url_target = ""
        wpscan_select = ""
        #wpscan program loop
        while wpscan_select != "99":
            wpscan_banner()
            wpscan_select = input("\nSelect: ")
    else:
        print("\n\033[1;31m[-] WpScan is not installed!\033[00m")
        useless = input("Enter any key to continue......")
