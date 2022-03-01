import os
import subprocess

def sqlmap_self_check():
    sqlmap_checkstatus = subprocess.run("apt list 2>/dev/null | grep -E '^sqlmap/'", shell=True, stdout=subprocess.PIPE)
    sqlmap_checkstatusd = sqlmap_checkstatus.stdout.decode('ascii')
    if "installed" in sqlmap_checkstatusd or "upgradable" in sqlmap_checkstatusd:
        return 1
    else:
        return 0

def sqlmap_enumerate_sub():
    sqlmap_enumerate_all_flag = 0
    sqlmap_enumerate_2_flag = 0
    sqlmap_enumerate_3_flag = 0
    sqlmap_enumerate_4_flag = 0
    sqlmap_enumerate_5_flag = 0
    sqlmap_enumerate_6_flag = 0
    sqlmap_enumerate_7_flag = 0
    sqlmap_enumerate_8_flag = 0
    sqlmap_enumerate_9_flag = 0
    sqlmap_enumerate_10_flag = 0


    sqlmap_enumerate_command = ""
    sqlmap_enumerate_2_command = ""
    sqlmap_enumerate_3_command = ""
    sqlmap_enumerate_4_command = ""
    sqlmap_enumerate_5_command = ""
    sqlmap_enumerate_6_command = ""
    sqlmap_enumerate_7_command = ""
    sqlmap_enumerate_8_command = ""
    sqlmap_enumerate_9_command = ""
    sqlmap_enumerate_10_command = ""

    sqlmap_enumerate_select = ""
    while sqlmap_enumerate_select != "99":
        #all flag override all settings
        if sqlmap_enumerate_all_flag != 1:
            sqlmap_enumerate_command = sqlmap_enumerate_2_command + sqlmap_enumerate_3_command +sqlmap_enumerate_4_command + sqlmap_enumerate_5_command + sqlmap_enumerate_6_command + sqlmap_enumerate_7_command
            sqlmap_enumerate_command += sqlmap_enumerate_8_command + sqlmap_enumerate_9_command + sqlmap_enumerate_10_command
        else:
            sqlmap_enumerate_command = "-a "
        
        #########colour########
        if sqlmap_enumerate_all_flag != 1:
            sqlmap_enumerate_1 = "\033[00m"
            if sqlmap_enumerate_2_flag == 1:
                sqlmap_enumerate_2 = "\033[1;32m"
            else:
                sqlmap_enumerate_2 = "\033[00m"
            if sqlmap_enumerate_3_flag == 1:
                sqlmap_enumerate_3 = "\033[1;32m"
            else:
                sqlmap_enumerate_3 = "\033[00m"
            if sqlmap_enumerate_4_flag == 1:
                sqlmap_enumerate_4 = "\033[1;32m"
            else:
                sqlmap_enumerate_4 = "\033[00m"
            if sqlmap_enumerate_5_flag == 1:
                sqlmap_enumerate_5 = "\033[1;32m"
            else:
                sqlmap_enumerate_5 = "\033[00m"
            if sqlmap_enumerate_6_flag == 1:
                sqlmap_enumerate_6 = "\033[1;32m"
            else:
                sqlmap_enumerate_6 = "\033[00m"
            if sqlmap_enumerate_7_flag == 1:
                sqlmap_enumerate_7 = "\033[1;32m"
            else:
                sqlmap_enumerate_7 = "\033[00m"
            if sqlmap_enumerate_8_flag == 1:
                sqlmap_enumerate_8 = "\033[1;32m"
            else:
                sqlmap_enumerate_8 = "\033[00m"
            if sqlmap_enumerate_9_flag == 1:
                sqlmap_enumerate_9 = "\033[1;32m"
            else:
                sqlmap_enumerate_9 = "\033[00m"
            if sqlmap_enumerate_10_flag == 1:
                sqlmap_enumerate_10 = "\033[1;32m"
            else:
                sqlmap_enumerate_10 = "\033[00m"
        else:
            sqlmap_enumerate_1 = "\033[1;32m"
            sqlmap_enumerate_2 = "\033[00m"
            sqlmap_enumerate_3 = "\033[00m"
            sqlmap_enumerate_4 = "\033[00m"
            sqlmap_enumerate_5 = "\033[00m"
            sqlmap_enumerate_6 = "\033[00m"
            sqlmap_enumerate_7 = "\033[00m"
            sqlmap_enumerate_8 = "\033[00m"
            sqlmap_enumerate_9 = "\033[00m"
            sqlmap_enumerate_10 = "\033[00m"
        os.system("clear")
        print("""
                          Joomla Scanner (JoomScan)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. """+sqlmap_enumerate_1+"""Retrieve Everything\033[00m

    2. """+sqlmap_enumerate_2+"""Retrieve DBMS banner\033[00m
    3. """+sqlmap_enumerate_3+"""Retrieve Current User\033[00m
    4. """+sqlmap_enumerate_4+"""Retrieve Current Database\033[00m
    5. """+sqlmap_enumerate_5+"""Enumerate Passwords\033[00m
    6. """+sqlmap_enumerate_6+"""Enumerate Database Tables\033[00m
    7. """+sqlmap_enumerate_7+"""Enumerate Database Columns\033[00m
    8. """+sqlmap_enumerate_8+"""Enumerate Database Schema\033[00m
    9. """+sqlmap_enumerate_9+"""Dump Database Table Entries\033[00m
   10. """+sqlmap_enumerate_10+"""Dump All Database Table Entries\033[00m
   11. Specify DBMS database to enumerate   :   N/A
   12. Specify DBMS table to enumerate      :   N/A
   13. Specify DBMS columns to enumerate    :   N/A

Selected: \033[1;32m"""+sqlmap_enumerate_command+"""\033[00m
   90. Submit
   99. Exit
    """)
        sqlmap_enumerate_select = input("\nSelect: ").strip()
        if sqlmap_enumerate_select == "1":
            if sqlmap_enumerate_all_flag != 1:
                sqlmap_enumerate_all_flag = 1
                sqlmap_enumerate_command = "-a "
            else:
                sqlmap_enumerate_all_flag = 0
                sqlmap_enumerate_command = ""
        elif sqlmap_enumerate_select == "2":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_2_flag != 1:
                sqlmap_enumerate_2_flag = 1
                sqlmap_enumerate_2_command = "--banner "
            else:
                sqlmap_enumerate_2_flag = 0
                sqlmap_enumerate_2_command = ""
        elif sqlmap_enumerate_select == "3":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_3_flag != 1:
                sqlmap_enumerate_3_flag = 1
                sqlmap_enumerate_3_command = "--current-user "
            else:
                sqlmap_enumerate_3_flag = 0
                sqlmap_enumerate_3_command = ""
        elif sqlmap_enumerate_select == "4":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_4_flag != 1:
                sqlmap_enumerate_4_flag = 1
                sqlmap_enumerate_4_command = "--current-db "
            else:
                sqlmap_enumerate_4_flag = 0
                sqlmap_enumerate_4_command = ""
        elif sqlmap_enumerate_select == "5":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_5_flag != 1:
                sqlmap_enumerate_5_flag = 1
                sqlmap_enumerate_5_command = "--passwords "
            else:
                sqlmap_enumerate_5_flag = 0
                sqlmap_enumerate_5_command = ""
        elif sqlmap_enumerate_select == "6":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_6_flag != 1:
                sqlmap_enumerate_6_flag = 1
                sqlmap_enumerate_6_command = "--tables "
            else:
                sqlmap_enumerate_6_flag = 0
                sqlmap_enumerate_6_command = ""
        elif sqlmap_enumerate_select == "7":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_7_flag != 1:
                sqlmap_enumerate_7_flag = 1
                sqlmap_enumerate_7_command = "--columns "
            else:
                sqlmap_enumerate_7_flag = 0
                sqlmap_enumerate_7_command = ""
        elif sqlmap_enumerate_select == "8":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_8_flag != 1:
                sqlmap_enumerate_8_flag = 1
                sqlmap_enumerate_8_command = "--schema "
            else:
                sqlmap_enumerate_8_flag = 0
                sqlmap_enumerate_8_command = ""
        elif sqlmap_enumerate_select == "9":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_9_flag != 1:
                sqlmap_enumerate_9_flag = 1
                sqlmap_enumerate_9_command = "--dump "
            else:
                sqlmap_enumerate_9_flag = 0
                sqlmap_enumerate_9_command = ""
        elif sqlmap_enumerate_select == "10":
            sqlmap_enumerate_all_flag = 0
            if sqlmap_enumerate_10_flag != 1:
                sqlmap_enumerate_10_flag = 1
                sqlmap_enumerate_10_command = "--dump-all "
            else:
                sqlmap_enumerate_10_flag = 0
                sqlmap_enumerate_10_command = ""
        #submit
        elif sqlmap_enumerate_select == "90":
            return sqlmap_enumerate_command
    return ""



