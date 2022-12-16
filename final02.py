"""
Program Name: CIS110 Final02
Program Description: Using a sentinel loop pattern, creates a list of words
entered by a user.    Once they have completed their input, print out the number
of words entered and, for each word, the original word, an uppercase version of the word, and the
last letter of the word (all on one line).
Author Name: Lee Kitchen
Date Created: 12/18/2021

"""

import time
def main():
    count = 0
    words = [ ]
    xStr = input("Enter a word (<Enter> to quit) >> ")
    while xStr != "":
        words += xStr.split(' ')
        count = count + 1
        xStr = input("Enter a word (<Enter> to quit) >> ")
    print()   
    print( count,"words were entered")
    for i in range(len(words)):
        print(words[i], end=' ')
        print(words[i].upper(),end=' ')
        last= words[i][-1:]
        print(last)
        
    #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Program: Final02")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__ == '__main__':
    main()
