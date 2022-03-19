import os
import subprocess
from module import sniper_scan
from module import tor
from module.hydra import hydra_password_provided_wordlist

def wpscan_self_check():
    print("\033[1;32m[+] Loading WpScan Module.\033[00m")
    wpscan_status_check = subprocess.run("apt list 2>/dev/null | grep -E '^wpscan/'", shell=True, stdout=subprocess.PIPE)
    wpscan_status_checkd = wpscan_status_check.stdout.decode('ascii')
    if "installed" in wpscan_status_checkd or "upgradable" in wpscan_status_checkd:
        return 1
    else:
        return 0

#make sure uri start from /
def wp_validate_uri(uri):
    if uri[0] != "/":
        return 0
    else:
        return 1
#make sure no space in directory name
def wp_validate_dir(dir):
    dir = dir.strip()
    dir_list = dir.split(" ")
    if len(dir_list) > 1:
        return 0
    else:
        return 1

#process all value and add colour for wpscan_banner()
def wpscan_banner_value_color():
    global wp_url_banner, wp_uri_banner, wp_password_banner, wp_username_banner, wp_content_dir_banner, wp_plugin_dir_banner, wp_enumerate_banner, wp_rua_color, wp_force_color, wp_stealthy_color, wp_aggr_color
    global wp_default_color, wp_cookie_banner, wp_verbose_color, wp_threads_banner, wp_proxy_color
    if wpscan_url != "":
        wp_url_banner = "\033[1;32m" + wpscan_url + "\033[00m"
    else:
        wp_url_banner = ""
    
    if wpscan_uri != "":
        wp_uri_banner = "\033[1;32m" + wpscan_uri + "\033[00m"
    else:
        wp_uri_banner = "Specify login page if it is different from /wp-login.php"
    
    if wpscan_password != "":
        wp_password_banner = "\033[1;32m" + wpscan_password + "\033[00m"
    else:
        wp_password_banner = "Specify the password file's path"

    if wpscan_username != "":
        wp_username_banner = "\033[1;32m" + wpscan_username + "\033[00m"
    else:
        wp_username_banner = "Specify the username value. Not specified -> retrieve from user enumeration"
    
    if wpscan_content_dir != "":
        wp_content_dir_banner = "\033[1;32m" + wpscan_content_dir + "\033[00m"
    else:
        wp_content_dir_banner = "Specify wp-content directory if not detected in scan"
    
    if wpscan_plugin_dir != "":
        wp_plugin_dir_banner = "\033[1;32m" + wpscan_plugin_dir + "\033[00m"
    else:
        wp_plugin_dir_banner = "Specify plugins directory if not detected in scan"

    if wp_enumerate_command == "-e ":
        wp_enumerate_banner = "\033[1;32m" + "vp,vt,tt,cb,dbe,u,m" + "\033[00m"
    elif wp_enumerate_command != "":
        wp_enumerate_banner = "\033[1;32m" + wp_enumerate_command.strip("-e ") + "\033[00m"
    else:
        wp_enumerate_banner = "Specify enumeration type (When this mode is selected)"
    
    if wpscan_rua_flag == 1:
        wp_rua_color = "\033[1;32m"
    else:
        wp_rua_color = "\033[00m"
    
    if wpscan_force_flag == 1:
        wp_force_color = "\033[1;32m"
    else:
        wp_force_color = "\033[00m"

    if wpscan_stealthy_flag == 1:
        wp_stealthy_color = "\033[1;32m"
    else:
        wp_stealthy_color = "\033[00m"
    
    if wpscan_aggr_flag == 1:
        wp_aggr_color = "\033[1;32m"
    else:
        wp_aggr_color = "\033[00m"
    
    if wpscan_default_flag == 1:
        wp_default_color = "\033[1;32m"
    else:
        wp_default_color = "\033[00m"
    
    if wpscan_cookie != "":
        wp_cookie_banner = "\033[1;32m" + wpscan_cookie + "\033[00m"
    else:
        wp_cookie_banner = "Specify cookie strings in requests. Format: COOKIE=abc123"
    
    if wpscan_verbose_flag == 1:
        wp_verbose_color = "\033[1;32m"
    else:
        wp_verbose_color = "\033[00m"

    if wpscan_threads == 0 or wpscan_threads < 0:
        wp_threads_banner = "\033[1;32m5 (Default)\033[00m"
    else:
        wp_threads_banner = "\033[1;32m" + str(wpscan_threads) + "\033[00m"
    
    if wpscan_proxy == 1:
        wp_proxy_color = "\033[1;32m"
    else:
        wp_proxy_color = "\033[00m"

def wpscan_banner():
    os.system("clear")
    print("""
                          Wordpress Scanner (WPscan)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. URL                  :   """+wp_url_banner+"""

Page locations:
    2. Logni URI            :   """+wp_uri_banner+"""
    3. Wp-content Directory -   """+wp_content_dir_banner+"""
    4. Wp-plugins Directory -   """+wp_plugin_dir_banner+"""

Brute-force:
    5. Password/s           :   """+wp_password_banner+"""
    6. Username/s           :   """+wp_username_banner+"""

Modes:
    7. Enumerate            :   """+wp_enumerate_banner+"""
    8. """+wp_rua_color+"""Random User Agent\033[00m    -   Each scan will use a random user agent
    9. """+wp_force_color+"""Force scan\033[00m           -   Does not check if target is running Wordpress

Scan Modes (Select 1):
   10. """+wp_stealthy_color+"""Stealthy\033[00m             -   Random user agent, passive detection, passive plugins detection
   11. """+wp_aggr_color+"""Aggressive\033[00m           -   Aggressive detection & Aggressive plugins detection
   12. """+wp_default_color+"""Default\033[00m              -   Mixed detection & passive plugins detection

Other:
   13. Cookie               -   """+wp_cookie_banner+"""
   14. """+wp_verbose_color+"""Verbose\033[00m              -   Display more information when scanning
   15. Threads              :   """+wp_threads_banner+"""
   16. """+wp_proxy_color+"""Tor Proxy\033[00m            :   Scan through Tor proxy to hide identity

Command: \033[0;31m"""+wpscan_final_command+"""\033[00m 
   90. Launch Attack
   99. Exit
    """)

