import os
import subprocess

def ettercap_self_check():
    ettercap_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^ettercap-common/'", shell=True, stdout=subprocess.PIPE)
    ettercap_checkstatusd = ettercap_checkstatus.stdout.decode('ascii')
    if "installed" in ettercap_checkstatusd or "upgradable" in ettercap_checkstatusd:
        return 1
    else:
        return 0

def ettercap_main():
    os.system("sudo ettercap -G")

def main():
    print("\033[1;32m[+] Loading Ettercap Module\033[00m")
    if ettercap_self_check() == 1:
        ettercap_main()
    else:
        print("\n\033[1;31m[-] Ettercap is not installed!\033[00m")
        useless = input("Enter any key to continue......")