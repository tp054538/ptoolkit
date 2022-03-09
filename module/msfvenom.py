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
    

def msfvenom_check_format(format):
    #exec format
    msf_exec_format_list = []
    with open("module/config/msfvenom_exec_format") as execfile:
        exec = execfile.readlines()
        for line in exec:
            msf_exec_format_list.append(line.replace("\n","").strip())
        execfile.close()
    #trans format
    msf_trans_format_list = []
    with open("module/config/msfvenom_trans_format") as tranfile:
        trans = tranfile.readlines()
        for line in trans:
            msf_trans_format_list.append(line.replace("\n","").strip())
        tranfile.close()
    #print all executable format
    if format == "format-1":
        print("\n\033[1;32mMsfvenom Executable Formats: \033[00m")
        for i in range(len(msf_exec_format_list)):
            print("{}. {}".format(i+1,msf_exec_format_list[i]))
        useless = input("\nEnter any key to continue......")
    #print all transform format
    elif format == "format-2":
        print("\n\033[1;32mMsfvenom Transform Formats: \033[00m")
        for i in range(len(msf_trans_format_list)):
            print("{}. {}".format(i+1,msf_trans_format_list[i]))
        useless = input("\nEnter any key to continue......")
    #validate if format exist
    else:
        for i in range(len(msf_exec_format_list)):
            if format.strip() == msf_exec_format_list[i].strip():
                return 1
        for i in range(len(msf_trans_format_list)):
            if format.strip() == msf_trans_format_list[i].strip():
                return 1
        return 0

def msfvenom_banner():
    if msfvenom_payload_command == "":
        msf_payload_banner = ""
    else:
        msf_payload_banner = "\033[1;32m" + msfvenom_payload_command.replace("-p ","").strip() + "\033[00m"
    
    if msfvenom_encoder_command == "":
        msf_encoder_banner = ""
    else:
        msf_encoder_banner = "\033[1;32m" + msfvenom_encoder_command.replace("-e ","").strip() + "\033[00m"
    
    if msfvenom_iteration_command == "":
        msf_iteration_banner = ""
    else:
        msf_iteration_banner = "\033[1;32m" + msfvenom_iteration_command.replace("-i ","").strip() + "\033[00m"
    
    if msfvenom_format_command == "":
        msf_format_banner = ""
    else:
        msf_format_banner = "\033[1;32m" + msfvenom_format_command.replace("-f ","").strip() + "\033[00m"
    
    if msfvenom_1_command == "":
        msfvenom_1_banner = "Check payload's argument with 91. and enter here."
    else:
        msfvenom_1_banner = "\033[1;32m" + msfvenom_1_command.strip() + "\033[00m"
    
    if msfvenom_2_command == "":
        msfvenom_2_banner = "Check payload's argument with 91. and enter here."
    else:
        msfvenom_2_banner = "\033[1;32m" + msfvenom_2_command.strip() + "\033[00m"
    
    if msfvenom_3_command == "":
        msfvenom_3_banner = "Check payload's argument with 91. and enter here."
    else:
        msfvenom_3_banner = "\033[1;32m" + msfvenom_3_command.strip() + "\033[00m"
    
    if msfvenom_4_command == "":
        msfvenom_4_banner = "Check payload's argument with 91. and enter here."
    else:
        msfvenom_4_banner = "\033[1;32m" + msfvenom_4_command.strip() + "\033[00m"

    os.system("clear")
    print("""
                        MsfVenom

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Payload      :   """+msf_payload_banner+"""
    2. Encoder      :   """+msf_encoder_banner+"""
    3. Iteration    :   """+msf_iteration_banner+"""
    4. Format       :   """+msf_format_banner+"""

    5. Argument 1   :   """+msfvenom_1_banner+"""
    6. Argument 2   :   """+msfvenom_2_banner+"""
    7. Argument 3   :   """+msfvenom_3_banner+"""
    8. Argument 4   :   """+msfvenom_4_banner+"""

Command: \033[1;32m"""+msfvenom_final_command+"""\033[00m
   
   90. Launch Attack
   91. Check Payload's required arguments
   99. Exit
""")

