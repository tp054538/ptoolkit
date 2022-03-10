import os
import subprocess
from module.sniper_scan import check_file_exist

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

def msfvenom_check_valid_platform(platform):
    valid_platform_list = []
    with open("module/config/msfvenom_platform_list") as file:
        valid_platform = file.readlines()
        for line in valid_platform:
            valid_platform_list.append(line.replace("\n","").strip())
        file.close()
    #view all platform
    if platform == "view":
        print("\n\033[1;32mMsfvenom Platforms: \033[00m")
        for i in range(len(valid_platform_list)):
            print("{}. {}".format(i+1,valid_platform_list[i]))
        useless = input("\nEnter any key to continue......")
    #validate if platform
    else:
        for i in range(len(valid_platform_list)):
            if platform.strip() == valid_platform_list[i].strip():
                return 1
        return 0

def msfvenom_check_valid_arch(arch):
    valid_arch_list = []
    with open("module/config/msfvenom_arch_list") as file:
        valid_arch = file.readlines()
        for line in valid_arch:
            valid_arch_list.append(line.replace("\n","").strip())
        file.close()
    #view all arch
    if arch == "view":
        print("\n\033[1;32mMsfvenom Archs: \033[00m")
        for i in range(len(valid_arch_list)):
            print("{}. {}".format(i+1,valid_arch_list[i]))
        useless = input("\nEnter any key to continue......")
    #validate if platform
    else:
        for i in range(len(valid_arch_list)):
            if arch.strip() == valid_arch_list[i].strip():
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
        msf_encoder_banner = "Encode the payload"
    else:
        msf_encoder_banner = "\033[1;32m" + msfvenom_encoder_command.replace("-e ","").strip() + "\033[00m"
    
    if msfvenom_iteration_command == "":
        msf_iteration_banner = "Encode the payload with n times"
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
    
    if msfvenom_platform_command == "":
        msfvenom_platform_banner = "Specify the platform for payload"
    else:
        msfvenom_platform_banner = "\033[1;32m" + msfvenom_platform_command.replace("--platform","").strip() + "\033[00m"
    
    if msfvenom_arch_command == "":
        msfvenom_arch_banner = "Specify the architecture for payload and encoder"
    else:
        msfvenom_arch_banner = "\033[1;32m" + msfvenom_arch_command.replace("-a","").strip() + "\033[00m"
    
    if msfvenom_embed_command == "":
        msfvenom_embed_banner = "Embed payload into an executable file"
    else:
        msfvenom_embed_banner = "\033[1;32m" + msfvenom_embed_command.replace("-x","").strip() + "\033[00m"

    os.system("clear")
    print("""
                    Payload Generator with Encoder (MSFvenom)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Payload         :   """+msf_payload_banner+"""
    2. Format          :   """+msf_format_banner+"""

    3. Encoder         :   """+msf_encoder_banner+"""
    4. Iteration       :   """+msf_iteration_banner+"""
    5. Platform        :   """+msfvenom_platform_banner+"""
    6. Arch            :   """+msfvenom_arch_banner+"""
    7. Argument 1      :   """+msfvenom_1_banner+"""
    8. Argument 2      :   """+msfvenom_2_banner+"""
    9. Argument 3      :   """+msfvenom_3_banner+"""
   10. Argument 4      :   """+msfvenom_4_banner+"""
   11. Embed into file :   """+msfvenom_embed_banner+"""

Command: \033[1;32m"""+msfvenom_final_command+"""\033[00m
   
   90. Launch Attack
   91. Check Payload's required arguments
   99. Exit
""")

