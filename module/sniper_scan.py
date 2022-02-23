import os
from module import sniper

def sniper_scan_banner():
    #show current working directory
    current_working_directory = os.getcwd() + "/"

    #use color to let user know which they have selected
    if sniper_web_scan == 1:
        sniper_web_color = "\033[1;32m"
    else:
        sniper_web_color = "\033[00m"

    if sniper_mweb_scan == 1:
        sniper_mweb_color = "\033[1;32m"
    else:
        sniper_mweb_color = "\033[00m"
    
    if sniper_vuln_scan == 1:
        sniper_vuln_color = "\033[1;32m"
    else:
        sniper_vuln_color = "\033[00m"
    
    if sniper_mvuln_scan == 1:
        sniper_mvuln_color = "\033[1;32m"
    else:
        sniper_mvuln_color = "\033[00m"
    
    os.system("clear")
    print("""
                        Web / Vulnerability Scanner (Sn1per)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Single Target:

    1. Target (2. & 3.)       :   \033[1;32m"""+sniper_scan_target+"""\033[00m
    2. """+sniper_web_color+"""Web Scan\033[00m               -   Full HTTP & HTTPS scan via BurpSuite and Arachni
    3. """+sniper_vuln_color+"""Vuln Scan\033[00m              -   OpenVAS vulnerability Scan 

Multiple Target:
*Current Working Directory: \033[1;32m"""+current_working_directory+"""\033[00m

    4. Targets file (4. & 5.) :   \033[1;32m"""+sniper_mscan_file_fullpath+"""\033[00m
    5. """+sniper_mweb_color+"""Mass Web Scan\033[00m          -   Multiple targets Web Scan
    6. """+sniper_mvuln_color+"""Mass Vuln Scan\033[00m         -   Multiple targets Vuln Scan

   90. Launch Attack
   99. Exit
    """)

def check_file_exist(filepath):
    if filepath.startswith("/") or filepath.startswith("~/"): #treat this as full path
        if filepath.startswith("~/"):
            filepath = os.path.expanduser(filepath)
        if os.path.isfile(filepath) == True:
            return 1
        else:
            return 0
    else:   #treat this to start from current working directory
        cwd = os.getcwd()
        cwd_and_filepath = cwd + "/" + filepath
        if os.path.isfile(cwd_and_filepath) == True:
            return 1
        else:
            return 0

