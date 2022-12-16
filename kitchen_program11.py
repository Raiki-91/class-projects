"""
Program Name: CIS110 Program11
Program Description: This program plays with Stacks!
Last in first out (LIFO) stack implemented using a list.
Author Name: Lee Kitchen
Date Created: 11/28/21
Notes: Uses mutable lists to pop or push items to the list.
"""
def lbreak(): #function for creating a line break for formatting.
    print()
    
class Stack(): #stack class
    
    def __init__(self):#stack class initialize 
        self.items= []
        
    def isEmpty(self): #method to check if the stack is empty
        if self.items == []:
            print("Stack is empty")
        else:
            return self.items == [ ]
        
    def push(self,item):#method to use append to put item in the stack.
         return self.items.append(item)
         
    
    def pop(self):#method for poping last value in the stack
       return self.items.pop()
        
    
    def peek(self):#method check to see what is in the stack with exception if it is empty
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.items
    
    def size(self):#method to check size of the stack
        return len(self.items)
    
        
        
import time
def main():
    print("This program is designed to play with stacks!!")#intro
    print("Stack Operations:")
    

    
    s= Stack()# stack initializer 
    p =[ ]# empty list to hold pop values later
   
    print("To push a value onto the stack type - push<value>")# instruction list
    print("To pop type - pop")
    print("To quit type - quit")
    lbreak()#formatting 
    while True:#while loop to check for push, pop, or quit
    
        do = input('What would you like to do? ').split()
 
        operation = do[0].strip().lower() #indexing first word and making it lowercase
        if operation == 'push': #boolean check for push
                s.push(int(do[1]))#pushing value from do 
                print("the stack contains",s.items,"\n")# printing stack
        elif operation == 'pop':#boolean check for pop
            if s.isEmpty():#exception for checking if stack is empty
                print('Stack is empty.')
            else:
                x= s.pop() #value holde for the pop
                p.append(x)#append to pop list
                print('Popped value: ',x ,"\n",) #popped value
        elif operation == 'quit':#boolean check for quit
            print("Popped values were: ",p)#print statment for popped values in order
            break#ends while loop
    lbreak()
        
            
        
    #Prints Author's name, class and date
    print("Lee Kitchen")
    print ("Class: CIS110", "Program: Program11")
    #this function will print current date and time using asctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__ == '__main__':
    main()
