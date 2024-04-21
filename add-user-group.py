import subprocess
import os

def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0].decode()
    print("Enter a list of groups to add the user to.")
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output)
    chosenGroups = input("Groups: ")

    output = output.split()
    chosenGroups = chosenGroups.split()
    print("Add To:")
    found = False
    groupString = ""
    
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print("-Existing Group: " + grp)
                groupString = groupString + grp + ","
                break
        if not found:
            print("-New Group: " + grp)
            groupString = groupString + grp + ","
        found = False

    groupString = groupString[:-1]
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input("Add user '" + username + "' to these groups? (Y/N)").upper()
    if confirm == "N":
        print("User '" + username + "' not added")
    elif confirm == "Y":
        os.system("sudo usermod -aG " + groupString + " " + username)
        print("User '" + username + "' added.")

add_user_to_group()
