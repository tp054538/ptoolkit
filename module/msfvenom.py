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

def msfvenom_check_valid_payload(payload_input):
    #read all valid payloads
    valid_payload_list = []
    with open("module/config/msfvenom_valid_payload_list") as file:
        valid_payload = file.readlines()
        for line in valid_payload:
            valid_payload_list.append(line.replace("\n","").strip())
        file.close()
    #search payload
    if payload_input == "search":
        msfvenom_payload_search_list = []
        msfvenom_payload_search = input("\nSearch Payload with keywords: ").strip().lower()
        if msfvenom_payload_search == "" or " " in msfvenom_payload_search:
            print("\n[*] Field is empty / contain space!")
            useless = input("\nEnter any key to continue......")
            return 0
        for i in range(len(valid_payload_list)):
            if msfvenom_payload_search in valid_payload_list[i]:
                msfvenom_payload_search_list.append(valid_payload_list[i].replace(msfvenom_payload_search,"\033[1;31m"+msfvenom_payload_search+"\033[00m"))
        if len(msfvenom_payload_search_list) == 0:
            print("\n[*] No matched payload found!")
            useless = input("\nEnter any key to continue......")
            return 0
        else:
            print("\n\033[1;32mMsfvenom Payloads: \033[00m")
            for i in range(len(msfvenom_payload_search_list)):
                print("{}. {}".format(i+1,msfvenom_payload_search_list[i]))
            useless = input("\nEnter any key to continue......")
            return 1
    #view all payloads
    if payload_input == "view":
        print("\n\033[1;32mMsfvenom Payloads: \033[00m")
        for i in range(len(valid_payload_list)):
            print("{}. {}".format(i+1,valid_payload_list[i]))
        useless = input("\nEnter any key to continue......")
    #validate payload is available
    else:
        for i in range(len(valid_payload_list)):
            if payload_input.strip() == valid_payload_list[i].strip():
                return 1
        return 0
    
def msfvenom_check_valid_encoder(encoder_input):
    #read valid all encoders
    valid_encoder_list = []
    with open("module/config/msfvenom_full_encoders") as file:
        valid_encoder = file.readlines()
        for line in valid_encoder:
            valid_encoder_list.append(line.replace("\n","").strip())
        file.close()
    #search encoder
    if encoder_input == "search":
        msfvenom_encoder_search_list = []
        msfvenom_encoder_search = input("\nSearch encoders: ").strip().lower()
        if msfvenom_encoder_search == "" or " " in msfvenom_encoder_search:
            print("\n[*] Field is empty / contain space!")
            useless = input("\nEnter any key to continue......")
            return 0
        for i in range(len(valid_encoder_list)):
            if msfvenom_encoder_search in valid_encoder_list[i]:
                msfvenom_encoder_search_list.append(valid_encoder_list[i].replace(msfvenom_encoder_search,"\033[1;31m"+msfvenom_encoder_search+"\033[00m"))
        if len(msfvenom_encoder_search_list) == 0:
            print("\n[*] No matched encoder found!")
            useless = input("\nEnter any key to continue......")
            return 0
        else:
            print("\n\033[1;32mMsfvenom Encoders: \033[00m")
            for i in range(len(msfvenom_encoder_search_list)):
                print("{}. {}".format(i+1,msfvenom_encoder_search_list[i]))
            useless = input("\nEnter any key to continue......")
            return 1
    #view all encoders
    if encoder_input == "view":
        print("\n\033[1;32mMsfvenom Encoders: \033[00m")
        for i in range(len(valid_encoder_list)):
            print("{}. {}".format(i+1,valid_encoder_list[i]))
        useless = input("\nEnter any key to continue......")
    #validate encoder is available
    else:
        for i in range(len(valid_encoder_list)):
            if encoder_input.strip() == valid_encoder_list[i].strip():
                return 1
        return 0
    

def msfvenom_banner():
    os.system("clear")
    print("""
                        MsfVenom

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
    global msfvenom_final_command, msfvenom_payload_command, msfvenom_encoder_command
    msfvenom_payload_command = ""
    msfvenom_encoder_command = ""

    msfvenom_select = ""
    while msfvenom_select != "99":
        msfvenom_final_command = "msfvenom " + msfvenom_payload_command + msfvenom_encoder_command
        msfvenom_banner()
        msfvenom_select = input("\nSelect: ").strip()

        #payload
        if msfvenom_select == "1":
            print("\n*Enter \"search\" to search payloads or \"view\" to view all available payloads.")
            msfvenom_payload = input("Payload: ").strip()
            if msfvenom_payload == "" or " " in msfvenom_payload:
                msfvenom_payload = ""
                msfvenom_payload_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            #search and view available payloads
            if msfvenom_payload == "search":
                msfvenom_check_valid_payload(msfvenom_payload)
                continue
            elif msfvenom_payload == "view":
                msfvenom_check_valid_payload(msfvenom_payload)
                continue
            #check if payload is correct
            if msfvenom_check_valid_payload(msfvenom_payload) != 1:
                msfvenom_payload = ""
                msfvenom_payload_command = ""
                print("\n[*] Invalid payload! Search or view all avaialbe payloads to confirm if its available.")######
                useless = input("Enter any key to continue......")
                continue
            msfvenom_payload_command = "-p " + msfvenom_payload + " "
        #encoders
        elif msfvenom_select == "2":
            print("\n*Enter \"search\" to search payloads or \"view\" to view all available encoders.")
            msfvenom_encoder = input("Encoder: ").strip()
            if msfvenom_encoder == "" or " " in msfvenom_encoder:
                msfvenom_encoder = ""
                msfvenom_encoder_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_encoder == "search":
                msfvenom_check_valid_encoder(msfvenom_encoder)
                continue
            elif msfvenom_encoder == "view":
                msfvenom_check_valid_encoder(msfvenom_encoder)
                continue
            if msfvenom_check_valid_encoder(msfvenom_encoder) != 1:
                msfvenom_encoder = ""
                msfvenom_encoder_command = ""
                print("\n[*] Invalid encoder! Search or view all avaialbe encoders to confirm if its available.")######
                useless = input("Enter any key to continue......")
                continue
            msfvenom_encoder_command = "-e " + msfvenom_encoder + " "
        #check payload arguments
        elif msfvenom_select == "91":
            if msfvenom_payload_command == "":
                print("\n[*] Payload is not specified!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_check_argument_command = "msfvenom " + msfvenom_payload_command + "--list-options"
            print("\033[1;32m[+] Loading MsfVenom to check arguments......\033[00m")
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