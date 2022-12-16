"""
Program Name: CIS110 Program9
Program Description: This is a program that generates random powerball numbers with no repeates.
Author Name: Lee Kitchen
Date Created: 11/12/21
Notes: Uses the random libary to genertate psudorandom numbers.


"""

import time
import random 

def printIntro():#Prints intro
    print("This program generates powerball numbers where the first 5 numbers")
    print("are 1-69 with no repeat and the 6th number is 1-26.\n")
          

def howManydraws():#determines how many 6 number draws to do.
   return int(input("How many draws would you like ?: "))
    
def firstFive():# generates the psudeo random 5 numbers 1-69.
    for i in range(1,6):
        n= random.randrange(1,70)
        if n == random.randrange(1,70):
            n=random.randrange(1,70)
            print(n,end=' ')
        else:
            print(n,end=' ')
def sixth():#generates 6th psudeo random number 1-26.
     n= random.randrange(1,27)
     print(n)
    
def genNum(d):#loop for nth draws 
    for i in range(d):
        firstFive()
        sixth()
        print()

def main():
    random.seed(123456)
    printIntro()
    d= howManydraws()
    genNum(d)
    
   
    
    #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Program: Program9")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__== '__main__':
    main()

