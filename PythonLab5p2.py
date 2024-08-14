class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} to account {self.account_number}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds in account {self.account_number}. Current balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")
    def get_balance(self):
        return self.balance

    def generate_statement(self):
        return f"Account {self.account_number}: Balance = ${self.balance:.2f}"
    

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def transfer_money(self, from_account, to_account, amount):
        from_acc = from_account.get_balance()
        if from_acc < amount:
            print("Insufficient funds for the transfer.")
        else:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"Transferred ${amount:.2f} from account {from_account.account_number} to account {to_account.account_number}.")
    
    def generate_bank_statement(self):
        statement = f"Bank: {self.name}\n"
        for customer in self.customers:
            statement += f"\nCustomer: {customer.name}\n"
            for account in customer.get_accounts():
                statement += f"{account.generate_statement()}\n"
        return statement
    

# Example 


bank = Bank("El-Ahly Bank")

customerSte = Customer("Stephania Ehab")
customerVer = Customer("Veronia Ehab")

accountSte = Account(110, 10000)  # Account with $500 balance
accountVer = Account(120, 50000) # Account with $1000 balance

accountMar = Account(200, 2000) # Account with $1500 balance

customerSte.add_account(accountSte)
customerVer.add_account(accountVer)
customerVer.add_account(accountMar)

bank.add_customer(customerSte)
bank.add_customer(customerVer)

print(bank.generate_bank_statement())

bank.transfer_money(accountSte, accountMar, 5000)

print("\nAfter Transfer:")
print(bank.generate_bank_statement())

print("\nAccount Balance:")
print(f"Account {accountSte.account_number}: ${accountSte.get_balance():.2f}")