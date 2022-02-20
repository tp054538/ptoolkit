import os
import subprocess

def sniper_banner():
    if normal_flag == 1:
        normal_color = "\033[1;32m"
        normal_o_r_color = "\033[00m"
        stealth_o_r_color = "\033[00m"
    elif normal_o_r_flag == 1:
        normal_color = "\033[00m"
        normal_o_r_color = "\033[1;32m"
        stealth_o_r_color = "\033[00m"
    elif stealth_o_r_flag == 1:
        normal_color = "\033[00m"
        normal_o_r_color = "\033[00m"
        stealth_o_r_color = "\033[1;32m"
    else:
        normal_color = "\033[00m"
        normal_o_r_color = "\033[00m"
        stealth_o_r_color = "\033[00m"

    os.system("clear")
    print("""
                            OSINT / Recon (Sn1per))

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target: \033[1;32m"""+target+"""\033[00m

    2. """+normal_color+"""Normal Mode\033[00m  
    3. """+normal_o_r_color+"""Normal MOde + OSINT + Recon\033[00m
    4. """+stealth_o_r_color+"""Stealth Mode + OSINT + Recon\033[00m

    5. Launch Attack

   99. Exit
    """)

#check sniper is installed
def sniper_self_check():
    print("\033[1;32m[+] Loading Sn1per Module.\033[00m")
    sniper_statuscheck = subprocess.run("ls | grep Sn1per", shell=True, stdout=subprocess.PIPE)
    sniper_statuscheckd = sniper_statuscheck.stdout.decode('ascii')
    if "Sn1per" in sniper_statuscheckd:
        return 1
    else:
        return 0

#check sniper dependencies is installed
def sniper_install_check():
    print("\033[1;32m[+] Checking Sn1per Installation.\033[00m")
    sniper_statuscheck2 = subprocess.run("sniper", shell=True, stdout=subprocess.PIPE)
    sniper_statuscheckd2 = sniper_statuscheck2.stdout.decode('ascii')
    if "This script must be run as root" or "You need to specify a target or workspace" in sniper_statuscheckd2:
        return 1
    else:
        return 0

#file saved to /usr/share/sniper/loot/workspace/*

def main():
    global normal_o_r_flag, normal_flag, stealth_o_r_flag, target
    target = ""
    normal_flag = 0
    normal_o_r_flag = 0
    stealth_o_r_flag = 0
    if sniper_self_check() == 1:
        if sniper_install_check() == 1:
            sniper_select = ""
            while sniper_select != "99":
                sniper_banner()
                sniper_select = input("\nSelect: ")
                if sniper_select == "1":
                    target = input("\nTarget: ")
                    target = target.strip()
                    if target == "":
                        print("\n[*] Target cannot be empty!")
                        useless = input("Enter any key to continue......")
                        continue
                elif sniper_select == "2":
                    if normal_flag != 1:
                        normal_flag = 1
                        normal_o_r_flag = 0
                        stealth_o_r_flag = 0
                    else:
                        normal_flag = 0
                elif sniper_select == "3":
                    if normal_o_r_flag != 1:
                        normal_flag = 0
                        normal_o_r_flag = 1
                        stealth_o_r_flag = 0
                    else:
                        normal_o_r_flag = 0
                elif sniper_select == "4":
                    if stealth_o_r_flag != 1:
                        normal_flag = 0
                        normal_o_r_flag = 0
                        stealth_o_r_flag = 1
                    else:
                        stealth_o_r_flag = 0
                elif sniper_select == "5":
                    pass#
                    
        else:
            print("\n\033[1;31m[-] Please install sniper through ./Sn1per/install.sh !\033[00m")
            seless = input("Enter any key to continue......")
    else:
        print("\n\033[1;31m[-] Sn1per is not installed!\033[00m")
        useless = input("Enter any key to continue......")
