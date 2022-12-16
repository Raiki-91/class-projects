"""
Program Name: CIS110 Final01
Program Description: A program which receives as input a single
integer n and produces a n by n times-table as output.
Author Name: Lee Kitchen
Date Created: 12/18/201
Notes: Final Program 01.

"""

import time

def timesTable(j,k):
    n= j*k
    return n

def main():
    i=int(input("enter an integer: "))
    print("  |", end='')
    for i in range(1,i+1):
        print("{:4d}|".format(i), end='')# print for the nth range
    print()
    print("--",end='')
    print("+----"*(i))#line break
    for j in range(1,i+1):# loop left number column
        output_line = "{0:2d}|".format(j)
        for k in range(1,i+1):
           output_line += " {0:3d}|".format(timesTable(j,k))
        print(output_line)
            
    
    #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Program: Final 01")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__ == '__main__':
    main()
