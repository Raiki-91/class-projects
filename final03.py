"""
Program Name: CIS110 Program Template
Program Description: program to play the guessing game.
Your program will randomly choose a number between 1 and 50.
You then prompt the user for a guess.
If they guess correctly, congratulate them and exit. 
Author Name: Lee Kitchen
Date Created: 8/31/201
Notes: Uses the pythontime libary.


"""

import time
import random
def main():
    n= random.randrange(1,51)
    x= int(input("Welcome. What is your guess? "))
    while x !=n:
        if x >n:
            x= int(input("Lower. What is your guess? "))
        elif x < n:
            x= int(input("Higher. What is your guess? "))
        else:
            break
    print("Correct!")
        
            
            
    #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Final03")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__ == '__main__':
    main()
