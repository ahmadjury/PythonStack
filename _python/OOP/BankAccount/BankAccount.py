class account:
	def __init__(self,int_rate=.01, account_balance=0):
		self.account_int_rate = int_rate
		self.account_balance = account_balance
	def deposit(self, amount):
		self.account_balance+=amount
	def withdraw(self, amount):
		self.account_balance-=amount
	def display_account_info(self):
		self.account_balance
		self.account_int_rate
		print(self.account_balance)
		print(self.account_int_rate)
	def yield_interest(self):
		self.account_balance = 1.01*self.account_balance
		return self.account_balance



account1 = account(.01,5000)
account2 = account(.01,7000)

account1.display_account_info()

account2.display_account_info()

print("_"*30)

account1.deposit(1000)
account1.deposit(500)
account1.deposit(500)
account1.withdraw(2000)
account1.yield_interest()

account1.display_account_info()

print("_"*30)

account2.deposit(1000)
account2.deposit(3000)
account2.withdraw(500)
account2.withdraw(400)
account2.withdraw(500)
account2.withdraw(600)
account2.yield_interest()

account2.display_account_info()


