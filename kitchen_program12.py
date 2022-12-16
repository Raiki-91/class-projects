"""
Program Name: CIS110 Program12
Program Description: Uses class BankAccount class to simulate deposits,
current balances and print checks.
Author Name: Lee Kitchen
Date Created: 12/06/2021
Notes: Uses subclasses to simulate checking and savings.


"""

import time

class BankAccount():
    balance= 0
    

    def __init__(self,label):#constructor for labeling an account
       self.label = label
       
    def withdraw(self, amount):# method for withdrawing money from account
        if amount >self.balance:# if statement to prompt error if  amount is more than in the account.
            print("${0:.2f} is an invaild withdrawl amount it exceeds ${1:.2f}".format(amount, self.balance))
        else:
            self.balance -= amount
            print("Withdrawing ${0:.2f} from {1}".format(amount,self.label))

    def deposit(self, amount):# method for deposting money into account
        if amount <0:#if statment that check for an amount greater then 0
            print("${0:.2f} is an invaild deposit amount".format(amount))
        else:
            self.balance += amount
            print("Depositing ${0:.2f} to {1}".format(amount,self.label))
        
        
    def Balance(self):#method for printing the balance with open end for formatting
        return ( "{0}:  ${1:.2f} \n".format(self.label, self.balance))
    
    def transfer(self, amount, ID):#method for printing tranfer line
        print("Transfering ${0:.2f} to {1} from {2}".format(amount,ID,self))

    def __str__(self):# string label for the account label
        return self.label


class Checking(BankAccount): # checking account subclass 
    def __init__(self, label,limit): #constructor for label and limit
        self.limit= limit 
        self.checknum= 0 #setting instance variable for check numbers
        BankAccount.__init__(self,label)# adding BankAccount constructors

    
    
    def pCheck(self,amount): #printing check method
        if amount <self.limit and amount < self.balance: #checking is amount is less then the limit and less then checking balance totoal
            self.balance-= amount
            self.checknum+= 1
            print("Check #{0:04d} for {1:.2f}\n".format(self.checknum,amount))

        else:
            if amount > self.limit:
                print("Error ${0:.2f} is over amount limit of ${1:.2f}".format(amount,self.limit))#error message for being over check limit
            else:
                if amount > self.balance:
                    print("Overdraft Error ${0:.2f} is more then ${1:.2f} account balance".format(amount,self.balance))# error for overdrafting checking is over checking balance     
        

class Savings(BankAccount):# saving account subclass 

    def __init__(self, label, rate): # savings constructor
        self.rate = rate
        BankAccount.__init__(self,label)# adding BankAccount constructors
        
    def accrueInterest(self,time):# method for accrueing interest
        interest= self.rate * (time/12) * self.balance
        self.balance= interest+self.balance
        

def main():
    check=Checking("My Checking", 250)
    save=Savings("My Savings", .05)
    print(check.Balance())
    print(save.Balance())
    check.deposit(100)
    save.deposit(50)
    print("Check for $50")
    check.pCheck(50)
    print(check.Balance())
    print("My Savings accrueing two months interest")
    save.accrueInterest(2)
    print(save.Balance())
    print("Check for $10")
    check.pCheck(10)
    print(check.Balance())
    check.pCheck(250)
    print()
    check.deposit(2000)
    print()
    check.pCheck(1000)
    print(check.Balance())
    print(save.Balance())
    
    
    
    

   #Prints Author's name, class and date
    print("\nLee Kitchen")
    print ("Class: CIS110", "Program: Program12")
   #this function will print current date and time using sctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__ == '__main__':
    main()
