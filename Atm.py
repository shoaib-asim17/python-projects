class BankAccount:

    def __init__(self):
        self.balance=0

    def withdraw(self,wd):
        self.wd=wd
        if wd>self.balance:
            print("your balance is less than the amount which you have entered ---you cannot withdraw")
        else:
            self.balance-=wd
            print("withdrawl amount :",wd)

    def deposit(self,_deposit):
        self.balance+=_deposit
        return self.balance

    def checkbal(self):
        return self.balance

def main():
    
    account=BankAccount()

    while True:
        print("1.withdraw")
        print("2.deposit")
        print("3.check balance")
        print("4.exit")

   
        choice= input("Enter your choice :")
        if choice=="1":
            wd=int(input("Enter the amount to withdraw : "))
            account.withdraw(wd)
           

        elif choice=="2":
            _deposit=int(input("Enter the amount to be deposited : "))
            depositedAmount=account.deposit(_deposit)
            print("your total amount is: ",depositedAmount)
        

        elif choice=="3":
           account.checkbal()
           print("your current balance is : ",    account.checkbal())

        else:
            print("--Terminating---")
            break


main()
            
        
           