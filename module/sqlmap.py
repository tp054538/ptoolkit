import os
import subprocess
from module import tor

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
    sqlmap_enumerate_11_command = ""
    sqlmap_enumerate_12_command = ""
    sqlmap_enumerate_13_command = ""

    sqlmap_enumerate_select = ""
    while sqlmap_enumerate_select != "99":
        #all flag override all settings
        if sqlmap_enumerate_all_flag != 1:
            sqlmap_enumerate_command = sqlmap_enumerate_2_command + sqlmap_enumerate_3_command +sqlmap_enumerate_4_command + sqlmap_enumerate_5_command + sqlmap_enumerate_6_command + sqlmap_enumerate_7_command
            sqlmap_enumerate_command += sqlmap_enumerate_8_command + sqlmap_enumerate_9_command + sqlmap_enumerate_10_command + sqlmap_enumerate_11_command + sqlmap_enumerate_12_command + sqlmap_enumerate_13_command 
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
            # D 
            if sqlmap_enumerate_11_command == "":
                sqlmap_enumerate_11 = "N/A" 
            else:
                sqlmap_enumerate_11 = "\033[1;32m" + sqlmap_enumerate_11_command.replace("-D","").strip() + "\033[00m"
            # T
            if sqlmap_enumerate_12_command == "":
                sqlmap_enumerate_12 = "N/A" 
            else:
                sqlmap_enumerate_12 = "\033[1;32m" + sqlmap_enumerate_12_command.replace("-T","").strip() + "\033[00m"
            # C
            if sqlmap_enumerate_13_command == "":
                sqlmap_enumerate_13 = "N/A" 
            else:
                sqlmap_enumerate_13 = "\033[1;32m" + sqlmap_enumerate_13_command.replace("-C","").strip() + "\033[00m"
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
            sqlmap_enumerate_11 = "N/A" 
            sqlmap_enumerate_12 = "N/A" 
            sqlmap_enumerate_13 = "N/A" 
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
   11. Specify DBMS database to enumerate   :   """+sqlmap_enumerate_11+"""
   12. Specify DBMS table to enumerate      :   """+sqlmap_enumerate_12+"""
   13. Specify DBMS columns to enumerate    :   """+sqlmap_enumerate_13+"""

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
        #specify database
        elif sqlmap_enumerate_select == "11":
            sqlmap_enumerate_database = input("\nDatabase to enumerate: ").strip()
            if sqlmap_enumerate_database == "" or " " in sqlmap_enumerate_database:
                sqlmap_enumerate_11_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue.....")
                continue
            sqlmap_enumerate_all_flag = 0
            sqlmap_enumerate_11_command = "-D " + sqlmap_enumerate_database + " "
        #specify tables
        elif sqlmap_enumerate_select == "12":
            sqlmap_enumerate_tables = input("\nTables to enumerate: ").strip()
            if sqlmap_enumerate_tables == "" or " " in sqlmap_enumerate_tables:
                sqlmap_enumerate_12_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue.....")
                continue
            sqlmap_enumerate_all_flag = 0
            sqlmap_enumerate_12_command = "-T " + sqlmap_enumerate_tables + " "
        #specify columns
        elif sqlmap_enumerate_select == "13":
            sqlmap_enumerate_columns = input("\nColumns to enumerate: ").strip()
            if sqlmap_enumerate_columns == "" or " " in sqlmap_enumerate_columns:
                sqlmap_enumerate_13_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue.....")
                continue
            sqlmap_enumerate_all_flag = 0
            sqlmap_enumerate_13_command = "-C " + sqlmap_enumerate_columns + " "
        #submit
        elif sqlmap_enumerate_select == "90":
            return sqlmap_enumerate_command
    return ""



