class Wallet:
    def __init__(self, balance): 
        self.balance = balance
    
    def set_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        self.balance = self.balance - val

    def increase_balance(self):
        self.balance = self.balance + 1000

if __name__ == "__main__":
    myWallet = Wallet(0)
    myWallet.increase_balance()
    val = myWallet.get_balance()
    print("El balance tiene que ser 1000 y es: ", val)