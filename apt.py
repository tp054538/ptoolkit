from queue import Queue
import subprocess
import multiprocessing
import time
#namexxx_ss variable can find "upgradable"
def tor_check(q):
    global tor_check
    tor_s = subprocess.run("apt list 2>/dev/null | grep -E '^tor/'", shell=True, stdout=subprocess.PIPE)
    tor_ss = tor_s.stdout.decode('ascii') #this variable is to find "upgradable" word in another script to determine updates
    if(tor_ss==""):
        tor_check = "Tor Not Installed"
    else:
        tor_check = "Tor Installed"
    print("Tor Done")
    return q.put(tor_check)

def nmap_check(q):
    global nmap_check
    nmap_s = subprocess.run("apt list 2>/dev/null | grep -E '^nmap/'", shell=True, stdout=subprocess.PIPE)
    nmap_ss = nmap_s.stdout.decode('ascii') #this variable is to find "upgradable" word in another script to determine updates
    if(nmap_ss==""):
        nmap_check = "Nmap Not Installed"
    else:
        nmap_check = "Nmap Installed"
    print("Nmap Done")
    return q.put(nmap_check)

def sqlmap_check(q):
    global sqlmap_check
    sqlmap_s = subprocess.run("apt list 2>/dev/null | grep -E '^sqlmap/'", shell=True, stdout=subprocess.PIPE)
    sqlmap_ss = sqlmap_s.stdout.decode('ascii')
    if(sqlmap_ss==""):
        sqlmap_check = "SQLmap Not Installed"
    else:
        sqlmap_check = "SQLmap Installed"
    print("SQLmap Done")
    return q.put(sqlmap_check)

def searchsploit_check(q):
    global searchsploit_check
    ssploit_s = subprocess.run("apt list 2>/dev/null | grep -E '^exploitdb/'", shell=True, stdout=subprocess.PIPE) #exploitdb is searchsploit, exploitdb-papers for scripts
    ssploit_ss = ssploit_s.stdout.decode('ascii')
    if(ssploit_ss==""):
        searchsploit_check = "Searchsploit Not Installed"
    else:
        searchsploit_check = "Searchsploit Installed"
    print("Searchsploit Done")
    return q.put(searchsploit_check)

def wpscan_check(q):
    global wpscan_check
    wpscan_s = subprocess.run("apt list 2>/dev/null | grep -E '^wpscan/'", shell=True, stdout=subprocess.PIPE)
    wpscan_ss = wpscan_s.stdout.decode('ascii')
    if(wpscan_ss==""):
        wpscan_check = "WPscan Not Installed"
    else:
        wpscan_check = "WPscan Installed"
    print("WPscan Done")
    return q.put(wpscan_check)

def self_check(): #run all packages check
    print("Starting process to check all packages...")
    q = multiprocessing.Queue()
    tor = multiprocessing.Process(target=tor_check, args=(q,))              #use args q for putting into the queue for returning packages status in queue
    nmap = multiprocessing.Process(target=nmap_check, args=(q,))
    sqlmap = multiprocessing.Process(target=sqlmap_check, args=(q,))
    searchsploit = multiprocessing.Process(target=searchsploit_check, args=(q,))
    wpscan = multiprocessing.Process(target=wpscan_check, args=(q,))

    tor.start()         # start multiprocessing
    nmap.start()
    sqlmap.start()
    searchsploit.start()
    wpscan.start()

    time.sleep(5)
    print("------------------------------")     
    for i in range(q.qsize()):    #qsize() get the Queue size, q.get to retrieve all value in the queue (FIFO)
        print(q.get())    #print this can be used to determine if the package is installed or not

    tor.join()              #join() wait the program to end
    nmap.join()
    sqlmap.join()
    searchsploit.join()
    wpscan.join()

    #print(q.get())
#    tor = tor_check()
#    nmap = nmap_check()
#    sqlmap = sqlmap_check()
#    searchsploit = searchsploit_check()
#    wpscan = wpscan_check()

self_check() ##to be deleted
