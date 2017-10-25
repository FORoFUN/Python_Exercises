#Lab 13
#Problem 1
class BankAccount(object):
    def __init__(self, account_number, balance):
        self.account = account_number
        self.balance = balance
        
    def get_balance(self):
        return self.balance
        
    def withdraw(self, x):
        if ((self.balance - x) < 0):
            print("Insufficient amount of money, no action will be taken")
        else:
            self.balance = self.balance - x
            
    def deposit(self, x):
        self.balance = self.balance + x

def main():
    account = input("What is your account number: ")
    money = int(input("How much money do you have on your account: "))
    my_account = BankAccount(account,money)
    print("Current balance is: ", my_account.get_balance())
    while True:
        ask_user = input("Is there anything you want to do? (Y/N) ")
        if (ask_user.lower() == "y"):
            action = input("Do you want to deposit or withdraw money from your account: ")
            if (action == "deposit"):
                amount = int(input("How much do you want to deposit: "))
                my_account.deposit(amount)
                print("Current balance is: ", my_account.get_balance())
            elif (action == "withdraw"):
                amount = int(input("How much do you want to withdraw: "))
                my_account.withdraw(amount)
                print("Current balance is: ", my_account.get_balance())
            else:
                print("Invalid input, bye~")
        else:
            print("Thank you")
            break

main()
