import subprocess

def self_check(): #check if package is installed
    print("Starting process to check all packages...")
    #nmap
    global nmap_check
    nmap_s = subprocess.run("apt list 2>/dev/null | grep -Eo '^nmap/'", shell=True, stdout=subprocess.PIPE)
    nmap_ss = nmap_s.stdout.decode('ascii')
    if(nmap_ss==""):
        nmap_check = "Not Installed"
    else:
        nmap_check = "Installed"
    print("Nmap Done")

    #SQLmap
    global sqlmap_check
    sqlmap_s = subprocess.run("apt list 2>/dev/null | grep -Eo '^sqlmap/'", shell=True, stdout=subprocess.PIPE)
    sqlmap_ss = sqlmap_s.stdout.decode('ascii')
    #print(sqlmap_ss)
    if(sqlmap_ss==""):
        sqlmap_check = "Not Installed"
    else:
        sqlmap_check = "Installed"
    print("SQLmap Done")

self_check()

print(nmap_check,sqlmap_check)
#apt list 2>/dev/null | grep -Eo '^nmap/'