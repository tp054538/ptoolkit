from queue import Queue
import subprocess
import multiprocessing
import time

#need to add !!apt update!! to get latest packages
#namexxx_ss variable can find "upgradable"
def tor_check(q):
    tor_s = subprocess.run("apt list 2>/dev/null | grep -E '^tor/'", shell=True, stdout=subprocess.PIPE)
    tor_ss = tor_s.stdout.decode('ascii') #this variable is to find "upgradable" word in another script to determine updates
    if("installed" in tor_ss):
        tor_checkr = "Tor Installed"
    elif("upgradable" in tor_ss):
        tor_checkr = "Tor Upgradeable"
    else:
        tor_checkr = "Tor Not Installed"
    print("Tor Done")
    return q.put(tor_checkr)

def nmap_check(q):
    nmap_s = subprocess.run("apt list 2>/dev/null | grep -E '^nmap/'", shell=True, stdout=subprocess.PIPE)
    nmap_ss = nmap_s.stdout.decode('ascii') #this variable is to find "upgradable" word in another script to determine updates
    if("installed" in nmap_ss):
        nmap_checkr = "Nmap Installed"
    elif("upgradable" in nmap_ss):
        nmap_checkr = "Nmap Upgradeable"
    else:
        nmap_checkr = "Nmap Not Installed"
    print("Nmap Done")
    return q.put(nmap_checkr)

def sqlmap_check(q):
    sqlmap_s = subprocess.run("apt list 2>/dev/null | grep -E '^sqlmap/'", shell=True, stdout=subprocess.PIPE)
    sqlmap_ss = sqlmap_s.stdout.decode('ascii')
    if("installed" in sqlmap_ss):
        sqlmap_checkr = "SQLmap Installed"
    elif("upgradable" in sqlmap_ss):
        sqlmap_checkr = "SQLmap Upgradeable"
    else:
        sqlmap_checkr = "SQLmap Not Installed"
    print("SQLmap Done")
    return q.put(sqlmap_checkr)

def searchsploit_check(q):
    ssploit_s = subprocess.run("apt list 2>/dev/null | grep -E '^exploitdb/'", shell=True, stdout=subprocess.PIPE) #exploitdb is searchsploit, exploitdb-papers for scripts
    ssploit_ss = ssploit_s.stdout.decode('ascii')
    if("installed" in ssploit_ss):
        ssploit_checkr = "SearchSploit Installed"
    elif("upgradable" in ssploit_ss):
        ssploit_checkr = "SearchSploit Upgradeable"
    else:
        ssploit_checkr = "SerchSploit Not Installed"
    print("Searchsploit Done")
    return q.put(ssploit_checkr)

def wpscan_check(q):
    wpscan_s = subprocess.run("apt list 2>/dev/null | grep -E '^wpscan/'", shell=True, stdout=subprocess.PIPE)
    wpscan_ss = wpscan_s.stdout.decode('ascii')
    if("installed" in wpscan_ss):
        wpscan_checkr = "WPscan Installed"
    elif("upgradable" in wpscan_ss):
        wpscan_checkr = "WPscan Upgradeable"
    else:
        wpscan_checkr = "WPscan Not Installed"
    print("WPscan Done")
    return q.put(wpscan_checkr)

def joomscan_check(q):
    joomscan_s = subprocess.run("apt list 2>/dev/null | grep -E '^joomscan/'", shell=True, stdout=subprocess.PIPE)
    joomscan_ss = joomscan_s.stdout.decode('ascii')
    if("installed" in joomscan_ss):
        joomscan_checkr = "JoomScan Installed"
    elif("upgradable" in joomscan_ss):
        joomscan_checkr = "JoomScan Upgradeable"
    else:
        joomscan_checkr = "JoomScan Not Installed"
    print("JoomScan Done")
    return q.put(joomscan_checkr)

def nikto_check(q):
    nikto_s = subprocess.run("apt list 2>/dev/null | grep -E '^nikto/'", shell=True, stdout=subprocess.PIPE)
    nikto_ss = nikto_s.stdout.decode('ascii')
    if("installed" in nikto_ss):
        nikto_checkr = "Nikto Installed"
    elif("upgradable" in nikto_ss):
        nikto_checkr = "Nikto Upgradeable"
    else:
        nikto_checkr = "Nikto Not Installed"
    print("Nikto Done")
    return q.put(nikto_checkr)

def gobuster_check(q):
    gobuster_s = subprocess.run("apt list 2>/dev/null | grep -E '^gobuster/'", shell=True, stdout=subprocess.PIPE)
    gobuster_ss = gobuster_s.stdout.decode('ascii')
    if("installed" in gobuster_ss):
        gobuster_checkr = "GoBuster Installed"
    elif("upgradable" in gobuster_ss):
        gobuster_checkr = "GoBuster Upgradeable"
    else:
        gobuster_checkr = "GoBuster Not Installed"
    print("GoBuster Done")
    return q.put(gobuster_checkr)