def msfvenom_main():
    global msfvenom_final_command, msfvenom_payload_command, msfvenom_encoder_command, msfvenom_iteration_command, msfvenom_format_command
    global msfvenom_1_command, msfvenom_2_command, msfvenom_3_command, msfvenom_4_command, msfvenom_platform_command, msfvenom_arch_command, msfvenom_embed_command
    msfvenom_payload_command = ""
    msfvenom_encoder_command = ""
    msfvenom_iteration_command = ""
    msfvenom_format_command = ""
    msfvenom_1_command = ""
    msfvenom_2_command = ""
    msfvenom_3_command = ""
    msfvenom_4_command = ""
    msfvenom_platform_command = ""
    msfvenom_arch_command = ""
    msfvenom_embed_command = ""

    msfvenom_select = ""
    while msfvenom_select != "99":
        msfvenom_argument_total = msfvenom_1_command + msfvenom_2_command + msfvenom_3_command + msfvenom_4_command
        msfvenom_final_command = "msfvenom " + msfvenom_arch_command + msfvenom_platform_command + msfvenom_payload_command + msfvenom_argument_total + msfvenom_encoder_command + msfvenom_iteration_command + msfvenom_embed_command + msfvenom_format_command
        msfvenom_banner()
        msfvenom_select = input("\nSelect: ").strip()

        #payload
        if msfvenom_select == "1":
            print("\n*Enter \"search\" to search payloads or \"view\" to view all available payloads.")
            msfvenom_payload = input("Payload: ").strip().lower()
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
        #Formats
        elif msfvenom_select == "2":
            print("\n*Type \"format-1\" to view all executable formats or \"format-2\" to view all transforms format.")
            msfvenom_format = input("Format: ").strip().lower()
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
        #encoders
        elif msfvenom_select == "3":
            print("\n*Enter \"search\" to search encoders or \"view\" to view all available encoders.")
            msfvenom_encoder = input("Encoder: ").strip().lower()
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
        elif msfvenom_select == "4":
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
        #Platform
        elif msfvenom_select == "5":
            print("\n*Enter \"view\" to view all platforms.")
            msfvenom_platform = input("Platform: ").strip().lower()
            if msfvenom_platform == "" or " " in msfvenom_platform:
                msfvenom_platform = ""
                msfvenom_platform_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_platform == "view":
                msfvenom_check_valid_platform(msfvenom_platform)
                continue
            if msfvenom_check_valid_platform(msfvenom_platform) != 1:
                msfvenom_platform = ""
                msfvenom_platform_command = ""
                print("\n[*] Invalid platform! View all avaialbe platforms to confirm if its available.")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_platform_command = "--platform " + msfvenom_platform + " "
        #Arch
        elif msfvenom_select == "6":
            print("\n*Enter \"view\" to view all archs.")
            msfvenom_arch = input("Arch: ").strip().lower()
            if msfvenom_arch == "" or " " in msfvenom_arch:
                msfvenom_arch = ""
                msfvenom_arch_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_arch == "view":
                msfvenom_check_valid_arch(msfvenom_arch)
                continue
            if msfvenom_check_valid_arch(msfvenom_arch) != 1:
                msfvenom_arch = ""
                msfvenom_arch_command = ""
                print("\n[*] Invalid arch! View all avaialbe archs to confirm if its available.")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_arch_command = "-a " + msfvenom_arch + " "

        #4 arguments name cannot be duplicated
        #Arguments 1
        elif msfvenom_select == "7":
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
        elif msfvenom_select == "8":
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
        elif msfvenom_select == "9":
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
        elif msfvenom_select == "10":
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
        #embed
        elif msfvenom_select == "11":
            print("\nCurrent Directory: \033[1;32m"+os.getcwd()+"/\033[00m")
            msf_embed_file = input("File to be embedded into: ").strip()
            if msf_embed_file == "" or " " in msf_embed_file:
                msfvenom_embed_command = ""
                msf_embed_file = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if check_file_exist(msf_embed_file) != 1:
                msfvenom_embed_command = ""
                msf_embed_file = ""
                print("\n[*] File not found!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_embed_command = "-x " + msf_embed_file + " "         

        #launch attack
        elif msfvenom_select == "90":
            #check condition
            if msfvenom_payload_command == "":
                print("\n[*] Payload is empty!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_format_command == "":
                print("\n[*] Format is empty!")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_iteration_command != "" and msfvenom_encoder_command == "":
                print("\n[*] Iteration must be used with encoder! Clear iteration or specify an encoder.")
                useless = input("Enter any key to continue......")
                continue
            if msfvenom_1_command == "" and msfvenom_2_command == "" and msfvenom_3_command == "" and msfvenom_4_command == "":
                print("\n[*] No Arguments specified. Please make sure the required arguments with 91.")
                msf_continue = input("Do you want to continue launching the command? (y/n): ").strip()
                if msf_continue == "y" or msf_continue == "Y":
                    pass
                else:
                    continue
            #prompt output filename
            msfvenom_filename = input("Output Filename: ").strip()
            if msfvenom_filename == "":
                print("\n[*] Field is empty!")
                useless = input("Enter any key to continue......")
                continue
            msfvenom_filename = msfvenom_filename.replace(" ","_")
            msfvenom_filename_command = "-o ./result/" + msfvenom_filename
            print("\033[1;32m[+] Starting MsfVenom......\033[00m")
            os.system(msfvenom_final_command.strip()+" "+msfvenom_filename_command)
            print("\033[1;32m[+] Payload generated at ./result/{}\033[00m".format(msfvenom_filename.strip()))
            useless = input("Enter any key to continue......")
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