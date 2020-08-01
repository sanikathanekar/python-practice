'''
bank application menu view, transactions, exit
transaction menu - changing user name, withdrawing money, depositing money, viewing ccount detials
'''
customers = {}
class Customer:
    def __init__(self,name,account,pin):
        self.__name= name
        self.__account= account
        self.__pin=pin

    def updateName(self,name):
        self.__name=name
        print("Name updated succesfully")
        
    def withdraw(self,amount):
        if self.__account.balance>= amount:
            self.__account.balance = self.__account.balance - amount
            print("Withdrawl succesfull")
        else:
            print("Indufficient Balance")

    def deposit(self,amount):
        self.__account.balance = self.__account.balance + amount

        
    def viewAccount(self):
        print("Your current balance is ",self.__account.balance)

class Account:
    def __init__(self,balance):
        self.balance= balance

                    
                    
def openAccount():
    global customers
    name = input("Enter name of customer-")
    pin = input("Enter pin")
    a = Account(0)
    c = Customer(name, a, pin)
    customers[pin] = c
    print("Account opened with balance ",a.balance)

def performTransactions():
    global customers
    pin = input("Enter pin-")
    if pin in customers:
        customer = customers[pin]
        print("What kind of transaction do you want to perform: \n 1. Withdraw\n2. Deposit\n3. Check Balance\n4. Update Details")
        option = input("Select your option-")
        if option == '1':
            amount = int(input("Enter amount"))
            customer.withdraw(amount)
        elif option == '2':
            amount = int(input("Enter amount"))
            customer.deposit(amount)
        elif option == '3':
            customer.viewAccount()
        elif option == '4':
            name = input("what's the new name")
            customer.updateName(name)
    else:
        print("Customer doesn't exist or invalid pin")
        
def main():
    print("                  Detroit United Bank                 ")
    print("Welcome to Detroit United Banks Net Banking Application")
    while(True):
        print("1. Create Account\n2.Perform Transactions\n3. Exit")
        option = input("Select your option-")
        if option=='1':
            openAccount()
        elif option=='2':
            performTransactions()
        elif option=='3':
            break
        

if __name__ == '__main__':
    main()
    
