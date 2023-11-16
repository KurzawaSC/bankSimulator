import random
from usersData import clientAndNumbers
from usersData import idForUsers
from usersData import usersPins
from usersData import users


class Account:
    nextClientNumber = 0
    currentClientNumber = 0
    balance = 0

    def __init__(self, name='', surname='', balance=0):
        self.name = name
        self.name = name
        self.surname = surname
        self.balance = balance
        self.password = 1234
        self.accountNumber = random.randint(
            10000000000000000000000000, 99999999999999999999999999)
        self.pin = 0000

    def create_account(self):
        self.nextClientNumber = Account.nextClientNumber
        Account.nextClientNumber += 1
        name = input('Enter your name: ')
        surname = input('Enter your surname: ')
        password = input('Create your passwrod: ')
        i = 0
        while i == 0:
            pin = input('Create your PIN (4 numbers): ')
            if (len(str(pin)) == 4):
                i += 1
            else:
                print('Your PIN number must have 4 numbers!')
        self.pin = pin
        self.password = password
        self.name = name
        self.surname = surname
        print('Name:', self.name, '\n Surname:', self.surname,
              '\n Account number:', self.nextClientNumber,
              '\n Your balance: 0 $'
              '\n Your account number:', self.accountNumber)
        return idForUsers.update({int(self.nextClientNumber): password}), users,\
            clientAndNumbers.update({int(self.nextClientNumber): int(self.accountNumber)}),\
            usersPins.update({int(self.nextClientNumber): int(self.pin)})

    def depositing(self):
        newDeposit = int(input('How much amount do you want to deposit?: '))
        self.balance += newDeposit
        print('Done, your current balance:', self.balance, '$')

    def withdrawal(self):
        paycheck = int(input('How much money you want to withdraw?: '))
        if (paycheck <= self.balance):
            self.balance -= paycheck
            print('Done, your current balance:', self.balance, '$')
        else:
            print('You don\'t have enough funds\n')

    def balance_check(self):
        print('Your current balance:', self.balance, '$')

    @staticmethod
    def interface_log_out():
        print('What do you want to do? \n \
                1 - Log in \n \
                2 - Create new account \n')

        selectedKey = input('Enter right key: ')
        currentClientNumber = 0

        if (selectedKey == '1'):
            currentClientNumber = int(input('Enter your account number: '))
            if (currentClientNumber <= len(users)-1):
                typedPassword = input('Enter your password: ')
                if (typedPassword == idForUsers[currentClientNumber]):
                    print('Hello,', users[currentClientNumber].name)
                    users[currentClientNumber].interface_log_in(
                        currentClientNumber)
                else:
                    print('Wrong password, please try again: ')
                    users[currentClientNumber].interface_log_out()
            else:
                print('That clinet number doesn\'t exist')
                Account.interface_log_out()

        elif (selectedKey == '2'):
            users.append(Account())
            currentClientNumber = len(users)-1
            users[currentClientNumber].create_account()
            print('Hello,', users[currentClientNumber].name)
            users[currentClientNumber].interface_log_in(currentClientNumber)
        else:
            print('Error, please try again \n \n')
            Account.interface_log_out()

    @staticmethod
    def interface_log_in(currentClientNumber):
        doesntMatter = 0

        while doesntMatter == 0:
            print('What do you want to do? \n \
                1 - Check your balance \n \
                2 - Depositing \n \
                3 - Withdrawing \n \
                4 - Transfer \n \
                5 - Log out')

            selectedKey = input('Enter right key: ')
            if (selectedKey == '1'):
                users[currentClientNumber].balance_check()
            elif (selectedKey == '2'):
                users[currentClientNumber].depositing()
            elif (selectedKey == '3'):
                users[currentClientNumber].withdrawal()
                users[currentClientNumber].interface_log_in(
                    currentClientNumber)
            elif (selectedKey == '4'):
                users[currentClientNumber].transfer()
            elif (selectedKey == '5'):
                users[currentClientNumber].log_out()
            else:
                print('Error, please try again \n \n')
                continue

    def log_out(self):
        Account.interface_log_out()

    def transfer(self):
        recipient = int(input("Enter recipient's account number: "))
        for key, value in clientAndNumbers.items():
            if (value == recipient):
                i = 0
                while i == 0:
                    sum = int(input('Enter the transfer amount: '))
                    if (sum <= self.balance):
                        i = 0
                        while i == 0:
                            enterPin = int(input('Enter your PIN: '))
                            if (usersPins[self.nextClientNumber] == enterPin):
                                self.balance -= sum
                                users[int(key)].balance += sum
                                print('Done\n')
                                i += 1
                            else:
                                print("Wrong PIN number, please try again: ")

                    else:
                        print('You don\'t have enough fuds')