def hydra_check(q):
    hydra_s = subprocess.run("apt list 2>/dev/null | grep -E '^hydra/'", shell=True, stdout=subprocess.PIPE)
    hydra_ss = hydra_s.stdout.decode('ascii')
    if("installed" in hydra_ss):
        hydra_checkr = "Hydra Installed"
    elif("upgradable" in hydra_ss):
        hydra_checkr = "Hydra Upgradeable"
    else:
        hydra_checkr = "Hydra Not Installed"
    print("Hydra Done")
    return q.put(hydra_checkr)

def john_check(q):
    john_s = subprocess.run("apt list 2>/dev/null | grep -E '^john/'", shell=True, stdout=subprocess.PIPE)
    john_ss = john_s.stdout.decode('ascii')
    if("installed" in john_ss):
        john_checkr = "JohnTheRipper Installed"
    elif("upgradable" in john_ss):
        john_checkr = "JohnTheRipper Upgradeable"
    else:
        john_checkr = "JohnTheRipper Not Installed"
    print("JohnTheRipper Done")
    return q.put(john_checkr)

def ettercap_check(q):
    ettercap_s = subprocess.run("apt list 2>/dev/null | grep -E '^ettercap-common/'", shell=True, stdout=subprocess.PIPE)
    ettercap_ss = ettercap_s.stdout.decode('ascii')
    if("installed" in ettercap_ss):
        ettercap_checkr = "Ettercap Installed"
    elif("upgradable" in ettercap_ss):
        ettercap_checkr = "Ettercap Upgradeable"
    else:
        ettercap_checkr = "Ettercap Not Installed"
    print("Ettercap Done")
    return q.put(ettercap_checkr)

def set_check(q):
    set_s = subprocess.run("apt list 2>/dev/null | grep -E '^set/'", shell=True, stdout=subprocess.PIPE)
    set_ss = set_s.stdout.decode('ascii')
    if("installed" in set_ss):
        set_checkr = "SEToolkit Installed"
    elif("upgradable" in set_ss):
        set_checkr = "SEToolkit Upgradeable"
    else:
        set_checkr = "SEToolkit Not Installed"
    print("SEToolkit Done")
    return q.put(set_checkr)

def msfvenom_check(q):
    msf_s = subprocess.run("apt list 2>/dev/null | grep -E '^metasploit-framework/'", shell=True, stdout=subprocess.PIPE)
    msf_ss = msf_s.stdout.decode('ascii')
    if("installed" in msf_ss):
        msf_checkr = "Metasploit Installed"
    elif("upgradable" in msf_ss):
        msf_checkr = "Metasploit Upgradeable"
    else:
        msf_checkr = "Metasploit Not Installed"
    print("Metasploit Done")
    return q.put(msf_checkr)
 ###################################################################   

def self_check(): #run all packages check
    print("Starting process to check all packages...")
    q = multiprocessing.Queue()
    
    tor = multiprocessing.Process(target=tor_check, args=(q,))              #use args q for putting into the queue for returning packages status in queue
    nmap = multiprocessing.Process(target=nmap_check, args=(q,))
    sqlmap = multiprocessing.Process(target=sqlmap_check, args=(q,))
    searchsploit = multiprocessing.Process(target=searchsploit_check, args=(q,))
    wpscan = multiprocessing.Process(target=wpscan_check, args=(q,))
    joomscan = multiprocessing.Process(target=joomscan_check, args=(q,))
    nikto = multiprocessing.Process(target=nikto_check, args=(q,))
    gobuster = multiprocessing.Process(target=gobuster_check, args=(q,))
    hydra = multiprocessing.Process(target=hydra_check, args=(q,))
    john = multiprocessing.Process(target=john_check, args=(q,))
    ettercap = multiprocessing.Process(target=ettercap_check, args=(q,))
    set = multiprocessing.Process(target=set_check, args=(q,))
    msfvenom = multiprocessing.Process(target=msfvenom_check, args=(q,))

    tor.start()         # start multiprocessing
    nmap.start()
    sqlmap.start()
    searchsploit.start()
    wpscan.start()
    joomscan.start()
    nikto.start()
    gobuster.start()
    hydra.start()
    john.start()
    ettercap.start()
    set.start()
    msfvenom.start()

    time.sleep(6)
    print("------------------------------")     
    for i in range(q.qsize()):    #qsize() get the Queue size, q.get to retrieve all value in the queue (FIFO)
        print(q.get())    #print this can be used to determine if the package is installed or not

    tor.join()              #join() wait the program to end
    nmap.join()
    sqlmap.join()
    searchsploit.join()
    wpscan.join()
    joomscan.join()
    nikto.join()
    gobuster.join()
    hydra.join()
    john.join()
    ettercap.join()
    set.join()
    msfvenom.join()

self_check() ##to be deleted
