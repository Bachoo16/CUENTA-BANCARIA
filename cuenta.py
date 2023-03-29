class BankAccount:
    cuentas = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

ahorrros = BankAccount(.05,1000)
checking = BankAccount(.02,5000)

ahorrros.deposito(10).deposito(20).deposito(40).withdraw(600).yeild_interest().display_account_info()
checking.deposito(100).deposito(200).deposito(400).withdraw(60).yeild_interest().display_account_info()

