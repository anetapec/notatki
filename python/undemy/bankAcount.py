class Result():
    def __init__(self, isSuccess, message, value):
        self.isSuccess = None
        self.message = message
        self.value = value

class OK(Result):
    def __init__(self, isSuccess, message, amount):
        super().__init__(message, amount)
        self.isSuccess = True

class Error(Result):
    def __init__(self, isSuccess, message, amount):
        self.isSuccess = False

class BankAcount():

    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        '''tu sprawdza się pieniądze czy prawdziwe'''
        self.balance += amount

    def try_withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return OK ("Wypłacono :", amount )
        return Error ("Brak wystarczających środków.", amount)
    def __str__(self):
        return str(self.balance)

class MinimumBalanceAcount(BankAcount):
    def __init__(self, balance = 0, minimumBalance = 1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def try_withdraw(self, amount):
        if self.balance - amount > self.minimumBalance:
            return super().try_withdraw(amount)
        else:
            return Error ('Nieudało się, próba przekroczenia progu', amount)

