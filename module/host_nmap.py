import os

def banner():
    print("""
                            Host Discovery Menu (Nmap)

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. Vulnerability Search (Searchsploit)   2. OSINT/Recon (Sn1per)                

   99. Exit
    """)

def main():
    host_nmap_select = ""
    while host_nmap_select != "99":
        banner()
        host_nmap_select = input("\nSelect: ")
