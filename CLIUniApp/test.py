import pickle
from datetime import datetime
import os

class Account:
    def __init__(self, type):
        self.type = type
        self.balance = self.read_balance()

    def read_balance(self):
        return float(input(f'Initial {self.type} balance $'))

    def has_type(self, type):
        return self.type == type

    def has(self, amount):
        return self.balance >= amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def pay_to(self, amount, target):
        self.balance -= amount
        target.balance += amount

    def __str__(self):
        return f'{self.type} account has ${self.balance:.2f}'


class BackUp:
    filename = '/Storage/test.data'

    @staticmethod
    def initialize():
        try:
            customers = []
            if not os.path.exists(BackUp.filename):
                with open(BackUp.filename, 'wb') as file:
                    pickle.dump(customers, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')

    @staticmethod
    def read():
        try:
            with open(BackUp.filename, 'rb') as file:
                customers = pickle.load(file)
                print(customers)
            return customers
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
            return []
        except IOError as e:
            print(f'Reading Error: {e}')
            return []

    @staticmethod
    def write(customers):
        try:
            with open(BackUp.filename, 'wb') as file:
                pickle.dump(customers, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')


class Bank:
    DTF = '%d/%m/%Y - %H:%M:%S'
    NOW = datetime.now()
    
    def __init__(self):
        self.admin = Manager()
        BackUp.initialize()
        self.customers = BackUp.read()

    def read_choice(self):
        return input('Customer menu (L/A/X): ').upper()

    def customer(self, name):
        for c in self.customers:
            if c.match(name):
                return c
        return None

    def read_name(self):
        return input('Enter Customer Name: ')

    def show(self):
        customer = self.customer(self.read_name())
        if customer is not None:
            print(customer)
        else:
            print('Customer does not exist')

    def view(self):
        for customer in self.customers:
            print(customer)

    def add(self):
        name = self.read_name()
        customer = self.customer(name)
        if customer is None:
            self.customers.append(Customer(name))
            BackUp.write(self.customers)
        else:
            print('Customer already exists')

    def remove(self):
        customer = self.customer(self.read_name())
        if customer is not None:
            self.customers.remove(customer)
            BackUp.write(self.customers)
        else:
            print('Customer does not exist')

    def customer_login(self):
        c = self.customer(self.read_name())
        if c is not None:
            index = self.customers.index(c)
            c.use()
            self.customers[index] = c
            BackUp.write(self.customers)
        else:
            print('Customer does not exist')

    def admin_login(self):
        self.admin.use(self)
        
### Bank Class/Main Class
    def menu(self):
        print(f'Bank menu: {self.NOW.strftime(self.DTF)}')
        while True:
            choice = self.read_choice()
            if choice == 'L':
                self.customer_login()
            elif choice == 'A':
                self.admin_login()
            elif choice == 'X':
                print('Done')
                break
            else:
                self.help()

    def help(self):
        print('help ========')
        print('Menu options')
        print('L = Login into customer menu')
        print('A = Login to admin menu')
        print('X = exit')


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = [Account("Savings"), Account("Loan")]

    @classmethod
    def create(cls):
        name = input('Create Accounts for Customer: ')
        return cls(name)

    def match(self, name):
        return self.name == name

    def account(self, type):
        for a in self.accounts:
            if a.has_type(type):
                return a
        return None

    def deposit(self):
        savings = self.account("Savings")
        if savings is not None:
            amount = self.read_amount("deposit")
            savings.deposit(amount)
        else:
            print("No such account")

    def withdraw(self):
        amount = self.read_amount("withdraw")
        savings = self.account("Savings")
        if savings is not None:
            if savings.has(amount):
                savings.withdraw(amount)
            else:
                print("Insufficient funds")
        else:
            print("No such account")

    def transfer(self):
        amount = self.read_amount("transfer")
        savings = self.account("Savings")
        loan = self.account("Loan")
        if savings is not None:
            if savings.has(amount):
                if loan is not None:
                    savings.pay_to(amount, loan)
                else:
                    print("No such account")
            else:
                print("Insufficient funds")
        else:
            print("No such account")

    def read_amount(self, action):
        return float(input(f"Amount to {action}: $"))

    def show(self):
        print(f"{self.name} bank statement: {Bank.NOW.strftime(Bank.DTF)}")
        for account in self.accounts:
            print(account)

    def __str__(self):
        accounts_info = ' | '.join(str(account) for account in self.accounts)
        return f'{self.name}\t--> {accounts_info}'

    def read_choice(self):
        return input('Customer menu (d/w/t/s/x): ').lower()

    def use(self):
        print(f'{self.name} banking menu: {Bank.NOW.strftime(Bank.DTF)}')
        while True:
            choice = self.read_choice()
            if choice == 'd':
                self.deposit()
            elif choice == 'w':
                self.withdraw()
            elif choice == 't':
                self.transfer()
            elif choice == 's':
                self.show()
            elif choice == 'x':
                print('Back to Bank menu')
                break
            else:
                self.help()

    def help(self):
        print('Menu options')
        print('d = deposit')
        print('w = withdraw')
        print('t = transfer')
        print('s = show')
        print('x = exit')


class Manager:
    def __init__(self):
        self.name = "John Smith"

    def view(self, bank):
        bank.view()

    def show(self, bank):
        bank.show()

    def remove(self, bank):
        bank.remove()

    def add(self, bank):
        bank.add()

    def read_choice(self):
        return input('Manager menu (a/r/s/v/x): ').lower()

    def use(self, bank):
        print(f'{self.name} admin menu: {Bank.NOW.strftime(Bank.DTF)}')
        while True:
            choice = self.read_choice()
            if choice == 'a':
                self.add(bank)
            elif choice == 'r':
                self.remove(bank)
            elif choice == 's':
                self.show(bank)
            elif choice == 'v':
                self.view(bank)
            elif choice == 'x':
                print('Back to Bank menu')
                break
            else:
                self.help()

    def help(self):
        print('Menu options')
        print('a = add a new customer')
        print('r = remove a customer')
        print('s = show customer statement')
        print('v = view all customers')
        print('x = exit')



if __name__ == "__main__":
    # bank = Bank()
    # bank.menu()
    BackUp.initialize()
    BackUp.read()
    BackUp.write({'a': 1, 'b': 2, 'c': 3})
    BackUp.read()