def sqlmap_banner():
    sqlmap_target_banner = sqlmap_target_command.strip().replace("-u","").strip()

    if sqlmap_enumerate_banner == "":
        sqlmap_enumerate_banner_main = "\033[00mSpecify what to enumerate"
    elif sqlmap_enumerate_banner == "-a":
        sqlmap_enumerate_banner_main = "All"
    else:
        sqlmap_enumerate_banner_main = sqlmap_enumerate_banner
    
    if sqlmap_level_command == "":
        sqlmap_level_banner = "Higher Level = more tests and injection points (Default = 1)"
    else:
        sqlmap_level_banner = "\033[1;32m" + sqlmap_level_command.replace("--level","").strip() + "\033[00m"

    os.system("clear")
    print("""
                             SQL Injection (SQLmap)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target URL    : \033[1;32m"""+sqlmap_target_banner+"""\033[00m

    2. Level         : """+sqlmap_level_banner+"""
    3. Risk          : Higher Risk adds heavy queries and OR-based injection (Default = 1)
    4. Tor Proxy     - Use Tor proxy as an additional layer to hide identity
    5. Enumeration   : \033[1;32m"""+sqlmap_enumerate_banner_main+"""\033[00m

Command: \033[1;32m"""+sqlmap_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
    """)

def sqlmap_main():
    global sqlmap_enumerate_banner, sqlmap_final_command, sqlmap_target_command, sqlmap_level_command
    sqlmap_enumerate_banner = ""
    sqlmap_enumerate_main_command = ""
    sqlmap_target_command = ""
    sqlmap_level_command = ""

    sqlmap_select = ""
    while sqlmap_select != "99":
        sqlmap_final_command = "sqlmap " + sqlmap_target_command + sqlmap_level_command + sqlmap_enumerate_main_command
        sqlmap_banner()
        sqlmap_select = input("\nSelect: ")
        #target
        if sqlmap_select == "1":
            sqlmap_target = input("\nTarget URL: ").strip()
            if sqlmap_target == "" or " " in sqlmap_target:
                sqlmap_target_command = ""
                sqlmap_target = ""
                print("\n[*] Field is empty / Contain spaces!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_target_command = "-u " + sqlmap_target + " "
        #level
        elif sqlmap_select == "2":
            sqlmap_level = input("\nLevel (Range: 1~5, Higher level will consume more time): ").strip()
            if sqlmap_level == "" or " " in sqlmap_level:
                sqlmap_level = ""
                sqlmap_level_command = ""
                print("\n[*] Field is empty / Contain spaces!")
                useless = input("Enter any key to continue......")
                continue
            #validate if it is valid range 1-5
            try:
                sqlmap_level_validate = int(sqlmap_level)
                if sqlmap_level_validate < 1 or sqlmap_level_validate > 5:
                    raise ValueError
            except ValueError:
                print("\n[*] Error Level Range!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_level_command = "--level " + sqlmap_level + " "
        #risk
        elif sqlmap_select == "3":
            pass

        #enumerate section
        elif sqlmap_select == "5":
            sqlmap_enumerate_main_command = sqlmap_enumerate_sub()
            sqlmap_enumerate_banner = sqlmap_enumerate_main_command.replace("--","").strip().replace(" ",",")




def main():
    print("\033[1;32m[+] Loading SQLmap Module\033[00m")
    if sqlmap_self_check() == 1:
        sqlmap_main()
    else:
        print("\n\033[1;31m[-] SQLmap is not installed!\033[00m")
        useless = input("Enter any key to continue......")