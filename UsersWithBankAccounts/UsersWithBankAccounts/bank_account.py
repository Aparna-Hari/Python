class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print (f"balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

# account1 = BankAccount(2.45,20000)
# account2 = BankAccount(0.99,50000)




# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# account1.deposit(2000).deposit(3000).deposit(3000).withdraw(1000).yield_interest().display_account_info()

# #To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
# account2.deposit(2000).deposit(3000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
