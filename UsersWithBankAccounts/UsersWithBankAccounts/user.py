from bank_account import BankAccount

class User:
    def __init__(self, name, email_address ):
        self.name = name
        self.email_address = email_address
        self.account = BankAccount(int_rate=0.1,balance=0)


    def make_deposit(self, amount):
        self.account.deposit(amount) 
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self


user1 = User( "Ray",  "Ray@gamil.com")
user1.make_deposit(1000)
user1.display_user_balance()