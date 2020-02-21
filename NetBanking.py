class Bank:
    def __init__(self):
        self.__acc = dict()
    
    def transfer(self,frmAccNo, frmPin, toAcc, amt):
        frmAcc = self.__acc[frmAccNo]
        toAcc = self.__acc[toAcc]
        if frmAcc.checkPin(frmPin):
            if frmAcc.Balance >= amt:
                frmAcc.withdraw(amt)
                toAcc.addFunds(amt)
            else:
                raise BankException("Insufficient Balance")
        else:
            raise BankException("Invalid Pin")
    def checkAccountBalance(self,AccNo, pin):
        if self.__acc[AccNo].checkPin(pin):
            account = self.__acc[AccNo]
            return account.Balance
    def create_account(self,AccNo,balance,pin):
        self.__acc[AccNo] = Account(AccNo, balance, pin)
class BankException(Exception):
    pass
class Account:
    def __init__(self,AccNo,Balance,Pin):
        self.AccNo=AccNo
        self.Balance=Balance
        self.__Pin=Pin
    def checkPin(self,pin):
        return pin==self.__Pin
    def addFunds(self,amount):
        self.Balance=self.Balance+amount
    def withdraw(self,amount):
        self.Balance =self.Balance-amount

b = Bank()
b.create_account(123,500,33)
b.create_account(321,600,23)
b.transfer(123,33,321,200)
print("The Account Balance after teansfer is",b.checkAccountBalance(123,33))
print("The Account Balance is",b.checkAccountBalance(321,23))
