import os
import subprocess

def ss_banner():
    os.system("clear")
    print("""
                            Searchsploit by exploitdb

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Search       -       Search exploits and shellcodes from Exploit-DB
    2. Retrieve     -       Get details and full file path of the exploit     

   99. Exit
    """)

def ss_menu():
    ss_input = ""
    while ss_input != "99":
        ss_banner()
        ss_input = input("Select: ")
        if ss_input == "1":
            search_input = input("\nSearch: ")
            search_input = search_input.strip()
            if search_input == "":
                print("\n[*] Field is empty!")
                useless = input("Enter any key to continue......")
            else:
                search_command = "searchsploit " + search_input
                os.system(search_command)
                useless = input("\n[*] Process Completed. Enter any key to continue......")
        elif ss_input == "2":
            retrieve_input = input("Enter the file path from search: ")
            retrieve_input = retrieve_input.strip()
            if retrieve_input == "":
                print("\n[*] Empty! Please enter the file path from search.")
                useless = input("Enter any key to continue......")
                continue
            else:
                retrieve_list = retrieve_input.split("/")
                retrieve_list2 = retrieve_list[-1].split(".")
                retrieve_input = retrieve_list2[0]
                retrieve_command = "searchsploit -p " + retrieve_input
                ret = subprocess.run(retrieve_command, shell=True, stdout=subprocess.PIPE)
                ret_out = ret.stdout.decode('ascii')
                print(ret_out)
                if "Could not find EDB-ID" in ret_out:
                    print("\n[*] No exploit found. Please provide the exploit index filename.")
                    input("Enter any key to continue......")
                    continue
                copy_retrieve = input("\nDo you want to copy the file to ./result/ directory? (y/n): ")
                if copy_retrieve == "y" or copy_retrieve == "Y":
                    a = subprocess.run(retrieve_command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True,shell=True)
                    a = a.stdout.split("\n")
                    a = a[2].strip().split(":")
                    a = a[1].strip()
                    cp_filename_l = a.split(".")
                    cp_filename_ext = "." + cp_filename_l[1].strip()
                    copy_command = "sudo cp " + a + " ./result/" + retrieve_list2[0] + cp_filename_ext
                    os.system(copy_command)
                    print("\033[1;32m\n[+] File copied to ./result/{}{}\033[00m".format(retrieve_list2[0],cp_filename_ext))
                useless = input("\n[*] Process Completed. Enter any key to continue......")

def sploit_self_check():
    ssploit_statuscheck = subprocess.run("apt list 2>/dev/null | grep -E '^exploitdb/'", shell=True, stdout=subprocess.PIPE) 
    ssploit_statuscheckd = ssploit_statuscheck.stdout.decode('ascii')
    if "installed" in ssploit_statuscheckd or "upgradable" in ssploit_statuscheckd:
        return 1
    else:
        return 0

def main():
    print("\033[1;32m[+] Loading Searchsploit Module\033[00m")
    if sploit_self_check() == 1:
        ss_menu()
    else:
        print("\n\033[1;31m[-] Searchsploit is not installed!\033[00m")
        useless = input("Enter any key to continue......")