def sqlmap_banner():
    sqlmap_target_banner = sqlmap_target_command.replace("-u","").replace("\"","").strip()

    if sqlmap_enumerate_banner == "":
        sqlmap_enumerate_banner_main = "\033[00mSpecify what to enumerate"
    elif sqlmap_enumerate_banner == "-a":
        sqlmap_enumerate_banner_main = "All"
    else:
        sqlmap_enumerate_banner_main = sqlmap_enumerate_banner
    
    if sqlmap_level_command == "":
        sqlmap_level_banner = "Higher Level = more tests and injection points (Default = 1)"
    else:
        sqlmap_level_banner = "\033[1;32m" + sqlmap_level_command.replace("--level=","").strip() + "\033[00m"
    
    if sqlmap_risk_command == "":
        sqlmap_risk_banner = "Higher Risk adds heavy queries and OR-based injection (Default = 1)"
    else:
        sqlmap_risk_banner = "\033[1;32m" + sqlmap_risk_command.replace("--risk=","").strip() + "\033[00m"
    
    if sqlmap_tor_flag == 1:
        sqlmap_tor_banner = "\033[1;32m" + "socks5://127.0.0.1:9050 (Tor)" + "\033[00m"
    else:
        sqlmap_tor_banner = "Use Tor proxy as an additional layer to hide identity"
    
    if sqlmap_cookie_command == "":
        sqlmap_cookie_banner = "Specify cookie to use"
    else:
        sqlmap_cookie_banner = "\033[1;32m" + sqlmap_cookie_command.replace("--cookie=","").strip().strip("\"") + "\033[00m"
    
    if sqlmap_rua_flag == 1:
        sqlmap_rua_color = "\033[1;32m"
    else:
        sqlmap_rua_color = "\033[00m"

    if sqlmap_data_string_command == "":
        sqlmap_data_banner = "Provide data to be sent through POST (eg. id=1 or password=abc123):"
    else:
        sqlmap_data_banner = "\033[1;32m" + sqlmap_data_string_command.replace("--data=","").strip().strip("\"") + "\033[00m"
    
    if sqlmap_testpara_command == "":
        sqlmap_testpara_banner = "Specify which parameter is testable among all parameters (Save Time)"
    else:
        sqlmap_testpara_banner = "\033[1;32m" + sqlmap_testpara_command.replace("-p","").strip().strip("\"") + "\033[00m"
    
    if sqlmap_database_command == "":
        sqlmap_database_banner = "Specify the backend database type (if known)"
    else:
        sqlmap_database_banner = "\033[1;32m" + sqlmap_database_command.replace("--dbms=","").strip() + "\033[00m"

    if sqlmap_os_flag == 1:
        sqlmap_os_color = "\033[1;32m"
    else:
        sqlmap_os_color = "\033[00m"
    
    if sqlmap_pwn_flag == 1:
        sqlmap_pwn_color = "\033[1;32m"
    else:
        sqlmap_pwn_color = "\033[00m"
    
    if sqlmap_threads_command == "":
        sqlmap_threads_banner = "Max num of concurrent HTTP request (Default = 1)"
    else:
        sqlmap_threads_banner = "\033[1;32m" + sqlmap_threads_command.replace("--threads=","").strip() + "\033[00m"
    
    if sqlmap_forms_flag == 1:
        sqlmap_forms_color = "\033[1;32m"
    else:
        sqlmap_forms_color = "\033[00m"
    
    if sqlmap_verbose_flag == 1:
        sqlmap_verbose_color = "\033[1;32m"
    else:
        sqlmap_verbose_color = "\033[00m"

    os.system("clear")
    print("""
                             SQL Injection (SQLmap)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Target URL         : \033[1;32m"""+sqlmap_target_banner+"""\033[00m

    2. Level              : """+sqlmap_level_banner+"""
    3. Risk               : """+sqlmap_risk_banner+"""
    4. Tor Proxy          : """+sqlmap_tor_banner+""" 
    5. Enumeration        : \033[1;32m"""+sqlmap_enumerate_banner_main+"""\033[00m
    6. Cookie             : """+sqlmap_cookie_banner+"""
    7. """+sqlmap_rua_color+"""Random User Agent\033[00m  - Use random user agent to add anonymity
    8. Data               : """+sqlmap_data_banner+"""
    9. Testable Parameter : """+sqlmap_testpara_banner+"""
   10. Database           : """+sqlmap_database_banner+"""
   11. """+sqlmap_os_color+"""OS Shell\033[00m           - Prompt for interactive system shell in linux server
   12. """+sqlmap_pwn_color+"""OS Pwn\033[00m             - Prompt for OOB Shell, Meterpreter or VNC
   13. """+sqlmap_forms_color+"""Forms page\033[00m         - Target URL have form's field to test (example: login page)
   14. Threads            : """+sqlmap_threads_banner+"""
   15. """+sqlmap_verbose_color+"""Verbose\033[00m            - Display more information

Command: \033[1;32m"""+sqlmap_final_command+"""\033[00m

   90. Launch Attack
   99. Exit
    """)

