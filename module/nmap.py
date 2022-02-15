import configparser
import os
import ipaddress

# \033[00m default print font
# purple = "\033[1;35m"
#"\033[1;32m" green

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
    os.system("clear")
    print("""
                                      \033[1;31mNMAP\033[00m

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target: """+target_color+target+"""\033[00m

Scan Type:
    2. Default Scan      -  Scan the 1,000 most common ports
    3. Fast Scan         -  Scan the 100 most common ports
    4. Aggressive Scan   -  With OS Detection, Version Detection, Script Scanning, and Traceroute

Port Specification:
    5. Port ranges: """+port_range+"""
\n""")

def newscan():
    green = "\033[1;32m"
    red = "\033[1;31m"
    global target, target_color, port_range, port_range_color
    target_color = "\033[00m"
    port_range_color = "\033[00m"
    target = ""
    port_range = ""

    select = 0
    while select != 99:
        newscan_banner()
        try:
            select = int(input("Select: "))
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
                    target = target_ip
            elif select == 5:
                port_range_temp = input("Port Ranges (1-65535): ")
                port_range_temp.strip()
                if port_range_temp[0].isnumeric() == True:
                    port_range = port_range_temp.split('-')
                    if type(port_range) is list:
                        if len(port_range) != 2:
                            print("Invalid Port Range! Eg. 1-65535")
                            port_range = ""
                        else:
                            try:
                                if int(port_range[0]) >= 1 and int(port_range[1]) <= 65535:
                                    if int(port_range[0]) >= int(port_range[1]):
                                        print("Invalid Value. (Starting Port is bigger than Ending Port)")
                                        port_range = ""
                                    else:
                                        port_range = port_range[0] + "-" + port_range[1]
                                else:
                                    print("Port is out of range!")
                                    port_range = ""
                            except ValueError:
                                port_range = ""
                                print("Port Range is not numbers! Please enter numbers only.") 
                    else:
                        port_range = ""
                        print("Port Range format is wrong. Hypen (-) must be used and 1-65535 numbers only.")
                else:
                    port_range = ""
                    print("Port Range format is wrong. Numbers only.") 
            input(".......")            
        except ValueError:
            pass

def main():
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
    
    #read input and check condition
    user_input = 0
    while user_input != 4:
        user_input = 0
        banner()
        try:
            user_input = int(input("Select: "))
            if user_input == 1:
                newscan()
            elif user_input == 2:
                if scan1_desc == "Not defined":
                    print("\n[*] Custom Scan is not defined. Please configure it in New Scan")
                    useless = input("Enter any key to continue......")
                    continue
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
