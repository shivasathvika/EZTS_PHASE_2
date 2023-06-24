'''write a python class BamkAccount with attributes like account_number,balance,date_of_opening and customer_name,methods like deposit ,with draw and check_balance'''
class Bankaccount:
    def __init__(self):
        self.acc=input('Account no.=')
        self.balance=int(input('Balance='))
        self.doo=input('Date of open:')
    def deposit(self):
        amount=int(input('amount to deposit:'))
        self.balance+=amount
        print('balance after deposit:',self.balance)
    def withdraw(self):
        amount=int(input('amount to withdraw:'))
        if (amount>self.balance):
            print('insufficient balance!!')
        else:
            self.balance-=amount
            print('balance after withdraw:',self.balance)

    def check_balance(self):
        print('total balance==>',self.balance)
a1=Bankaccount()
a1.deposit()
a1.withdraw()
a1.check_balance()