def sqlmap_main():
    global sqlmap_enumerate_banner, sqlmap_final_command, sqlmap_target_command, sqlmap_level_command, sqlmap_risk_command, sqlmap_tor_flag, sqlmap_cookie_command, sqlmap_rua_flag
    global sqlmap_data_string_command, sqlmap_testpara_command, sqlmap_os_flag, sqlmap_pwn_flag, sqlmap_database_command, sqlmap_threads_command, sqlmap_forms_flag, sqlmap_verbose_flag
    sqlmap_enumerate_banner = ""
    sqlmap_enumerate_main_command = ""
    sqlmap_target_command = ""
    sqlmap_level_command = ""
    sqlmap_risk_command = ""
    sqlmap_tor_command = ""
    sqlmap_cookie_command = ""
    sqlmap_rua_command = ""
    sqlmap_tor_flag = 0
    sqlmap_rua_flag = 0
    sqlmap_data_string_command = ""
    sqlmap_testpara_command = ""
    sqlmap_os_flag = 0
    sqlmap_pwn_flag = 0
    sqlmap_database_command = ""
    sqlmap_os_command = ""
    sqlmap_pwn_command = ""
    sqlmap_threads_command = ""
    sqlmap_forms_flag = 0
    sqlmap_forms_command = ""
    sqlmap_verbose_flag = 0
    sqlmap_verbose_command = ""

    sqlmap_select = ""
    while sqlmap_select != "99":
        #initialize filename save command
        sqlmap_save_command = ""
        #share variable for banner()
        sqlmap_final_command = "sqlmap " + sqlmap_target_command + sqlmap_forms_command + sqlmap_level_command + sqlmap_risk_command + sqlmap_cookie_command + sqlmap_database_command + sqlmap_data_string_command + sqlmap_testpara_command 
        sqlmap_final_command += sqlmap_enumerate_main_command + sqlmap_os_command + sqlmap_pwn_command +sqlmap_tor_command + sqlmap_rua_command + sqlmap_threads_command + sqlmap_verbose_command + "--batch"
        sqlmap_banner()
        sqlmap_select = input("\nSelect: ")
        #target
        if sqlmap_select == "1":
            sqlmap_target = input("\nTarget URL (eg. http://abc.com or https://abc.com): ").strip()
            if sqlmap_target == "" or " " in sqlmap_target:
                sqlmap_target_command = ""
                sqlmap_target = ""
                print("\n[*] Field is empty / Contain spaces!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_target_command = "-u \"" + sqlmap_target + "\" "
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
            sqlmap_level_command = "--level=" + sqlmap_level + " "
        #risk
        elif sqlmap_select == "3":
            sqlmap_risk = input("\nRisk (Range: 1~3, Higher Risk will consume more time): ").strip()
            if sqlmap_risk == "" or " " in sqlmap_risk:
                sqlmap_risk = ""
                sqlmap_risk_command = ""
                print("\n[*] Field is empty / Contain spaces!")
                useless = input("Enter any key to continue......")
                continue
            #validate if it is valid range 1-3
            try:
                sqlmap_risk_validate = int(sqlmap_risk)
                if sqlmap_risk_validate < 1 or sqlmap_risk_validate > 3:
                    raise ValueError
            except ValueError:
                print("\n[*] Error Risk Range!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_risk_command = "--risk=" + sqlmap_risk + " "
        #tor proxy
        elif sqlmap_select == "4":
            if tor.check_init() == 1:
                if sqlmap_tor_flag != 1:
                    sqlmap_tor_flag = 1
                    sqlmap_tor_command = "--proxy=\"socks5://127.0.0.1:9050\" --check-tor "
                else:
                    sqlmap_tor_flag = 0
                    sqlmap_tor_command = ""
            else:
                sqlmap_tor_flag = 0
                sqlmap_tor_command = ""
                print("\n[*] Tor is not running! Please activate Tor at main menu.")
                useless = input("Enter any key to continue......")
                continue
        #enumerate section
        elif sqlmap_select == "5":
            sqlmap_enumerate_main_command = sqlmap_enumerate_sub()
            sqlmap_enumerate_banner = sqlmap_enumerate_main_command.replace("--","").strip().replace(" ",",")
        #cookie
        elif sqlmap_select == "6":
            sqlmap_cookie = input("\nCookie (use ; as seperator for multiple cookie. Eg. cookie1=xx;cookie2=xx): ").strip()
            if sqlmap_cookie == "" or " " in sqlmap_cookie:
                sqlmap_cookie = ""
                sqlmap_cookie_command = ""
                print("\n[*] Field is empty / Contain spaces!")
                useless = input("Enter any key to continue......")
                continue
            if "=" not in sqlmap_cookie:
                sqlmap_cookie = ""
                sqlmap_cookie_command = ""
                print("\n[*] Error format! No \"=\" used.")
                useless = input("Enter any key to continue......")
                continue
            #check format for multiple value
            if sqlmap_cookie.count("=") > 1:
                if sqlmap_cookie.count(";") == 0:
                    sqlmap_cookie = ""
                    sqlmap_cookie_command = ""
                    print("\n[*] Error format! Use ; to seperate multiple cookies.")
                    useless = input("Enter any key to continue......")
                    continue
                if sqlmap_cookie.count(";") == sqlmap_cookie.count("=") or sqlmap_cookie.count(";") == (sqlmap_cookie.count("=") - 1):
                    pass
                else:
                    sqlmap_cookie = ""
                    sqlmap_cookie_command = ""
                    print("\n[*] Error format! Use ; to seperate multiple cookies.")
                    useless = input("Enter any key to continue......")
                    continue
            #check format 
            sqlmap_cookie_command = "--cookie=\"" + sqlmap_cookie + "\" "
        #rua
        elif sqlmap_select == "7":
            if sqlmap_rua_flag != 1:
                sqlmap_rua_flag = 1
                sqlmap_rua_command = "--random-agent "
            else:
                sqlmap_rua_flag = 0
                sqlmap_rua_command = ""
        #data strings
        elif sqlmap_select == "8":
            sqlmap_data_string = input("\nData string (Eg. username=admin&password=abc): ").strip()
            if sqlmap_data_string == "" or " " in sqlmap_data_string:
                sqlmap_data_string = ""
                sqlmap_data_string_command = ""
                print("\n[*] Field is empty / Contain spaces!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_data_string_command = "--data=\"" + sqlmap_data_string + "\" "
        #testable parameter
        elif sqlmap_select == "9":
            sqlmap_testpara = input("\nTestable Parameter (use , as seperator for multiple parameters): ").strip()
            if sqlmap_testpara == "" or " " in sqlmap_testpara:
                sqlmap_testpara = ""
                sqlmap_testpara_command = ""
                print("\n[*] Field is empty / Contain spaces!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_testpara_command = "-p \"" + sqlmap_testpara + "\" "
        #database type
        elif sqlmap_select == "10":
            sqlmap_database = input("\nDatabase: ").strip()
            if sqlmap_database == "" or " " in sqlmap_database:
                sqlmap_database = ""
                sqlmap_database_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_database_command = "--dbms=" + sqlmap_database + " "
        #os shell
        elif sqlmap_select == "11":
            if sqlmap_os_flag != 1:
                sqlmap_os_flag = 1
                sqlmap_os_command = "--os-shell "
                sqlmap_pwn_flag = 0
                sqlmap_pwn_command = ""
            else:
                sqlmap_os_flag = 0
                sqlmap_os_command = ""
        #os cmd
        elif sqlmap_select == "12":
            if sqlmap_pwn_flag != 1:
                sqlmap_pwn_flag = 1
                sqlmap_pwn_command = "--os-pwn "
                sqlmap_os_flag = 0
                sqlmap_os_command = ""
            else:
                sqlmap_pwn_flag = 0
                sqlmap_pwn_command = ""
        #forms
        elif sqlmap_select == "13":
            if sqlmap_forms_flag != 1:
                sqlmap_forms_flag = 1
                sqlmap_forms_command = "--forms "
            else:
                sqlmap_forms_flag = 0
                sqlmap_forms_command = ""
        #threads
        elif sqlmap_select == "14":
            sqlmap_threads = input("\nThreads (1~5): ").strip()
            if sqlmap_threads == "" or " " in sqlmap_threads:
                sqlmap_threads = ""
                sqlmap_threads_command = ""
                print("\n[*] Field is empty / contain space!")
                useless = input("Enter any key to continue......")
                continue
            #validate number range
            try:
                sqlmap_threads_val = int(sqlmap_threads)
                if sqlmap_threads_val < 1 or sqlmap_threads_val > 5:
                    raise ValueError
            except ValueError:
                sqlmap_threads = ""
                sqlmap_threads_command = ""
                print("\n[*] Enter numbers from 1 to 5 only!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_threads_command = "--threads=" + sqlmap_threads + " "
        #verbose
        elif sqlmap_select == "15":
            if sqlmap_verbose_flag != 1:
                sqlmap_verbose_flag = 1
                sqlmap_verbose_command = "-v "
            else:
                sqlmap_verbose_flag = 0
                sqlmap_verbose_command = ""
        #launch attack
        elif sqlmap_select == "90":
            if sqlmap_target_command == "":
                print("\n[*] Target is empty!")
                useless = input("Enter any key to continue......")
                continue
            sqlmap_launch_command = sqlmap_final_command.strip()
            sqlmap_save_prompt = input("\nDo you want to save the result to a file? (y/n): ").strip()
            if sqlmap_save_prompt == "y" or sqlmap_save_prompt == "Y":
                sqlmap_save_filename = input("Enter a new filename: ").strip()
                if sqlmap_save_filename == "":
                    print("\n[*] Filename is empty!")
                    useless = input("Enter any key to continue......")
                    continue
                sqlmap_save_filename = sqlmap_save_filename.replace(" ","_")
                sqlmap_save_command = " --output-dir=\"" + os.getcwd() + "/result/" + sqlmap_save_filename + "\""
            print("\033[1;32m[+] Starting SQLmap......\033[00m")
            os.system(sqlmap_launch_command+sqlmap_save_command)
            if sqlmap_save_command != "":
                print("\033[1;32m[+] File saved to {}\033[00m".format(sqlmap_save_command.replace("--output-dir=","").strip().strip("\"")))
            useless = input("[*] Process Completed! Enter any key to continue......")


def main():
    print("\033[1;32m[+] Loading SQLmap Module\033[00m")
    if sqlmap_self_check() == 1:
        sqlmap_main()
    else:
        print("\n\033[1;31m[-] SQLmap is not installed!\033[00m")
        useless = input("Enter any key to continue......")