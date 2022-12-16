"""
Program Name: CIS110 Program6
Program Description: Program that checks if a password is valid based on:
at least 8 characters long
at least 1 upper case letter
at least 1 lower case letter
at least 1 digit
at least 1 of these four special characters: ! @ # $

Author Name: Lee Kitchen
Date Created: 10/14/2021
Notes: Uses multi decision making and condtions to verfy a password.

"""

import time
#function for checking if password is valid
def passwordCheck(password):
    length = False
    upper = False
    lower = False
    digit = False
    special = False
    valid = False
    if lengthTest(password) == True:
            length = True
    if upperCaseTest(password) == True:
            upper = True
    if lowerCaseTest(password) == True:
            lower = True
    if digitTest(password) == True:
            digit = True
    if specialCharacterTest(password) == True:
            special = True
    if length and upper and lower and digit and special:
        valid = True
    if valid == True:
        print("Your selected password is valid")
    else:
        print("Your selected password is invalid. Please resubmit")
        
# function for determining if  length is 8 or more.             
def lengthTest(password):
    if len(password) >= 8:
        return True
    else:
        print("the password needs to have at least 8 characters")

# function for determining if there is at least one uppercase letter.       
def upperCaseTest(password):
    for char in password: #loop for checking is letter is uppercase
        if char.isupper():
            return True
    else:
            print("the password should have at least one uppercase letter")
        
def lowerCaseTest(password):
    for char in password: #loop for checking is letter is lowercase
        if char.islower():
            return True
    else:
            print("the password should have at least one lowercase letter")

#function for determining if there is at least one number.
def digitTest(password):
    for char in password: #loop for checking if there is a number.
        if char.isdigit():
          return True
    else:
            print("the password should have at least one number")
#fuction for determinining if there is one or more special charater.
def specialCharacterTest(password):
    for char in password:#loop for checking if thre is one or more special charater.
        if char in "!@#$":
            return True
    else:
            print("the password should have at least one special charater")
            
        

def main():
    password = input("Please enter your password: ")
    passwordCheck(password)
    print()
    print()


    #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Program: Program6")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__ == '__main__':
    main()