def main():
    global sniper_web_scan, sniper_vuln_scan, sniper_mweb_scan, sniper_mvuln_scan, sniper_scan_target, sniper_mscan_file, sniper_mscan_file_fullpath
    sniper_web_scan = 0
    sniper_mweb_scan = 0
    sniper_vuln_scan = 0
    sniper_mvuln_scan = 0
    sniper_scan_target = ""
    sniper_mscan_file_fullpath = ""
    sniper_scan_base_command = "sudo sniper "
    sniper_scan_target_param = ""

    if sniper.sniper_self_check() == 1:
        if sniper.sniper_install_check() == 1:
            sniper_scan_select = ""
            while sniper_scan_select != "99":
                sniper_scan_banner()
                sniper_scan_select = input("\nSelect: ")
                # 1 for single target
                if sniper_scan_select == "1":
                    sniper_scan_target = input("\nTarget: ")
                    sniper_scan_target = sniper_scan_target.strip()
                    if sniper_scan_target == "":
                        print("\n[*] Target cannot be empty!")
                        useless = input("Enter any key to continue......")
                        continue
                    sniper_mscan_file_fullpath = ""

                # 4 for multiple target (file only)
                elif sniper_scan_select == "4":
                    sniper_mscan_file = input("\nTarget file's filepath: ")
                    sniper_mscan_file = sniper_mscan_file.strip()
                    if sniper_mscan_file == "":
                        print("\n[*] Target file cannot be empty!")
                        useless = input("Enter any key to continue......")
                        continue
                    if check_file_exist(sniper_mscan_file) == 0:
                        print("\n[*] Target file does not exist! Make sure the file path is correct.")
                        sniper_mscan_file_fullpath = ""
                        useless = input("Enter any key to continue......")
                        continue
                    sniper_mscan_file_fullpath = os.getcwd() + "/" + sniper_mscan_file
                    sniper_scan_target = ""

                elif sniper_scan_select == "2":
                    if sniper_web_scan != 1:
                        sniper_web_scan = 1
                        sniper_mweb_scan = 0
                        sniper_vuln_scan = 0
                        sniper_mvuln_scan = 0
                    else:
                        sniper_web_scan = 0
                elif sniper_scan_select == "3":
                    if sniper_vuln_scan != 1:
                        sniper_web_scan = 0
                        sniper_mweb_scan = 0
                        sniper_vuln_scan = 1
                        sniper_mvuln_scan = 0
                    else:
                        sniper_vuln_scan = 0
                elif sniper_scan_select == "5":
                    if sniper_mweb_scan != 1:
                        sniper_web_scan = 0
                        sniper_mweb_scan = 1
                        sniper_vuln_scan = 0
                        sniper_mvuln_scan = 0
                    else:
                        sniper_mweb_scan = 0
                elif sniper_scan_select == "6":
                    if sniper_mvuln_scan != 1:
                        sniper_web_scan = 0
                        sniper_mweb_scan = 0
                        sniper_vuln_scan = 0
                        sniper_mvuln_scan = 1
                    else:
                        sniper_mvuln_scan = 0
                #launch attack command
                elif sniper_scan_select == "90":
                    #check target
                    if sniper_scan_target == "" and sniper_mscan_file_fullpath == "":
                        print("\n[*] Target is empty! Please specify the target.")
                        useless = input("Enter any key to continue......")
                        continue
                    #check single or multiple target
                    if sniper_scan_target != "":
                        sniper_scan_target_param = "-t "
                    elif sniper_mscan_file_fullpath != "":
                        sniper_scan_target_param = "-f "
                    
                    #check which mode is selected
                    #flag for determine mass or single mode
                    sniper_single_flag = 0
                    sniper_mass_flag = 0
                    #check single target for single mode
                    if sniper_web_scan == 1:
                        sniper_mode = "-m web "
                        if sniper_scan_target == "":
                            print("\n[*] Wrong target specified. Please specify single target at 1. Target.")
                            useless = input("Enter any key to continue......")
                            continue
                        sniper_single_flag = 1
                    elif sniper_vuln_scan == 1:
                        sniper_mode = "-m vulnscan "
                        if sniper_scan_target == "":
                            print("\n[*] Wrong target specified. Please specify single target at 1. Target.")
                            useless = input("Enter any key to continue......")
                            continue
                        sniper_single_flag = 1
                    #check file target for multiple mode
                    elif sniper_mweb_scan == 1:
                        sniper_mode = "-m massweb "
                        if sniper_mscan_file_fullpath == "":
                            print("\n[*] Wrong target specified. Please specify multiple target at 4. Targets file.")
                            useless = input("Enter any key to continue......")
                            continue
                        sniper_mass_flag = 1
                    elif sniper_mvuln_scan == 1:
                        sniper_mode = "-m massvulnscan "
                        if sniper_mscan_file_fullpath == "":
                            print("\n[*] Wrong target specified. Please specify multiple target at 4. Targets file.")
                            useless = input("Enter any key to continue......")
                            continue
                        sniper_mass_flag = 1
                    else:
                        print("\n[*] No mode selected! Please select which scan mode before launching the attack.")
                        useless = input("Enter any key to continue......")
                        continue
                    
                    #variable for mass mode *single mode also can use 
                    sniper_mass_workspace = ""
                    sniper_mass_filename = input("\nEnter a directory name for storing result: ")
                    sniper_mass_filename = sniper_mass_filename.strip()
                    if sniper_mass_filename == "":
                        print("\n[*] Directory name cannot be empty!")
                        useless = input("Enter any key to continue......")
                        continue
                    sniper_mass_workspace = "-w " + sniper_mass_filename

                    #generate command and launch
                    if sniper_mass_flag == 1:
                        sniper_scan_launch_command = sniper_scan_base_command + sniper_scan_target_param + sniper_scan_target + sniper_mscan_file_fullpath + " " + sniper_mode + sniper_mass_workspace
                    elif sniper_single_flag == 1:
                        sniper_scan_launch_command = sniper_scan_base_command + sniper_scan_target_param + sniper_scan_target + sniper_mscan_file_fullpath + " " + sniper_mode 
                    print("\033[1;32m\n[+] Starting Sn1per Scan\033[00m")
                    os.system(sniper_scan_launch_command)
                    
                    #move file to cwd 
                    #single mode
                    move_to_path = os.getcwd() + "/result/"
                    if sniper_single_flag == 1:
                        sniper_scan_move_result = "sudo mv /usr/share/sniper/loot/workspace/" + sniper_scan_target + " " + move_to_path + sniper_mass_filename
                    #mass mode
                    elif sniper_mass_flag == 1:
                        sniper_scan_move_result = "sudo mv /usr/share/sniper/loot/workspace/" + sniper_mass_filename + " " + move_to_path + sniper_mass_filename
                    os.system(sniper_scan_move_result)
                    print("\033[1;32m\n[+] File saved to ./result/{}\033[00m".format(sniper_mass_filename))
                    useless = input("\033[1;32m\n[+] Process Completed. Enter any key to continue\033[00m")
                    
        else:
            print("\n\033[1;31m[-] Please install sniper through ./Sn1per/install.sh !\033[00m")
            useless = input("Enter any key to continue......")
    else:
        print("\n\033[1;31m[-] Sn1per is not installed!\033[00m")
        useless = input("Enter any key to continue......")
