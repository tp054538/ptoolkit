import configparser
import os
import ipaddress
from sqlalchemy import desc

from websockets import protocol

# \033[00m default print font
# purple = "\033[1;35m"
#"\033[1;32m" green
def port_duplicate_check(ports):
    ports_set = set(ports)
    if type(ports) is list:
        if len(ports_set) != len(ports):
            return True
        else:
            return False
    else:
        return False

#def port_value_check():

def banner():
    os.system("clear")
    print("""
                                      \033[1;31mNMAP\033[00m

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. New Scan
            -  \033[0;35mLaunch a Nmap Scan\033[00m

    2. """+custom_scan1.capitalize()+"\n            -  \033[0;35m"+scan1_desc.capitalize()+"""\033[00m

    3. """+custom_scan2.capitalize()+"\n            -  \033[0;35m"+scan2_desc.capitalize()+"""\033[00m

    4. Exit
            -  \033[0;35mBack to main menu\033[00m
    """)

def newscan_banner():
    #determine which shortcuts is selected, only can select 1
    if shortcut_flag == 2:
        default_scan_flag = "\033[1;32m"
        aggressive_flag = "\033[00m"
        fast_scan_flag = "\033[00m"
    elif shortcut_flag == 3:
        fast_scan_flag = "\033[1;32m"
        default_scan_flag = "\033[00m"
        aggressive_flag = "\033[00m"
    elif shortcut_flag == 4:
        aggressive_flag = "\033[1;32m"
        default_scan_flag = "\033[00m"
        fast_scan_flag = "\033[00m"
    else:
        default_scan_flag = "\033[00m"
        fast_scan_flag = "\033[00m"
        aggressive_flag = "\033[00m"
    
    #scan technique colour
    if udpscan_flag == 1:
        udp_color = "\033[1;32m"
    else:
        udp_color = "\033[00m"
    #
    if synscan_flag == 1:
        syn_color = "\033[1;32m"
    else:
        syn_color = "\033[00m"
    #
    if nullscan_flag == 1:
        null_color = "\033[1;32m"
    else:
        null_color = "\033[00m"
    #
    if finscan_flag == 1:
        fin_color = "\033[1;32m"
    else:
        fin_color = "\033[00m"
    #
    if xmasscan_flag == 1:
        xmas_color = "\033[1;32m"
    else:
        xmas_color = "\033[00m"
    #
    if ipprotocol_flag == 1:
        ipprotocol_color = "\033[1;32m"
    else:
        ipprotocol_color = "\033[00m"
    #
    if os_detection_flag == 1:
        os_color = "\033[1;32m"
    else:
        os_color = "\033[00m"
    #reserve for speed
    #
    if verbose_flag == 1:
        verbose_color = "\033[1;32m"
    else:
        verbose_color = "\033[00m"
    #
    if xverbose_flag == 1:
        xverbose_color = "\033[1;32m"
    else:
        xverbose_color = "\033[00m"

    os.system("clear")
    print("""
                                      \033[1;31mNMAP\033[00m

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target: """+target_color+target+"""\033[00m

\033[1;33mShortcuts: (Maximum select 1 only)\033[00m
    2. """+default_scan_flag+"""Default Scan\033[00m      -  Scan the 1,000 most common ports
    3. """+fast_scan_flag+"""Fast Scan\033[00m         -  Scan the 100 most common ports
    4. """+aggressive_flag+"""Aggressive Scan\033[00m   -  OS, Version Detection, Script Scanning, and Traceroute
\033[1;33mPort Specification: (Select either 1 or leave empty)\033[00m
    5. Port ranges     :  \033[1;32m"""+port_range+"""\033[00m
    6. Specific Ports  :  \033[1;32m"""+specific_port+"""\033[00m
\033[1;33mScan Techniques:\033[00m
    7. """+udp_color+"""UDP Scan\033[00m         -   Send UDP packets
    8. """+syn_color+"""TCP SYN Scan\033[00m     -   Send TCP SYN packets, relatively stealthy
    9. """+null_color+"""TCP NULL Scan\033[00m    -   Identify listening TCP ports with flagless TCP packet
   10. """+fin_color+"""TCP FIN Scan\033[00m     -   Set TCP FIN packets, more invisible compared to SYN Scan
   11. """+xmas_color+"""TCP Xmas Scan\033[00m    -   Utilize TCP FIN, PSH, and URG flags to perform scan
   12. """+ipprotocol_color+"""IP Protocol Scan\033[00m -   Scan the IP protocols used (cant use with other scan techniques)
\033[1;33mOthers:\033[00m
   13. """+os_color+"""OS Detection\033[00m     -   Scan the target machine running OS
   14. Scan Speed (0-5) :   \033[1;32m"""+str(scanspeed)+"""\033[00m
   15. """+verbose_color+"""Verbose\033[00m          -   Get more information when nmap is running
   16. """+xverbose_color+"""Extra Verbose\033[00m    -   Get all information when nmap is running
\033[1;33mOperation:\033[00m
   90. Launch Attack
   91. Save to Custom Scan Setting
   99. Exit

Attack Command: """+attack_command+"""
""")

