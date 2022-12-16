"""
Program Name: CIS110 Program4
Program Description: This is a program creates a circular Caesar cipher from the user input message .
Author Name: Lee Kitchen
Date Created: 9/26/2021
Notes: Uses modular math to create a cicular funtion.


"""

import time
def main():
    #prints intro statement
    print("This program creates a caesar cipher based on a phrase and key you enter.\n")
    #user input for key length
    key = int(input("enter a key value: "))
    #user input for phrase
    phrase = input("Enter a phrase to encode : ")
    #joins strings removing the spaces
    phrase = ''.join(phrase.split()).lower()
    #setting blank starting points for variables
    cipher = ""
    decrypt = ""
    #loop for creating the circular cipher
    for character in phrase:
        cipher = cipher + chr((ord(character)+ key - ord('a'))% 26 + ord('a'))
   #loop for decrypting cipher
    for character in cipher:
        decrypt = decrypt + chr((ord(character) - key - ord('a'))% 26 + ord('a'))
    #Print orginal phrase
    print("Orginal phrase: ",phrase)
    #Print the ciphered phrase
    print("Cihper: ", cipher)
    #Print the decrypted phrase
    print("Decrpted: ",decrypt,"\n")

    
    #Prints Author's name, class and date
    print("Lee Kitchen\n")
    print ("Class: CIS110", "Program: Program4\n")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
    
main()
