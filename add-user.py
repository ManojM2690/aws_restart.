import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter thename of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)

new_user()