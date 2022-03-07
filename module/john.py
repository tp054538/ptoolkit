import os
import subprocess
from module.sniper_scan import check_file_exist
from module.hydra import hydra_password_provided_wordlist

def john_self_check():
    john_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^john/'", shell=True, stdout=subprocess.PIPE)
    john_checkstatusd = john_checkstatus.stdout.decode('ascii')
    if "installed" in john_checkstatusd or "upgradable" in john_checkstatusd:
        return 1
    else:
        return 0

def john_print_incre():
    print("\n- - - - - - - - -Incremental Modes- - - - - - - - -")
    print("\n 1. ASCII (95 characters)")
    print(" 2. LM_ASCII (for LM hashes only)")
    print(" 3. Alnum (62 alphanumeric characters)")
    print(" 4. Alnumspace (62 alphanumeric characters + space)")
    print(" 5. Alpha (52 characters)")
    print(" 6. LowerNum (lowercase letter + numbers , 36 characters)")
    print(" 7. UpperNum (uppercase letter + numbers , 36 characters)")
    print(" 8. LowerSpace (lowercase + space , 27 characters)")
    print(" 9. Lower (lowercase letters, 26 characters)")
    print("10. Upper (uppercase letters, 26 characters)")
    print("11. Digits (1~10)")
    try:
        john_incre_input = int(input("\nSelect a mode: ").strip())
        if john_incre_input < 1 or john_incre_input > 11:
            raise ValueError
    except ValueError:
        return ""
    if john_incre_input == 1:
        return "ascii"
    elif john_incre_input == 2:
        return "lm_ascii"
    elif john_incre_input == 3:
        return "alnum"
    elif john_incre_input == 4:
        return "alnumspace"
    elif john_incre_input == 5:
        return "alpha"
    elif john_incre_input == 6:
        return "lowernum"
    elif john_incre_input == 7:
        return "uppernum"
    elif john_incre_input == 8:
        return "lowerspace"
    elif john_incre_input == 9:
        return "lower"
    elif john_incre_input == 10:
        return "upper"
    elif john_incre_input == 11:
        return "digits"
    else:
        return ""

def john_show_supported_format(viewtype):
    global john_supported_format_list_lower
    john_supported_format = """descrypt, bsdicrypt, md5crypt, md5crypt-long, bcrypt, scrypt, LM, AFS, 
tripcode, AndroidBackup, adxcrypt, agilekeychain, aix-ssha1, aix-ssha256, 
aix-ssha512, andOTP, ansible, argon2, as400-des, as400-ssha1, asa-md5, 
AxCrypt, AzureAD, BestCrypt, BestCryptVE4, bfegg, Bitcoin, BitLocker, 
bitshares, Bitwarden, BKS, Blackberry-ES10, WoWSRP, Blockchain, chap, 
Clipperz, cloudkeychain, dynamic_n, cq, CRC32, cryptoSafe, sha1crypt, 
sha256crypt, sha512crypt, Citrix_NS10, dahua, dashlane, diskcryptor, Django, 
django-scrypt, dmd5, dmg, dominosec, dominosec8, DPAPImk, dragonfly3-32, 
dragonfly3-64, dragonfly4-32, dragonfly4-64, Drupal7, eCryptfs, eigrp, 
electrum, EncFS, enpass, EPI, EPiServer, ethereum, fde, Fortigate256, 
Fortigate, FormSpring, FVDE, geli, gost, gpg, HAVAL-128-4, HAVAL-256-3, hdaa, 
hMailServer, hsrp, IKE, ipb2, itunes-backup, iwork, KeePass, keychain, 
keyring, keystore, known_hosts, krb4, krb5, krb5asrep, krb5pa-sha1, krb5tgs, 
krb5-17, krb5-18, krb5-3, kwallet, lp, lpcli, leet, lotus5, lotus85, LUKS, 
MD2, mdc2, MediaWiki, monero, money, MongoDB, scram, Mozilla, mscash, 
mscash2, MSCHAPv2, mschapv2-naive, krb5pa-md5, mssql, mssql05, mssql12, 
multibit, mysqlna, mysql-sha1, mysql, net-ah, nethalflm, netlm, netlmv2, 
net-md5, netntlmv2, netntlm, netntlm-naive, net-sha1, nk, notes, md5ns, 
nsec3, NT, o10glogon, o3logon, o5logon, ODF, Office, oldoffice, 
OpenBSD-SoftRAID, openssl-enc, oracle, oracle11, Oracle12C, osc, ospf, 
Padlock, Palshop, Panama, PBKDF2-HMAC-MD4, PBKDF2-HMAC-MD5, PBKDF2-HMAC-SHA1, 
PBKDF2-HMAC-SHA256, PBKDF2-HMAC-SHA512, PDF, PEM, pfx, pgpdisk, pgpsda, 
pgpwde, phpass, PHPS, PHPS2, pix-md5, PKZIP, po, postgres, PST, PuTTY, 
pwsafe, qnx, RACF, RACF-KDFAES, radius, RAdmin, RAKP, rar, RAR5, Raw-SHA512, 
Raw-Blake2, Raw-Keccak, Raw-Keccak-256, Raw-MD4, Raw-MD5, Raw-MD5u, Raw-SHA1, 
Raw-SHA1-AxCrypt, Raw-SHA1-Linkedin, Raw-SHA224, Raw-SHA256, Raw-SHA3, 
Raw-SHA384, restic, ripemd-128, ripemd-160, rsvp, RVARY, Siemens-S7, 
Salted-SHA1, SSHA512, sapb, sapg, saph, sappse, securezip, 7z, Signal, SIP, 
skein-256, skein-512, skey, SL3, Snefru-128, Snefru-256, LastPass, SNMP, 
solarwinds, SSH, sspr, Stribog-256, Stribog-512, STRIP, SunMD5, SybaseASE, 
Sybase-PROP, tacacs-plus, tcp-md5, telegram, tezos, Tiger, tc_aes_xts, 
tc_ripemd160, tc_ripemd160boot, tc_sha512, tc_whirlpool, vdi, OpenVMS, vmx, 
VNC, vtp, wbb3, whirlpool, whirlpool0, whirlpool1, wpapsk, wpapsk-pmk, 
xmpp-scram, xsha, xsha512, zed, ZIP, ZipMonster, plaintext, has-160, 
HMAC-MD5, HMAC-SHA1, HMAC-SHA224, HMAC-SHA256, HMAC-SHA384, HMAC-SHA512, 
dummy, crypt"""
    john_supported_format_list = john_supported_format.replace(" ","").replace("\n","").split(",")
    john_supported_format_list_lower = []
    for i in range(len(john_supported_format_list)):
        john_supported_format_list_lower.append(john_supported_format_list[i].lower())
    if viewtype == 1:
        search_store_list = []
        john_supported_input = input("\nSearch: ").strip()
        if john_supported_input == "":
            print("\n[*] Field is empty!")
            useless = input("Enter any key to continue......")
            return 0
        for i in range(len(john_supported_format_list)):
            if john_supported_input.lower() in john_supported_format_list[i].lower():
                search_store_list.append(john_supported_format_list[i])
        if len(search_store_list) == 0:
            print("\nNo format found!")
            useless = input("Enter any key to continue......")
            return 0
        else:
            print("\n\033[1;32mResult:\033[00m")
            for i in range(len(search_store_list)):
                print("{}. {}".format(i+1,search_store_list[i]))
            return 1
    elif viewtype == 2:
        print("\n"+john_supported_format)
    #initiate
    elif viewtype == 3:
        pass
        

