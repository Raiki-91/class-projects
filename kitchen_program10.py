"""
Program Name: CIS110 Program Template
Program Description: Uses class BankAccount class to simulate deposits, current balance, transfer money and make withdrawals.
Author Name: Lee Kitchen
Date Created: 11/20/201
Notes: Uses classes to simulate check/saving/cash.


"""

import time

class BankAccount():
    balance= 0
    cash= 0

    def __init__(self,label):#construstor for labeling an account
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
        print( "{0}:  ${1:.2f} ".format(self.label, self.balance),end=' ')
    
    def transfer(self, amount, ID):#method for printing tranfer line
        print("Transfering ${0:.2f} to {1} from {2}".format(amount,ID,self))

    def __str__(self):# string label for the account label
        return self.label
    

def main():
    save=BankAccount("Savings")#creating acounts
    check=BankAccount("Checking")
    cash= 0 #setting cash variable to 0
    print("Opening Balances:") #starting balances
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))
    print()
    print()
    check.deposit(500)#$500 deposit to checking
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))#balances
    print()
    print()
    save.deposit(100)#$100 deposit to savings
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))#balances
    print()
    print()
    check.transfer(150,save)#$150 transfer to savings
    check.withdraw(150)
    save.deposit(150)
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))#balances
    print()
    print()
    check.deposit(-50)# validating invalid deposit amount
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))#balances
    print()
    print()
    check.withdraw(600)#validating invalid withdrawal amount
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))#balances
    print()
    print()
    check.withdraw(250)#$250 withdrawal to cash from checking
    cash=250
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))#balances
    print()
    print()
    save.withdraw(100)#$100 withdrawal to cash from savings
    cash= cash +100
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))#balances
    print()
    print()
    save.transfer(75, check)#$75 transfer from saving to checking
    save.withdraw(75)
    check.deposit(75)
    check.Balance()
    save.Balance()
    print("Cash: ${0:.2f} ".format(cash))#balances
    


   #Prints Author's name, class and date
    print("\nLee Kitchen")
    print ("Class: CIS110", "Program: Program10")
   #this function will print current date and time using sctime()
    print(time.asctime( time.localtime(time.time())))
    
if __name__ == '__main__':
    main()
