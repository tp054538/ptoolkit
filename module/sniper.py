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
                            OSINT / Recon (Sn1per)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target URL/IP:  \033[1;32m"""+sniper_target+"""\033[00m

    2. """+normal_color+"""Normal Mode\033[00m                    -   Basic scans of target and open ports
    3. """+normal_o_r_color+"""Normal Mode + OSINT + Recon\033[00m    -   Normal + OSINT Recon
    4. """+stealth_o_r_color+"""Stealth Mode + OSINT + Recon\033[00m   -   Non-instrusive scan to avoid WAF/IPS + OSINT Recon

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

def main():
    global normal_o_r_flag, normal_flag, stealth_o_r_flag, sniper_target
    sniper_target = ""
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
                    sniper_target = input("\nTarget: ")
                    sniper_target = sniper_target.strip()
                    if sniper_target == "" or " " in sniper_target:
                        sniper_target = ""
                        print("\n[*] Target cannot be empty / Target cannot contain space between words!")
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
                    if sniper_target == "":
                        print("\n[*] Target cannot be empty!")
                        useless = input("Enter any key to continue......")
                        continue
                    else:
                        base_command = "sudo sniper -t " + sniper_target

                        if normal_o_r_flag == 1:
                            add_command = " -o -re"
                        elif stealth_o_r_flag == 1:
                            add_command = " -m stealth -o -re"
                        else:
                            add_command = ""
                        
                        launch_command = base_command + add_command
                        os.system(launch_command)

                        #move sniper result to /result directory
                        saved_filepath = "/usr/share/sniper/loot/workspace/" + sniper_target
                        working_directory = os.getcwd()
                        move_file_command = "sudo mv " + saved_filepath + " " + working_directory +"/result/" + sniper_target.replace(" ","_")
                        os.system(move_file_command)
                        print("\033[1;32m\n[+] File saved to ./result/{}\033[00m".format(sniper_target))
                        useless = input("\n[*] Process Completed. Enter any key to continue......")
        else:
            print("\n\033[1;31m[-] Please install sniper through ./Sn1per/install.sh !\033[00m")
            seless = input("Enter any key to continue......")
    else:
        print("\n\033[1;31m[-] Sn1per is not installed!\033[00m")
        useless = input("Enter any key to continue......")