def john_banner():
    if john_wordlist_command == "":
        john_wordlist_banner = "Default = password.lst"
    else:
        john_wordlist_banner = "\033[1;32m" + john_wordlist_command.replace("--wordlist=","").strip() + "\033[00m"
    
    if john_format_command == "":
        john_format_banner = "Default = Auto Detect (specify to increase accuracy)"
    else:
        john_format_banner = "\033[1;32m" + john_format_command.replace("--format=","").strip() + "\033[00m"
    
    if john_mangle_flag == 1:
        john_mangle_color = "\033[1;32m"
    else:
        john_mangle_color = "\033[00m"
    
    if john_min_length_command == "":
        john_min_banner = "Specify minimum length words to look for in wordlist"
    else:
        john_min_banner = "\033[1;32m" + john_min_length_command.replace("--min-length=","").strip() + "\033[00m"
    
    if john_max_length_command == "":
        john_max_banner = "Specify maximum length words to look for in wordlist"
    else:
        john_max_banner = "\033[1;32m" + john_max_length_command.replace("--max-length=","").strip() + "\033[00m"
    
    if john_incremental_command == "":
        john_incremental_banner = "Use Brute Force"
    else:
        john_incremental_banner = "\033[1;32m" + john_incremental_command.replace("--incremental:","").strip() + "\033[00m"

    os.system("clear")
    print("""
                        Password Cracker (JohnTheRipper)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. File         :   \033[1;32m"""+john_target+"""\033[00m
    2. Wordlist     :   """+john_wordlist_banner+"""
    3. Incremental  :   """+john_incremental_banner+"""
    4. Hash Format  :   """+john_format_banner+"""

    5. """+john_mangle_color+"""Mangle Mode\033[00m - Produce additional likely password based on the wordlist
    6. Min Length   :   """+john_min_banner+"""
    7. Max Length   :   """+john_max_banner+"""

Command: \033[1;32m"""+john_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
""")

def john_main():
    global john_final_command, john_target, john_wordlist_command, john_format_command, john_mangle_flag, john_min_length_command, john_max_length_command, john_incremental_command
    john_target = ""
    john_wordlist_command = ""
    john_format_command = ""
    john_mangle_command = ""
    john_mangle_flag = 0
    john_min_length_command = ""
    john_max_length_command = ""
    john_incremental_command = ""

    john_select = ""
    while john_select != "99":
        john_final_command = "john " + john_incremental_command + john_wordlist_command + john_mangle_command + john_format_command + john_min_length_command + john_max_length_command +  john_target
        john_banner()
        john_select = input("\nSelect: ").strip()
        #password/hash file to crack
        if john_select == "1":
            john_target = input("\nTarget File: ").strip()
            if john_target == "" or " " in john_target:
                john_target = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if check_file_exist(john_target) != 1:
                john_target = ""
                print("\n[*] File not found!")
                useless = input("Enter any key to continue......")
                continue
        #wordlist
        elif john_select == "2":
            print("\nType \"wordlists\" to select from provided wordlists.")
            john_wordlist = input("Wordlist File: ").strip()
            if john_wordlist == "" or " " in john_wordlist:
                john_wordlist = ""
                john_wordlist_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if john_wordlist == "wordlists":
                john_wordlist = hydra_password_provided_wordlist()
            if check_file_exist(john_wordlist) != 1:
                john_wordlist = ""
                john_wordlist_command = ""
                print("\n[*] File not found!")
                useless = input("Enter any key to continue......")
                continue
            john_wordlist_command = "--wordlist=" + john_wordlist + " "
            john_incremental_command = ""
        #incremental
        elif john_select == "3":
            john_incremental = john_print_incre()
            if john_incremental == "":
                john_incremental_command = ""
                print("\nError Value / Out of Range! 1~10 only.")
                useless = input("Enter any key to continue......")
                continue
            john_incremental_command = "--incremental:" + john_incremental + " "
            john_wordlist_command = ""
            john_wordlist = ""
        #hash format
        elif john_select == "4":
            john_show_supported_format(3)
            print("\nType \"search\" to search for supported format. Type \"View\" to view all supported format.")
            john_format = input("Hash Format: ").strip()
            if john_format.lower() == "search":
                john_return = john_show_supported_format(1)
                if john_return == 1:
                    john_format = input("\nHash Format: ").strip()
                else:
                    continue
            elif john_format.lower() == "view":
                john_show_supported_format(2)
                john_format = input("\nHash Format: ").strip()
            if john_format == "" or " " in john_format:
                john_format = ""
                john_format_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            if john_format.lower() not in john_supported_format_list_lower:
                john_format = ""
                john_format_command = ""
                print("\n[*] Format not found! Check available format by search or view all supported formats.")
                useless = input("Enter any key to continue......")
                continue
            john_format_command = "--format=" + john_format + " "
        #Mangle
        elif john_select == "5":
            if john_mangle_flag != 1:
                john_mangle_flag = 1
                john_mangle_command = "--rules:Jumbo "
            else:
                john_mangle_flag = 0
                john_mangle_command = ""
        #min length
        elif john_select == "6":
            try:
                john_min_length = int(input("\nMinimum Length: ").strip())
                if john_min_length < 1:
                    raise ValueError
            except ValueError:
                john_min_length_command = ""
                print("\n[*] Error Value Provided! Positive number only.")
                useless = input("Enter any key to continue......")
                continue
            if john_max_length_command != "":
                if int(john_max_length_command.replace("--max-length=","").strip()) < john_min_length:
                    john_min_length_command = ""
                    print("\n[*] Minimum length cannot be bigger than minimum length!")
                    useless = input("Enter any key to continue......")
                    continue
            john_min_length_command = "--min-length=" + str(john_min_length) + " "
        #max length
        elif john_select == "7":
            try:
                john_max_length = int(input("\nMaximum Length: ").strip())
                if john_max_length < 1:
                    raise ValueError
            except ValueError:
                john_max_length_command = ""
                print("\n[*] Error Value Provided! Positive number only.")
                useless = input("Enter any key to continue......")
                continue
            if john_min_length_command != "":
                if int(john_min_length_command.replace("--min-length=","").strip()) > john_max_length:
                    john_max_length_command = ""
                    print("\n[*] Maximum length cannot be smaller than minimum length!")
                    useless = input("Enter any key to continue......")
                    continue
            john_max_length_command = "--max-length=" + str(john_max_length) + " "
        #launch attack
        elif john_select == "90":
            if john_target == "":
                print("\n[*] No file is selected!")
                useless = input("Enter any key to continue......")
                continue
            if john_wordlist_command == "" and john_incremental_command == "":
                print("\n[*] Specify Wordlist or Incremental Mode to launch attack!")
                useless = input("Enter any key to continue......")
                continue
            if john_mangle_command != "" and john_incremental_command != "":
                print("\n[*] Mangle mode can be used with wordlist only!")
                useless = input("Enter any key to continue......")
                continue
            print("\033[1;32m[+] Starting JohnTheRipper......\033[00m")
            os.system(john_final_command)
            useless = input("\033[1;32m[*] Process Completed!\033[00m\nEnter any key to continue......")



            

def main():
    print("\033[1;32m[+] Loading JohnTheRipper Module\033[00m")
    if john_self_check() == 1:
        john_main()
    else:
        print("\n\033[1;31m[-] JohnTheRipper is not installed!\033[00m")
        useless = input("Enter any key to continue......")
    