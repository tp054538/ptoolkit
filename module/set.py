#Written By: Foong Yew Joe (TP054538)
#Description: Launch SET
#First Written Date: 10 March 2022
#Last Edited: 18 April 2022

import os
import subprocess

def set_self_check():
    set_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^set/'", shell=True, stdout=subprocess.PIPE)
    set_checkstatusd = set_checkstatus.stdout.decode('ascii')
    if "installed" in set_checkstatusd or "upgradable" in set_checkstatusd:
        return 1
    else:
        return 0

def set_main():
    os.system("sudo setoolkit")

def main():
    print("\033[1;32m[+] Loading SEToolkit Module\033[00m")
    if set_self_check() == 1:
        set_main()
    else:
        print("\n\033[1;31m[-] SEToolkit is not installed!\033[00m")
        useless = input("Enter any key to continue......")