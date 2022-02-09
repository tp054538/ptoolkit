

from importlib.resources import Package

from django.shortcuts import redirect
import PackageCheck#delete

def printMenu(package_status):
    print(package_status)
    green = "\033[1;32m" #green for installed
    red = "\033[1;31m"   #red for not installed

    nmap_status = red

    print("""
                                Install Packages

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    1. """+ nmap_status +"Nmap"+"""
    
    """)

printMenu(PackageCheck.self_check())#delete