class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.balance = 0

    def make_deposit(self,amount):
        self.balance += amount
        return self

    def make_withdrawl(self,amount):
        self.balance = self.balance-amount
        return self

    def display_user_balance(self):
        print(self.name,self.balance)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)
        return self



user1= User('Aparna','aparna@hari.com')
user2= User('Sreeram','sreeram@kumar.com')
user3= User('Snigdha','sniggy@email.com')

user1.make_deposit(5000) .make_deposit(5000) .make_deposit(5000) .make_withdrawl(1000) 
user1.display_user_balance()

user2.make_deposit(10000).make_deposit(10000).make_withdrawl(1000).make_withdrawl(1000)
user2.display_user_balance()

user3.make_deposit(10000).make_withdrawl(1000).make_withdrawl(1000).make_withdrawl(1000)
user3.display_user_balance()

user1.transfer_money(user2,3000)
user1.display_user_balance()
user2.display_user_balance()

# Create a file with the User class, including the __init__ and make_deposit methods

# Add a make_withdrawal method to the User class

# Add a display_user_balance method to the User class

# Create 3 instances of the User class

# Have the first user make 3 deposits and 1 withdrawal and then display their balance

# Have the second user make 2 deposits and 2 withdrawals and then display their balance

# Have the third user make 1 deposits and 3 withdrawals and then display their balance

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances