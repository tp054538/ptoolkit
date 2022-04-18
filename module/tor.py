#Written By: Foong Yew Joe (TP054538)
#Description: Start Tor in background / Stop Tor
#First Written Date: 24 February 2022
#Last Edited: 18 April 2022

import os 
import subprocess
import time
from PackageCheck import prGreen, prRed

def check_init(): #initialize tor state during main program start up
    tor_flag = 0 
    a = subprocess.run("service tor status | head -3 | tail -1", shell=True, stdout=subprocess.PIPE)
    b = a.stdout.decode('ascii')
    if "Active: active" in b:
        tor_flag = 1
    else:
        tor_flag = 0
    return tor_flag

def main():
    global tor_flag
    if check_init() == 0:
        prGreen("[+] Loading Tor Module")
        tor_1 = subprocess.run("apt list 2>/dev/null | grep -E '^tor/'", shell=True, stdout=subprocess.PIPE)
        tor_2 = tor_1.stdout.decode('ascii')
        if "installed" in tor_2:
            os.system("sudo service tor start")
            a = subprocess.run("service tor status | head -3 | tail -1", shell=True, stdout=subprocess.PIPE)
            b = a.stdout.decode('ascii')
            if "Active: active" in b:
                prGreen("[+] Tor is running.")
                tor_flag = 1
                time.sleep(2)
        else:
            prRed("\n[+] Tor is not installed! Please install Tor before accessing this page.")
            useless = input("Enter any Key to continue......")
    else:
        os.system("sudo service tor stop")

