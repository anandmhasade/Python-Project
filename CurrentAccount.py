from BankAC import BankAccount

class CurrentAccount(BankAccount):

    def __init__(self, no, initialAmount ):
        super().__init__(no, initialAmount)
        print(" Congurations..! Your Current Account has  been Created. " +str(self._accNo))

    def curwithdrwal(self, amount):
        amount += 200
        print(" Charge 200 is applicable for every withdrwal ")
        self.withdraw(amount)