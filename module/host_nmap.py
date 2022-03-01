import os
from module import nmap

def hostd_banner():
    os.system("clear")
    print("""
                            Host Discovery Menu (Nmap)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Host Discovery   -   ARP Ping Scan             

   99. Exit
    """)

def check_subnet_format(ipaddr):
    if "/" in ipaddr:
        ipaddr_list = ipaddr.split("/")
        try:
            subnet = int(ipaddr_list[-1])
            if subnet >= 0 and subnet <= 32:
                return 1
            else:
                return 0
        except ValueError:
            return 0

    else:
        return 0

def check_ipaddr(ipaddr):
    ipaddr_check_list = ipaddr.split("/")
    ipaddr_check = ipaddr_check_list[0]
    ip_check = ipaddr_check.split(".")
    if len(ip_check) == 4:
        try:
            for i in range(4):
                if int(ip_check[i]) >= 0 and int(ip_check[i]) <= 255:
                    pass
                else:
                    return 0
        except ValueError:
            return 0
        return 1
    else:
        return 0


def main():
    if nmap.nmap_self_check() == 1:
        host_nmap_select = ""
        while host_nmap_select != "99":
            hostd_banner()
            host_nmap_select = input("\nSelect: ")
            if host_nmap_select == "1":
                user_nmap = input("\nTarget (IP address with subnet (eg. 192.168.0.1/24): ")
                user_nmap = user_nmap.strip()
                if user_nmap == "" or " " in user_nmap:
                    print("\n[*] Field is empty / Contain spaces!")
                    useless = input("Enter any key to continue......")
                else:
                    if check_subnet_format(user_nmap) == 1:
                        if check_ipaddr(user_nmap) == 1:
                            host_discovery_command = "sudo nmap " + user_nmap + " -sn"
                            output_to_file = input("Do you want to save the result to a file? (y/n) : ")
                            if output_to_file == "y" or output_to_file == "Y":
                                hostd_file_name = input("Filename: ").strip()
                                if hostd_file_name != "":
                                    hostd_file_name = hostd_file_name.replace(" ","_")
                                    host_discovery_command += " -o ./result/" + hostd_file_name
                                else:
                                    print("[*] Filename cannot be emtpy!")
                                    useless = input("Enter any key to continue......")
                                    continue
                            print("\033[1;32m[+] Starting NMAP Host Discovery\033[00m")
                            os.system(host_discovery_command)
                            if "-o" in host_discovery_command:
                                print("\n\033[1;32m[+] File saved to ./result/{}\033[00m".format(hostd_file_name))
                            useless = input("\nProcess Completed. Enter any key to continue......")
                        else:
                            print("\n[*] Invalid IP Address!")
                            useless = input("Enter any key to continue......")
                            continue
                    else:
                        print("\n[*] Invalid format / subnet error!")
                        useless = input("Enter any key to continue......")
                        continue
    else:
        print("\n\033[1;31m[-] Nmap is not installed!\033[00m")
        useless = input("Enter any key to continue......")