def newscan():
    green = "\033[1;32m"
    red = "\033[1;31m"
    global target, target_color, port_range, port_range_color, specific_port, shortcut_flag, udpscan_flag, synscan_flag, nullscan_flag, finscan_flag
    global xmasscan_flag, ipprotocol_flag, os_detection_flag, scanspeed, verbose_flag, xverbose_flag
    global attack_command
    target_color = "\033[00m"
    port_range_color = "\033[00m"
    target = ""
    port_range = ""
    specific_port = ""

    select = 0
    shortcut_flag = 0
    udpscan_flag = 0
    synscan_flag = 0
    nullscan_flag = 0
    finscan_flag = 0
    xmasscan_flag = 0
    ipprotocol_flag = 0
    os_detection_flag = 0
    scanspeed = 2
    verbose_flag = 0
    xverbose_flag = 0
    attack_command = ""
    port = ""

    while select != 99:
        #clear other scan technique (if not nmap will fail)
        if ipprotocol_flag == 1:
            udpscan_flag = 0
            synscan_flag = 0
            nullscan_flag = 0
            finscan_flag = 0
            xmasscan_flag = 0
        
        #compile all settings and generate the command
        if shortcut_flag == 3:
            shortcut = "-F "
        elif shortcut_flag == 4:
            shortcut = "-A "
        else:
            shortcut = ""
        
        if (port_range + specific_port) != "":
            port = "-p "+ port_range + specific_port + " "
        
        attack_command = "sudo nmap "
        scan_technique = ""
        verbose_command = ""
        os_detect = ""
        scanspeed_command = " -T"
        scanspeed_command += str(scanspeed)

        if ipprotocol_flag == 1:
            scan_technique = "-sO "
        else:
            if udpscan_flag == 1:
                scan_technique += "-sU "
            if synscan_flag == 1:
                scan_technique += "-sS "
            if nullscan_flag == 1:
                scan_technique += "-sN "
            if finscan_flag == 1:
                scan_technique += "-sF "
            if xmasscan_flag == 1:
                scan_technique += "-sX "
            scan_technique = scan_technique
        if verbose_flag == 1:
            verbose_command = "-v "
        elif xverbose_flag == 1:
            verbose_command = "-vv "
        if os_detection_flag == 1:
            os_detect = "-O "

        attack_command += verbose_command + shortcut + port + scan_technique + os_detect + target + scanspeed_command
        newscan_banner()
        try:
            select = int(input("Select: "))
            #target
            if select == 1:
                target_ip = input("Target IP Address: ")
                #check ip address format valid
                try:
                    ip = ipaddress.ip_address(target_ip)
                    target_color = green
                except ValueError:
                    if target_ip[0].isnumeric() == True:
                        print("\n{} is not a valid IP Address format.".format(target_ip))
                        useless = input("Enter any key to continue......")
                    target_color = red
                    continue
                finally:
                    target = target_ip.strip()

            #Shortcuts (only can choose 1), reselect again will cancel selection
            elif select == 2:
                if shortcut_flag != 2:
                    shortcut_flag = 2
                else:
                    shortcut_flag = 0
            elif select == 3:
                if shortcut_flag != 3:
                    shortcut_flag = 3
                else:
                    shortcut_flag = 0
            elif select == 4:
                if shortcut_flag != 4:
                    shortcut_flag = 4
                else:
                    shortcut_flag = 0
            #port range -> no duplicate, min range must larger than max range, 1-65535, format check (-), numbers only / cancel specific port 
            elif select == 5:
                port_range_temp = input("Port Ranges (1-65535): ")
                port_range_temp.strip()
                if port_range_temp[0].isnumeric() == True:
                    port_range = port_range_temp.split('-')
                    if type(port_range) is list:
                        if len(port_range) != 2:
                            print("[*] Invalid Port Range! Eg. 1-65535")
                            port_range = ""
                            input("Enter any key to continue")   
                        else:
                            try:
                                if int(port_range[0]) >= 1 and int(port_range[1]) <= 65535:
                                    if int(port_range[0]) >= int(port_range[1]):
                                        print("[*] Invalid Value. (Starting Port is bigger than Ending Port)")
                                        port_range = ""
                                        input("Enter any key to continue")   
                                    else:
                                        port_range = port_range[0] + "-" + port_range[1]
                                        specific_port = ""
                                else:
                                    print("[*] Port is out of range!")
                                    port_range = ""
                                    input("Enter any key to continue")   
                            except ValueError:
                                port_range = ""
                                print("[*] Port Range is not numbers! Please enter numbers only.") 
                                input("Enter any key to continue")   
                    else:
                        port_range = ""
                        print("[*] Port Range format is wrong. Hypen (-) must be used and 1-65535 numbers only.")
                        input("Enter any key to continue")   
                else:
                    port_range = ""
                    print("[*] Port Range format is wrong. Numbers only.") 
                    input("Enter any key to continue")   
            #specific port (validation input -> 1-65535, only numbers, no duplicate / cancel port range
            elif select == 6:
                try:
                    specific_port = ""
                    specific_port_string = ""
                    specific_port_temp = input("\nSpecific Port (use a space between two ports number for multiple specific port): ")
                    specific_port_temp2 = specific_port_temp.strip().split()
                    if port_duplicate_check(specific_port_temp2) == True:
                        print("\n[*] Invalid Ports! Ports number duplicated!")
                        useless  = input("Enter any key to continue......")
                        continue
                    for i in range(len(specific_port_temp2)):
                        if specific_port_temp2[i].isnumeric() == True and int(specific_port_temp2[i]) >= 1 and int(specific_port_temp2[i]) <= 65535:
                            specific_port_string +=  str(specific_port_temp2[i]).strip() + ","
                            specific_port_string.strip()
                        else:
                            raise ValueError
                    specific_port = specific_port_string.strip(",")
                    port_range = ""
                except ValueError:
                    print("\n[*] Port numbers invalid.")
                    useless = input("Enter any key to continue......")
                    pass
            #Scan techniques
            elif select == 7: 
                if udpscan_flag != 1:
                    udpscan_flag = 1
                else:
                    udpscan_flag = 0
            elif select == 8:
                if synscan_flag != 1:
                    synscan_flag = 1
                    nullscan_flag = 0
                    finscan_flag = 0
                    xmasscan_flag = 0
                else:
                    synscan_flag = 0
            elif select == 9:
                if nullscan_flag != 1:
                    nullscan_flag = 1
                    synscan_flag = 0
                    xmasscan_flag = 0
                    finscan_flag = 0
                else:
                    nullscan_flag = 0
            elif select == 10:
                if finscan_flag != 1:
                    finscan_flag = 1
                    synscan_flag = 0
                    nullscan_flag = 0
                    xmasscan_flag = 0
                else:
                    finscan_flag = 0
            elif select == 11:
                if xmasscan_flag != 1:
                    xmasscan_flag = 1
                    synscan_flag = 0
                    finscan_flag = 0
                    nullscan_flag = 0
                else:
                    xmasscan_flag = 0
            elif select == 12:
                if ipprotocol_flag != 1: #ip protocol scan cannot use with other scan techniques
                    ipprotocol_flag = 1
                    udpscan_flag = 0
                    synscan_flag = 0
                    nullscan_flag = 0
                    finscan_flag = 0
                    xmasscan_flag = 0
                else:
                    ipprotocol_flag = 0
            #others section
            elif select == 13:
                if os_detection_flag != 1:
                    os_detection_flag = 1
                else:
                    os_detection_flag = 0
            elif select == 14:
                try:
                    speed = int(input("Speed (0-5): "))
                    if speed >= 0 and speed <= 5:
                        scanspeed = speed
                    else:
                        scanspeed = 2
                        raise ValueError
                except ValueError:
                    print("\n[*] Please enter numbers from 0 to 5 only!")
                    useless = input("Enter any key to continue......")
            elif select == 15:
                if verbose_flag != 1:
                    verbose_flag = 1
                    xverbose_flag = 0
                else:
                    verbose_flag = 0
            elif select == 16:
                if xverbose_flag != 1:
                    xverbose_flag = 1
                    verbose_flag = 0
                else:
                    xverbose_flag = 0
            #launch attack
            elif select == 90:
                if target == "" :
                    print("[*] Target cannot be empty!")
                    useless = input("Enter any key to continue......")
                else:
                    os.system(attack_command)
                    useless = input("\n[*] Completed. Enter any key to continue......")
            #save settings
            elif select == 91:
                file = '/module/config/nmap_config.txt'
                path = os.getcwd()+file
                custom_input = input("Save to Custom 1 or Custom 2? : ")
                write_config = configparser.ConfigParser()
                write_config.read(path)
                if custom_input == "1":
                    name = input("\nPlease enter a new name for custom scan 1: ")
                    description = input("\nPlease enter a new description for custom scan 1: ")
                    if name == "" or name[0].isalnum() == False:
                        name_flag = 0
                        print("[*] Name cannot be empty or start with space")
                        useless = input("Enter any key to continue......")
                        continue
                    if description == "" or description[0].isalnum() == False:
                        description_flag = 0
                        print("[*] Description cannot be empty or start with space")
                        useless = input("Enter any key to continue......")
                        continue

                    #change configuration file values
                    write_config.set('Custom1','shortcut_flag',str(shortcut_flag))
                    write_config.set('Custom1','udpscan_flag',str(udpscan_flag))
                    write_config.set('Custom1','synscan_flag',str(synscan_flag))
                    write_config.set('Custom1','nullscan_flag',str(nullscan_flag))
                    write_config.set('Custom1','finscan_flag',str(finscan_flag))
                    write_config.set('Custom1','xmasscan_flag',str(xmasscan_flag))
                    write_config.set('Custom1','ipprotocol_flag',str(ipprotocol_flag))
                    write_config.set('Custom1','os_detection_flag',str(os_detection_flag))
                    write_config.set('Custom1','scanspeed',str(scanspeed))
                    write_config.set('Custom1','verbose_Flag',str(verbose_flag))
                    write_config.set('Custom1','xverbose_flag',str(xverbose_flag))
                    write_config.set('Custom1','port',port)
                    write_config.set('nmap config','custom_scan1',name)
                    write_config.set('nmap config','scan1_desc',description)
                    with open(path, 'w') as configuration_file:
                        write_config.write(configuration_file)
                    
                elif custom_input == "2":
                    name = input("\nPlease enter a new name for custom scan 2: ")
                    description = input("\nPlease enter a new description for custom scan 2: ")
                    if name == "" or name[0].isalnum() == False:
                        name_flag = 0
                        print("[*] Name cannot be empty or start with space")
                        useless = input("Enter any key to continue......")
                        continue
                    if description == "" or description[0].isalnum() == False:
                        description_flag = 0
                        print("[*] Description cannot be empty or start with space")
                        useless = input("Enter any key to continue......")
                        continue

                    write_config.set('Custom2','shortcut_flag',str(shortcut_flag))
                    write_config.set('Custom2','udpscan_flag',str(udpscan_flag))
                    write_config.set('Custom2','synscan_flag',str(synscan_flag))
                    write_config.set('Custom2','nullscan_flag',str(nullscan_flag))
                    write_config.set('Custom2','finscan_flag',str(finscan_flag))
                    write_config.set('Custom2','xmasscan_flag',str(xmasscan_flag))
                    write_config.set('Custom2','ipprotocol_flag',str(ipprotocol_flag))
                    write_config.set('Custom2','os_detection_flag',str(os_detection_flag))
                    write_config.set('Custom2','scanspeed',str(scanspeed))
                    write_config.set('Custom2','verbose_Flag',str(verbose_flag))
                    write_config.set('Custom2','xverbose_flag',str(xverbose_flag))
                    write_config.set('Custom2','port',port)
                    write_config.set('nmap config','custom_scan2',name)
                    write_config.set('nmap config','scan2_desc',description)
                    with open(path, 'w') as configuration_file:
                        write_config.write(configuration_file)
                else:
                    print("\n[*] Invalid input. Please select either 1 or 2 custom scan to save.")
                    useless = input("Enter any key to continue.......")
                    continue
        except ValueError:
            pass

