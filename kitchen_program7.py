"""
Program Name: CIS110 Program7
Program Description: This is a program creates a table for windchill index from 0-50 mph
and -20 to 60 degrees.
Author Name: Lee Kitchen
Date Created: 10/19/2021
Notes: Uses 35.74 + 0.6215*t - 35.75*math.pow(v, 0.16) + 0.4275*t*math.pow(v, 0.16) to calculate windchil


"""

import time
import math
#function for calulating windchil index
def windChill(t, v):
    while v >=3:#while to check if windspeed is more the or equal to 3 mph
        #windchill equation
        wc = 35.74 + 0.6215*t - 35.75*math.pow(v, 0.16) + 0.4275*t*math.pow(v, 0.16)
        return wc
    else:
        wc = t
        return wc
    
def main():
    print("                               Temperature")# table header
    print("MPH|", end=' ')#left colum header
    for i in range(-20, 70, 10):# loop for temp range
        print("{:6.0f} ".format(i), end='')#space formatting for temprange
    print()
    print("---+" + "-" * 67)#line break
    for v in range(0, 55, 5):# loop for  windspeed 
        output_line = "{0:3.0f}|".format(v)#formatting for windspeed
        for t in range(-20, 70, 10):#loop for temps
            output_line += " {0:6.0f}".format(windChill(t, v))#formating for printing table
        print(output_line)#printed table of values
   
    print()
   #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Program: Program7")
   #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
if __name__ == '__main__':
    main()
