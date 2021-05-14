class user:
    def __init__(self,name,balance):
        self.name=name
        self.user_balance=balance

    def make_deposit(self, amount):
        self.user_balance+=amount

    def make_withdrawal(self,amount ):
        if (self.user_balance < amount):
            print("no enugh money")
        else: self.user_balance-=amount

    def display_user_balance(self):
        print (self.name)
        print (self.user_balance)


    def transfer(self,otheruser,amount):
        self.user_balance=self.user_balance-amount
        otheruser.user_balance=otheruser.user_balance+amount

ahmad = user("ahmad",5000)
Khalil = user("Khalil",6000)
tasneem = user("tasneem",10000)

ahmad.make_deposit(500)
ahmad.make_deposit(700)
ahmad.make_deposit(1500)

ahmad.make_withdrawal(500)

print ("_"*30)

ahmad.display_user_balance()
Khalil.display_user_balance()
tasneem.display_user_balance()

print ("_"*30)

Khalil.make_deposit(700)
Khalil.make_deposit(700)
Khalil.make_withdrawal(400)
Khalil.make_withdrawal(8000)

print ("_"*30)
ahmad.display_user_balance()
Khalil.display_user_balance()
tasneem.display_user_balance()

print ("_"*30)

tasneem.make_deposit(900)
tasneem.make_withdrawal(400)
tasneem.make_withdrawal(400)
tasneem.make_withdrawal(400)

ahmad.display_user_balance()
Khalil.display_user_balance()
tasneem.display_user_balance()


print ("_"*30)  



ahmad.transfer(tasneem,500)

ahmad.display_user_balance()
Khalil.display_user_balance()
tasneem.display_user_balance()


