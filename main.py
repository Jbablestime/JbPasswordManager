from colorama import *
import os
from os import system
import json
import time

# Start up
system('title Password Manager')

# System
def readPass():
    with open('passwords.json', 'r') as file:
        content = file.read()

    password = json.loads(content)
    return password

def writePass(content):
    with open('passwords.json', 'w') as f:
        json.dump(content, f, indent=4)


# Variables

lightblue = Fore.LIGHTBLUE_EX
red = Fore.RED
green = Fore.GREEN
white = Fore.RESET
password = readPass()

# Code

def set_information():
    os.system('cls')

    print("What would you like to change?")
    new_information = str.lower(input("Choose Platform >>> "))
    new_email = input("New Email >>> ")
    new_password = input("New Password >>> ")

    password["passwords"][f"{new_information}"]["email"] = new_email
    password["passwords"][f"{new_information}"]["password"] = new_password
    writePass(password)

    print(green + f"New Email: {new_email}\nNew Password: {new_password}" + white)

    os.system('pause')
    main_menu()

def view_information():
    os.system('cls')

    print("What would you like to see?")
    information = str.lower(input("Choose Platform >>> "))

    print("Email: " + green + password["passwords"][f"{information}"]["email"] + white)
    print("Password: " + green + password["passwords"][f"{information}"]["password"] + white)

    os.system('pause')
    main_menu()

def main_menu():
    os.system('cls')

    print("Welcome to Password Manager, what would you like to do?")
    print("Current Commands: View, Set")
    option = str.lower(input("Option >>> "))

    if option == "view":
        view_information()
    elif option == "set":
        set_information()

def auth():
    os.system('cls')

    if password["system"]["first_startup"] == True:
        print("Please set a numerical authorization code.")
        new_code = int(input("New Code >>> "))

        password["system"]["access_code"] = new_code
        password["system"]["first_startup"] = False
        writePass(password)
        main_menu()

    else:

        print("Please enter your authorization code.")
        code = int(input("Code >>>"))

        if code == password["system"]["access_code"]:
            print(green + "Access Granted" + white)
            time.sleep(1)
            main_menu()

        elif code != password["system"]["access_code"]:
            print(red + "Access Denied" + white)
            time.sleep(1)
            auth()



# Start Up
auth()