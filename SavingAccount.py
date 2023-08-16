from BankAC import BankAccount

class SavingAccount(BankAccount):

    __acc = None

    def __init__(self, no, initialAmount):
        super().__init__(no, initialAmount)
        print(" Congratulations..! Your Saving Account has been created. " +str(self._accNo))


    def savedeposit(self, amount):
        intr = amount * 3 / 100
        amount += intr
        print(str(intr) + " interest is added in your account ")
        self.deposit(amount)