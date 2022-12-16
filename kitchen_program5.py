"""
Program Name: CIS110 Program5
Program Description: This is a program that sums and squares nth numbers in a given list.
Author Name: Lee Kitchen
Date Created: 8/05/2021
Notes: Uses list mutablibity to change values.


"""
#imports time libary
import time
#function that sums the list of nth numbers
def sumList(nums):
    total = 0
    for num in nums: #accumulator loop for summing nth list
        total = total + num
    return total
#function that square each index in the give list
def squareEach(nums):
   for num in range(len(nums)): #loop for squaring nums in list
       nums[num] = nums[num] * nums[num] 
#main function 
def main():
    #user input for nth number list
    nth = int(input("Give a length of a list of numbers to sum: "))
    #blank space formmating
    print()
    #expression for generating nth number list
    nums = list(range( 1, nth +1 ))
    #print nth list
    print(nums)
    #print sum of orginal nth list
    print("The sum of the natual number of nth list is %d.\n" % sumList(nums))
    #function to square and replace the orginal nth list
    squareEach(nums)
    #print the new squared nth list
    print(nums)
    #print the sum of the nth squared list
    print("The sum of the squared numbers of nth list is %d.\n" % sumList(nums))
   
    
    #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Program: Program5")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
#exception for running main function 
if __name__ == '__main__':
    main()