def msfvenom_main():
    global msfvenom_final_command, msfvenom_payload_command, msfvenom_encoder_command, msfvenom_iteration_command, msfvenom_format_command
    global msfvenom_1_command, msfvenom_2_command, msfvenom_3_command, msfvenom_4_command
    msfvenom_payload_command = ""
    msfvenom_encoder_command = ""
    msfvenom_iteration_command = ""
    msfvenom_format_command = ""
    msfvenom_1_command = ""
    msfvenom_2_command = ""
    msfvenom_3_command = ""
    msfvenom_4_command = ""

    msfvenom_select = ""
    while msfvenom_select != "99":
        msfvenom_final_command = "msfvenom " + msfvenom_payload_command + msfvenom_encoder_command + msfvenom_iteration_command + msfvenom_format_command + msfvenom_1_command + msfvenom_2_command
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
                print("\n[*] Invalid payload! Search or view all avaialbe payloads to confirm if its available.")
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
                print("\n[*] Invalid encoder! Search or view all avaialbe encoders to confirm if its available.")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_encoder_command = "-e " + msfvenom_encoder + " "
        #Iteration
        elif msfvenom_select == "3":
            if msfvenom_encoder_command == "":
                msfvenom_iteration = 0
                msfvenom_iteration_command = ""
                print("\n[*] Specify encoder first before iteration!")
                useless = input("Enter any key to continue......")
                continue
            try:
                msfvenom_iteration = int(input("\nIteration: ").strip())
                if msfvenom_iteration < 1:
                    raise ValueError
            except ValueError:
                msfvenom_iteration = 0
                msfvenom_iteration_command = ""
                print("\n[*] Error Value! Positive integer only.")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_iteration_command = "-i " + str(msfvenom_iteration) + " "
        #Formats
        elif msfvenom_select == "4":
            print("\nType \"format-1\" to view all executable formats or \"format-2\" to view all transforms format.")
            msfvenom_format = input("\nFormat: ").strip().lower()
            if msfvenom_format == "" or " " in msfvenom_format:
                msfvenom_format = ""
                msfvenom_format_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_format == "format-1" or msfvenom_format == "format-2":
                msfvenom_check_format(msfvenom_format)
                continue
            #check if format exist
            if msfvenom_check_format(msfvenom_format) != 1:
                msfvenom_format = ""
                msfvenom_format_command = ""
                print("\n[*] Invalid format! View all avaialbe formats to see supported formats.")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_format_command = "-f " + msfvenom_format + " "
        #4 arguments name cannot be duplicated
        #Arguments 1
        elif msfvenom_select == "5":
            if msfvenom_payload_command == "":
                msfvenom_1_command = ""
                print("\n[*] Specify payload first before arguments!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_1_input = input("\nArgument (format -> name=value) (Eg. LHOST=127.0.0.1) : ").strip()
            if msfvenom_1_input == "" or " " in msfvenom_1_input:
                msfvenom_1_input = ""
                msfvenom_1_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_1_input.count("=") != 1:
                msfvenom_1_input = ""
                msfvenom_1_command = ""
                print("\n[*] Error format!")
                useless = input("Enter any key to continue......")
                continue
            if "" in msfvenom_1_input.split("="):
                msfvenom_1_input = ""
                msfvenom_1_command = ""
                print("\n[*] No argument name / value provided!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_1_input.split("=")[0].lower() == msfvenom_2_command.strip().split("=")[0].lower() or msfvenom_1_input.split("=")[0].lower() == msfvenom_3_command.strip().split("=")[0].lower() or msfvenom_1_input.split("=")[0].lower() == msfvenom_4_command.strip().split("=")[0].lower():
                msfvenom_1_input = ""
                msfvenom_1_command = ""
                print("\n[*] Duplicated argument!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_1_command = msfvenom_1_input + " "
        #Argument 2
        elif msfvenom_select == "6":
            if msfvenom_payload_command == "":
                msfvenom_2_command = ""
                print("\n[*] Specify payload first before arguments!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_2_input = input("\nArgument (format -> name=value) (Eg. LHOST=127.0.0.1) : ").strip()
            if msfvenom_2_input == "" or " " in msfvenom_2_input:
                msfvenom_2_input = ""
                msfvenom_2_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_2_input.count("=") != 1:
                msfvenom_2_input = ""
                msfvenom_2_command = ""
                print("\n[*] Error format!")
                useless = input("Enter any key to continue......")
                continue
            if "" in msfvenom_2_input.split("="):
                msfvenom_2_input = ""
                msfvenom_2_command = ""
                print("\n[*] No argument name / value provided!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_2_input.split("=")[0].lower() == msfvenom_1_command.strip().split("=")[0].lower() or msfvenom_2_input.split("=")[0].lower() == msfvenom_3_command.strip().split("=")[0].lower() or msfvenom_2_input.split("=")[0].lower() == msfvenom_4_command.strip().split("=")[0].lower():
                msfvenom_2_input = ""
                msfvenom_2_command = ""
                print("\n[*] Duplicated argument!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_2_command = msfvenom_2_input + " "
        #Argument 3
        elif msfvenom_select == "7":
            if msfvenom_payload_command == "":
                msfvenom_3_command = ""
                print("\n[*] Specify payload first before arguments!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_3_input = input("\nArgument (format -> name=value) (Eg. LHOST=127.0.0.1) : ").strip()
            if msfvenom_3_input == "" or " " in msfvenom_3_input:
                msfvenom_3_input = ""
                msfvenom_3_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_3_input.count("=") != 1:
                msfvenom_3_input = ""
                msfvenom_3_command = ""
                print("\n[*] Error format!")
                useless = input("Enter any key to continue......")
                continue
            if "" in msfvenom_3_input.split("="):
                msfvenom_3_input = ""
                msfvenom_3_command = ""
                print("\n[*] No argument name / value provided!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_3_input.split("=")[0].lower() == msfvenom_1_command.strip().split("=")[0].lower() or msfvenom_3_input.split("=")[0].lower() == msfvenom_2_command.strip().split("=")[0].lower() or msfvenom_3_input.split("=")[0].lower() == msfvenom_4_command.strip().split("=")[0].lower():
                msfvenom_3_input = ""
                msfvenom_3_command = ""
                print("\n[*] Duplicated argument!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_3_command = msfvenom_3_input + " "
        #Argument 4
        elif msfvenom_select == "8":
            if msfvenom_payload_command == "":
                msfvenom_4_command = ""
                print("\n[*] Specify payload first before arguments!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_4_input = input("\nArgument (format -> name=value) (Eg. LHOST=127.0.0.1) : ").strip()
            if msfvenom_4_input == "" or " " in msfvenom_4_input:
                msfvenom_4_input = ""
                msfvenom_4_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_4_input.count("=") != 1:
                msfvenom_4_input = ""
                msfvenom_4_command = ""
                print("\n[*] Error format!")
                useless = input("Enter any key to continue......")
                continue
            if "" in msfvenom_4_input.split("="):
                msfvenom_4_input = ""
                msfvenom_4_command = ""
                print("\n[*] No argument name / value provided!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_4_input.split("=")[0].lower() == msfvenom_1_command.strip().split("=")[0].lower() or msfvenom_4_input.split("=")[0].lower() == msfvenom_2_command.strip().split("=")[0].lower() or msfvenom_4_input.split("=")[0].lower() == msfvenom_3_command.strip().split("=")[0].lower():
                msfvenom_4_input = ""
                msfvenom_4_command = ""
                print("\n[*] Duplicated argument!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_4_command = msfvenom_4_input + " "



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