def custom_scan_menu():
    customparser = configparser.ConfigParser()
    file = '/module/config/nmap_config.txt'
    path = os.getcwd()+file
    customparser.read(path)
    """
    shortcut_flag = 0
    udpscan_flag = 0
    synscan_flag = 0
    nullscan_flag = 0
    finscan_flag = 0
    xmasscan_flag = 0
    ipprotocol_flag = 0
    os_detection_flag = 0
    scanspeed = 2
    verbose_flag = 0
    xverbose_flag = 0
    port = 
    """

def main():
    #read input and check condition
    user_input = 0
    while user_input != 4:
        #read nmap config file for custom 1 and custom 2 data
        parser = configparser.ConfigParser()
        file = '/module/config/nmap_config.txt'
        path = os.getcwd()+file
        
        parser.read(path)
        global custom_scan1, custom_scan2, scan1_desc, scan2_desc
        custom_scan1 = parser.get("nmap config","custom_scan1")
        scan1_desc  = parser.get("nmap config","scan1_desc")
        custom_scan2 = parser.get("nmap config","custom_scan2")
        scan2_desc = parser.get("nmap config","scan2_desc")
        ##########################################################

        user_input = 0
        banner()
        try:
            user_input = int(input("Select: "))
            if user_input == 1:
                newscan()
            elif user_input == 2:
                if scan1_desc == "Custom 1 Not Defined":
                    print("\n[*] Custom Scan is not defined. Please configure it in New Scan")
                    useless = input("Enter any key to continue......")
                    continue
                custom_scan_menu()
            elif user_input == 3:
                if scan2_desc == "Custom 2 Not Defined":
                    print("\n[*] Custom Scan is not defined. Please configure it in New Scan")
                    useless = input("Enter any key to continue......")
                    continue
                custom_scan_menu()
            elif user_input == 4:
                pass
            else:
                print("\n[*] Number entered is out of range! Please enter number from 1 - 4 only.")
                useless = input("Enter any key to continue......")
                continue
        except ValueError:
            print("\n[*] Invalid Input! Please enter numbers from 1 - 4 only.")
            useless = input("Enter any key to continue......")
            continue
