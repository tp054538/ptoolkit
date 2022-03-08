import os
import subprocess
from sys import stderr

def msfvenom_self_check():
    msf_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^metasploit-framework/'", shell=True, stdout=subprocess.PIPE)
    msf_checkstatusd = msf_checkstatus.stdout.decode('ascii')
    if "installed" in msf_checkstatusd or "upgradable" in msf_checkstatusd:
        return 1
    else:
        return 0

def msfvenom_banner():
    os.system("clear")
    print("""
                        Password Cracker (JohnTheRipper)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Payload      :   s
    2. Encoder      :   s
    3. Argument 1   :   s
    4. Argument 2   :   s
    5. Argument 3   :   s
    6. Argument 4   :   s

Command: \033[1;32m"""+msfvenom_final_command+"""\033[00m
   
   90. Launch Attack
   91. Check Payload's required arguments
   99. Exit
""")

def msfvenom_main():
    global msfvenom_final_command, msfvenom_payload_command
    msfvenom_payload_command = ""

    msfvenom_select = ""
    while msfvenom_select != "99":
        msfvenom_final_command = "msfvenom " + msfvenom_payload_command
        msfvenom_banner()
        msfvenom_select = input("\nSelect: ").strip()
        if msfvenom_select == "1":
            msfvenom_payload = input("\nPayload: ").strip()
            if msfvenom_payload == "" or " " in msfvenom_payload:
                msfvenom_payload = ""
                msfvenom_payload_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_payload_command = "-p " + msfvenom_payload + " "
        elif msfvenom_select == "91":
            if msfvenom_payload_command == "":
                print("\n[*] Payload is not specified!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_check_argument_command = "msfvenom " + msfvenom_payload_command + "--list-options"
            msfvenom_check_argument = subprocess.run(msfvenom_check_argument_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            msfvenom_check_argumentd = msfvenom_check_argument.stdout.decode("ascii")
            msfvenom_check_starting = msfvenom_check_argumentd.find("Basic options:")
            msfvenom_check_ending = msfvenom_check_argumentd.find("Description",msfvenom_check_argumentd.find("Description")+1)
            msfvenom_grep_argument_section = msfvenom_check_argumentd[msfvenom_check_starting:msfvenom_check_ending]
            if msfvenom_grep_argument_section.replace(" ","") == "":
                print("\033[1;31m[-] Invalid Payload Specified!\033[00m")
            else:
                print("\n" + msfvenom_grep_argument_section.replace("Basic options:","\033[1;32mArguments:\033[00m").rstrip())
            useless = input("\nEnter any key to continue......")

def main():
    print("\033[1;32m[+] Loading MsfVenom Module\033[00m")
    if msfvenom_self_check() == 1:
        msfvenom_main()
    else:
        print("\n\033[1;31m[-] MsfVenom is not installed!\033[00m")
        useless = input("Enter any key to continue......")
"""
#logic to grep all basic options for payload
payload = input("Payload: ").strip()
if payload != "":
    txt_input = "msfvenom -p " + payload + " --list-options"
    txt2 = subprocess.run(txt_input, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    txt = txt2.stdout.decode('ascii')
grep_start = txt.find("Basic options:")
grep_stop = txt.find("Description",txt.find("Description")+1)
grep = txt[grep_start:grep_stop]
print(grep)
"""