from BankAC import BankAccount
from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount


B1 = BankAccount( 1111, 500)
B1.displaybalance()
B1.withdraw(200)
B1.deposit(700)
B1.displaybalance()

print("******************************************* ")

B2 = BankAccount(1112,200)
B2.displaybalance()
B2.transfer(500,B1)
B1.displaybalance()
B2.displaybalance()

print("******************************************* ")

s1 = SavingAccount( 1113, 2000)
s1.displaybalance()
s1.savedeposit(500)
s1.displaybalance()
s1.withdraw(4000)

print("******************************************* ")

c1 = CurrentAccount(1114, 2000)
c1.displaybalance()
c1.deposit(500)
c1.curwithdrwal(100)
c1.transfer(500,s1)
c1.displaybalance()

print("******************************************* ")


