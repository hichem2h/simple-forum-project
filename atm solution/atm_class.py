class ATM :

    def __init__(self, balance, name):
        self.name = name
        self.balance = balance

    def withdraw (self, request):
        sep = '-' * 23

        print sep
        print 'Welcome to {}'.format(self.name)
        print 'Current balance = {}'.format(self.balance)
        print sep

        if   request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.balance -= request
            cash = [100, 50, 20, 10, 5, 2, 1]
            for e in cash:
                while request >= e:
                    print 'give {}'.format(e)
                    request -= e


if __name__ == '__main__':
    balance1 = 500
    balance2 = 1000

    atm1 = ATM(balance1, "Smart Bank")
    atm2 = ATM(balance2, "Baraka Bank")

    atm1.withdraw(277)
    atm1.withdraw(800)

    atm2.withdraw(100)
    atm2.withdraw(2000)