#a seperate display for enumeration selection
def wp_enumerate_program():
    #global wp_ap_flag, wp_vp_flag, wp_p_flag, wp_vt_flag, wp_at_flag, wp_tt_flag, wp_t_flag, wp_cb_flag, wp_dbe_flag, wp_u_flag, wp_m_flag
    wp_ap_flag = 0
    wp_vp_flag = 0
    wp_p_flag = 0
    wp_vt_flag = 0
    wp_at_flag = 0
    wp_t_flag = 0
    wp_tt_flag = 0
    wp_cb_flag = 0
    wp_dbe_flag = 0
    wp_u_flag = 0
    wp_m_flag = 0


    wp_enumerate_select = ""
    while wp_enumerate_select != "90":
        if wp_ap_flag == 1:
            wp_ap_color = "\033[1;32m"
        else:
            wp_ap_color = "\033[00m"
        
        if wp_vp_flag == 1:
            wp_vp_color = "\033[1;32m"
        else:
            wp_vp_color = "\033[00m"
        
        if wp_p_flag == 1:
            wp_p_color = "\033[1;32m"
        else:
            wp_p_color = "\033[00m"
        
        if wp_vt_flag == 1:
            wp_vt_color = "\033[1;32m"
        else:
            wp_vt_color = "\033[00m"
        
        if wp_at_flag == 1:
            wp_at_color = "\033[1;32m"
        else:
            wp_at_color = "\033[00m"
        
        if wp_t_flag == 1:
            wp_t_color = "\033[1;32m"
        else:
            wp_t_color = "\033[00m"
        
        if wp_tt_flag == 1:
            wp_tt_color = "\033[1;32m"
        else:
            wp_tt_color = "\033[00m"
        
        if wp_cb_flag == 1:
            wp_cb_color = "\033[1;32m"
        else:
            wp_cb_color = "\033[00m"
        
        if wp_dbe_flag == 1:
            wp_dbe_color = "\033[1;32m"
        else:
            wp_dbe_color = "\033[00m"
        
        if wp_u_flag == 1:
            wp_u_color = "\033[1;32m"
        else:
            wp_u_color = "\033[00m"
        
        if wp_m_flag == 1:
            wp_m_color = "\033[1;32m"
        else:
            wp_m_color = "\033[00m"

        os.system("clear")
        print("""
                        ENUMERATION TARGET SELECTION

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select either 1 or none (1~3)
        1. """+wp_vp_color+"""vp\033[00m           -   Vulnerable Plugins
        2. """+wp_ap_color+"""ap\033[00m           -   All Plugins
        3. """+wp_p_color+"""p\033[00m            -   Popular Plugins
Select either 1 or none (4~6)
        4. """+wp_vt_color+"""vt\033[00m           -   Vulnerable Themes
        5. """+wp_at_color+"""at\033[00m           -   All Themes 
        6. """+wp_t_color+"""t\033[00m            -   Popular Themes
Others
        7. """+wp_tt_color+"""tt\033[00m           -   Timthumbs
        8. """+wp_cb_color+"""cb\033[00m           -   Config Backups
        9. """+wp_dbe_color+"""dbe\033[00m          -   Database Exports
       10. """+wp_u_color+"""u\033[00m            -   User ID range (Default = 1-10)
       11. """+wp_m_color+"""m\033[00m            -   Media ID range (Default = 1-100)
        
       90. Submit""")

        wp_enumerate_select = input("\nSelect: ")
        if wp_enumerate_select == "1":
            if wp_vp_flag != 1:
                wp_vp_flag = 1
                wp_ap_flag = 0
                wp_p_flag = 0
            else:
                wp_vp_flag = 0
        elif wp_enumerate_select == "2":
            if wp_ap_flag != 1:
                wp_vp_flag = 0
                wp_ap_flag = 1
                wp_p_flag = 0
            else:
                wp_ap_flag = 0
        elif wp_enumerate_select == "3":
            if wp_p_flag != 1:
                wp_vp_flag = 0
                wp_ap_flag = 0
                wp_p_flag = 1
            else:
                wp_p_flag = 0
        elif wp_enumerate_select == "4":
            if wp_vt_flag != 1:
                wp_vt_flag = 1
                wp_at_flag = 0
                wp_t_flag = 0
            else:
                wp_vt_flag = 0
        elif wp_enumerate_select == "5":
            if wp_at_flag != 1:
                wp_vt_flag = 0
                wp_at_flag = 1
                wp_t_flag = 0
            else:
                wp_at_flag = 0
        elif wp_enumerate_select == "6":
            if wp_t_flag != 1:
                wp_vt_flag = 0
                wp_at_flag = 0
                wp_t_flag = 1
            else:
                wp_t_flag = 0
        elif wp_enumerate_select == "7":
            if wp_tt_flag != 1:
                wp_tt_flag = 1
            else:
                wp_tt_flag = 0
        elif wp_enumerate_select == "8":
            if wp_cb_flag != 1:
                wp_cb_flag = 1
            else:
                wp_cb_flag = 0
        elif wp_enumerate_select == "9":
            if wp_dbe_flag != 1:
                wp_dbe_flag = 1
            else:
                wp_dbe_flag = 0
        elif wp_enumerate_select == "10":
            if wp_u_flag != 1:
                wp_u_flag = 1
            else:
                wp_u_flag = 0
        elif wp_enumerate_select == "11":
            if wp_m_flag != 1:
                wp_m_flag = 1
            else:
                wp_m_flag = 0
        #return the selected flags
        elif wp_enumerate_select == "90":
            wp_enumerate_temp_command = "-e "
            wp_enumerate_temp_list = []
            if wp_vp_flag == 1:
                wp_enumerate_temp_list.append("vp")
            if wp_ap_flag == 1:
                wp_enumerate_temp_list.append("ap")
            if wp_p_flag == 1:
                wp_enumerate_temp_list.append("p")
            if wp_vt_flag == 1:
                wp_enumerate_temp_list.append("vt")
            if wp_at_flag == 1:
                wp_enumerate_temp_list.append("at")
            if wp_t_flag == 1:
                wp_enumerate_temp_list.append("t")
            if wp_tt_flag == 1:
                wp_enumerate_temp_list.append("tt")
            if wp_cb_flag == 1:
                wp_enumerate_temp_list.append("cb")
            if wp_dbe_flag == 1:
                wp_enumerate_temp_list.append("dbe")
            if wp_u_flag == 1:
                wp_enumerate_temp_list.append("u")
            if wp_m_flag == 1:
                wp_enumerate_temp_list.append("m")
            #join all the selected flags
            if len(wp_enumerate_temp_list) >= 1:
                for i in range(len(wp_enumerate_temp_list)):
                    wp_enumerate_temp_command += wp_enumerate_temp_list[i] + ","
                wp_enumerate_temp_command = wp_enumerate_temp_command.strip(",")
                return wp_enumerate_temp_command
            else:
                return wp_enumerate_temp_command.strip()

