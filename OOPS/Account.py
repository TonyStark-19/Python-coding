# This code creates account class with balnce and account no attributes

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance :", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance :", self.get_balance())

    def get_balance(self):
        return self.balance
        

a1 = Account(10000, 12345)

print(a1.balance)
print(a1.account_no)

a1.debit(4000)

a1.credit(500)