import os

def install_or_remove_packages():
    iOrR = ""
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()
    if iOrR == "I":
        iOrR = "install"
    elif iOrR == "R":
        iOrR = "remove"
        
    print("Enter a list of packages to " + iOrR)
    print("The list should be separated by spaces, for example:")
    print(" package1 package2 package3")
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program")
    packages = input().lower()
    defaultPackages = "package1 package2 package3"
    if packages == "default":
        packages = defaultPackages  
    if iOrR == "install":
        os.system("sudo apt-get install " + packages)
    elif iOrR == "remove":
        while True:
            print("Purge files after removing? (Y/N)")
            choice = input().upper()
            if choice == "Y":
                os.system("sudo apt-get --purge " + iOrR + " " + packages)
                break
            elif choice == "N":
                os.system("sudo apt-get " + iOrR + " " + packages)  
                break
        os.system("sudo apt autoremove")

def clean_environment():
    os.system("sudo apt-get autoremove")
    os.system("sudo apt-get autoclean")
        
def update_environment():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
    os.system("sudo apt-get dist-upgrade")
    
install_or_remove_packages()