def main():
    #check wpscan installed
    if wpscan_self_check() == 1:
        global wpscan_url, wpscan_uri, wpscan_password, wpscan_username, wpscan_content_dir, wpscan_plugin_dir, wp_enumerate_command, wpscan_rua_flag, wpscan_force_flag, wpscan_stealthy_flag, wpscan_aggr_flag
        global wpscan_default_flag, wpscan_cookie, wpscan_verbose_flag, wpscan_threads, wpscan_final_command, wpscan_proxy
        wpscan_url = ""
        wpscan_uri = ""
        wpscan_password = ""
        wpscan_username = ""
        wpscan_content_dir = ""
        wpscan_plugin_dir = ""
        wp_enumerate_select_flag = 0
        wpscan_rua_flag = 0
        wpscan_force_flag = 0
        wpscan_stealthy_flag = 0
        wpscan_aggr_flag = 0
        wpscan_default_flag = 0
        wpscan_cookie = ""
        wpscan_verbose_flag = 0
        wpscan_threads = 0
        wpscan_proxy = 0

        wpscan_url_command = ""
        wpscan_uri_command = ""
        wpscan_password_command = ""
        wpscan_username_command = ""
        wpscan_content_dir_command = ""
        wpscan_plugin_dir_command = ""
        wp_enumerate_command = ""
        wpscan_force_command = ""
        wpscan_rua_command = ""
        wpscan_stealthy_command = ""
        wpscan_aggr_command = ""
        wpscan_cookie_command = ""
        wpscan_verbose_command = ""
        wpscan_threads_command = ""
        wpscan_final_command = ""
        wpscan_proxy_command = ""

        wpscan_select = ""
        #wpscan program loop
        while wpscan_select != "99":
            #generate command
            wpscan_final_command = "wpscan " + wpscan_url_command + wpscan_uri_command + wpscan_content_dir_command + wpscan_plugin_dir_command + wpscan_cookie_command + wp_enumerate_command + wpscan_password_command + wpscan_username_command 
            wpscan_final_command += wpscan_rua_command + wpscan_force_command + wpscan_stealthy_command + wpscan_aggr_command + wpscan_proxy_command + wpscan_threads_command + wpscan_verbose_command
            #main program
            wpscan_banner_value_color()
            wpscan_banner()
            wpscan_select = input("Select: ")
            #url
            if wpscan_select == "1":
                wpscan_url = input("\nURL (https protocol need to be specified. Eg. https://example.com): ").strip()
                if wpscan_url == "" or " " in wpscan_url:
                    wpscan_url_command = ""
                    print("\n[*] URL cannot be empty or contain space between words!")
                    useless = input("Enter any key to continue......")
                    continue
                wpscan_url_command = "--url " + wpscan_url + " "
            #uri
            elif wpscan_select == "2":
                wpscan_uri = input("\nURI: ").strip()
                if wpscan_uri == "" or " " in wpscan_uri:
                    wpscan_uri_command = ""
                    wpscan_uri = ""
                    print("\n[*] URI cannot be empty / contain spaces!")
                    useless = input("Enter any key to continue......")
                    continue
                if wp_validate_uri(wpscan_uri) == 1:
                    wpscan_uri_command = "--login-uri " + wpscan_uri + " "
                else:
                    wpscan_uri = ""
                    wpscan_uri_command = ""
                    print("\n[*] URI format error. Start with \"/\". Eg. /wp-admin.php")
                    useless = input("Enter any key to continue......")
                    continue
            #wp-content directory
            elif wpscan_select == "3":
                wpscan_content_dir = input("\nContent Directory: ").strip()
                if wpscan_content_dir == "":
                    wpscan_content_dir_command = ""
                    print("\n[*] Content directory cannot be empty!")
                    useless = input("Enter any key to continue......")
                    continue
                if wp_validate_dir(wpscan_content_dir) == 1:
                    wpscan_content_dir_command = "--wp-content-dir " + wpscan_content_dir + " "
                else:
                    wpscan_content_dir = ""
                    wpscan_content_dir_command = ""
                    print("\n[*] Content Directory format error. No space is allowed in between characters.")
                    useless = input("Enter any key to continue......")
                    continue
            #wp-plugins directory
            elif wpscan_select == "4":
                wpscan_plugin_dir = input("\nPlugins Directory: ").strip()
                if wpscan_plugin_dir == "":
                    wpscan_plugin_dir_command = ""
                    print("\n[*] Plugins directory cannot be empty!")
                    useless = input("Enter any key to continue......")
                    continue
                if wp_validate_dir(wpscan_plugin_dir) == 1:
                    wpscan_plugin_dir_command = "--wp-plugins-dir " + wpscan_plugin_dir + " "
                else:
                    wpscan_plugin_dir = ""
                    wpscan_plugin_dir_command = ""
                    print("\n[*] Plugins Directory format error. No space is allowed in between characters.")
                    useless = input("Enter any key to continue......")
                    continue
            
            #bruteforce file/value section
            #password
            elif wpscan_select == "5":
                print("\nCurrent Directory = \033[1;32m{}/\033[00m".format(os.getcwd()))
                print("*Type \"\033[1;33mwordlists\033[00m\" to select from provided password wordlists.")
                wpscan_password = input("Password file path: ").strip()
                if wpscan_password == "":
                    wpscan_password_command = ""
                    print("\n[*] Password file path cannot be empty!")
                    useless = input("Enter any key to continue......")
                    continue
                if wpscan_password == "wordlists":
                    wpscan_password = hydra_password_provided_wordlist()
                #check file exist
                if sniper_scan.check_file_exist(wpscan_password) == 0:
                    wpscan_password = ""
                    wpscan_password_command = ""
                    print("\n[*] File does not exist!")
                    useless = input("Enter any key to continue......")
                    continue
                #make file path to full path
                if wpscan_password.startswith("~/") or wpscan_password.startswith("/"):
                    pass
                else:
                    wpscan_password = os.getcwd()+"/"+wpscan_password
                wpscan_password_command = "-P " + wpscan_password + " "
            #username
            elif wpscan_select == "6":
                wpscan_username = input("\nUsername/s (use \",\" as seperator for multiple usernames): ").strip()
                if wpscan_username == "" or " " in wpscan_username:
                    wpscan_username_command = ""
                    wpscan_username = ""
                    print("\n[*] Field cannot be empty / contain space!")
                    useless = input("Enter any key to continue......")
                    continue
                wpscan_username_command = "-U " + wpscan_username + " "
            #enumerate
            #enumerate flag use for deselect
            elif wpscan_select == "7":
                if wp_enumerate_select_flag != 1:
                    wp_enumerate_command = wp_enumerate_program() + " "
                    wp_enumerate_select_flag = 1
                else:
                    wp_enumerate_select_flag = 0
                    wp_enumerate_command = ""
                    continue
            #random user agent
            elif wpscan_select == "8":
                if wpscan_rua_flag != 1:
                    wpscan_rua_flag = 1
                    wpscan_rua_command = "--random-user-agent "
                else:
                    wpscan_rua_flag = 0
                    wpscan_rua_command = ""
            #force
            elif wpscan_select == "9":
                if wpscan_force_flag != 1:
                    wpscan_force_flag = 1
                    wpscan_force_command = "--force "
                else:
                    wpscan_force_flag = 0
                    wpscan_force_command = ""
            #Scan Modes select 1 only
            elif wpscan_select == "10":
                if wpscan_stealthy_flag != 1:
                    wpscan_stealthy_flag = 1
                    wpscan_stealthy_command = "--stealthy "
                    wpscan_aggr_flag = 0
                    wpscan_aggr_command = ""
                    wpscan_default_flag = 0
                else:
                    wpscan_stealthy_flag = 0
                    wpscan_stealthy_command = ""
            elif wpscan_select == "11":
                if wpscan_aggr_flag != 1:
                    wpscan_aggr_flag = 1
                    wpscan_aggr_command = "--plugins-detection aggressive --detection-mode aggressive --plugins-version-detection aggressive "
                    wpscan_stealthy_flag = 0
                    wpscan_stealthy_command = ""
                    wpscan_default_flag = 0
                else:
                    wpscan_aggr_flag = 0
                    wpscan_aggr_command = ""
            elif wpscan_select == "12":
                if wpscan_default_flag != 1:
                    wpscan_default_flag = 1
                    wpscan_aggr_flag = 0
                    wpscan_aggr_command = ""
                    wpscan_stealthy_flag = 0
                    wpscan_stealthy_command = ""
                else:
                    wpscan_default_flag = 0
            #Others
            #Cookie
            elif wpscan_select == "13":
                wpscan_cookie = input("\nCookie (format: cookiename=cookievalue): ").strip()
                if wpscan_cookie == "" or " " in wpscan_cookie:
                    wpscan_cookie = ""
                    wpscan_cookie_command = ""
                    print("\n[*] Field cannot be empty / contain space!")
                    useless = input("Enter any key to continue......")
                    continue
                #validate format
                if "=" not in wpscan_cookie:
                    wpscan_cookie = ""
                    wpscan_cookie_command = ""
                    print("\n[*] Wrong format! No \"=\" detected.")
                    useless = input("Enter any key to continue......")
                    continue
                wpscan_cookie_command = "--cookie-string " + wpscan_cookie + " "
            #Verbose
            elif wpscan_select == "14":
                if wpscan_verbose_flag != 1:
                    wpscan_verbose_flag = 1
                    wpscan_verbose_command = "--verbose "
                else:
                    wpscan_verbose_flag = 0
                    wpscan_verbose_command = ""
            #Threads
            elif wpscan_select == "15":
                wpscan_threads = input("\nThreads: ")
                try:
                    wpscan_threads = int(wpscan_threads.strip())
                    if wpscan_threads < 0:
                        wpscan_threads_command = ""
                        print("\n[*] Threads must be 1 or higher!")
                        useless = input("Enter any key to continue......")
                        continue
                    if wpscan_threads == 0:
                        wpscan_threads_command = ""
                        print("\n[*] Threads cannot be 0!")
                        useless = input("Enter any key to continue......")
                        continue
                    wpscan_threads_command = "-t " + str(wpscan_threads) + " "
                except ValueError:
                    wpscan_threads = 0
                    wpscan_threads_command = ""
                    print("\n[*] Numbers only!")
                    useless = input("Enter any key to continue......")
                    continue
            #proxy
            elif wpscan_select == "16":
                if tor.check_init() == 1:
                    if wpscan_proxy != 1:
                        wpscan_proxy = 1
                        wpscan_proxy_command = "--proxy socks5://127.0.0.1:9050 "
                    else:
                        wpscan_proxy = 0
                        wpscan_proxy_command = ""
                else:
                    wpscan_proxy = 0
                    wpscan_proxy_command = ""
                    print("\n[*]Tor is not running! Activate Tor at main menu before using this option.")
                    useless = input("Enter any key to continue......")
                    continue
            #check target is not empty -> fire attack.
            elif wpscan_select == "90":
                if wpscan_url == "":
                    print("\n[*] No target specified!")
                    useless = input("Enter any key to continue......")
                    continue
                #initialize output state
                wpscan_output_command = ""
                #Prompt for output file y/n and output format
                wpscan_output_tofile = input("\nDo you want to save the result? (y/n): ")
                if wpscan_output_tofile == "y" or wpscan_output_tofile == "Y":
                    wpscan_output_filename = input("\nEnter a new filename: ").strip()
                    if wpscan_output_filename == "":
                        print("\n[*] Error. Filename is empty!")
                        useless = input("Enter any key to continue......")
                        continue
                    wpscan_output_filename = wpscan_output_filename.replace(" ","_")
                    wpscan_output_filepath = os.getcwd() + "/result/" + wpscan_output_filename
                    wpscan_output_command = " -o " + wpscan_output_filepath + " "    
                #launch wpscan
                print("\033[1;32m[+] Starting WpScan......\033[00m")
                os.system(wpscan_final_command.strip()+wpscan_output_command+" --no-update")
                if wpscan_output_command != "":
                    print("\n\033[1;32m[+] Result saved to {}\033[00m".format(wpscan_output_filepath))
                wpscan_output_command = ""
                useless = input("[*] Process Completed. Enter any key to continue......")

    else:
        print("\n\033[1;31m[-] WpScan is not installed!\033[00m")
        useless = input("Enter any key to continue......")
