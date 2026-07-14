class BankAccount:
    bank_name='National python Bank '
    def __init__ (self,full_name, account_number,initial_balance=0.0) :
        self.full_name=full_name
        self._account_number= account_number
        self.__balance=initial_balance


    def deposit(self,amount):
        if amount > 0: 
            self.__balance +=amount 
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance :
            self.__balance -=amount 
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self,name,account_number):
        if name ==self.full_name and account_number==self._account_number:
            return self.__balance 
        else:
            print ('Authentication failed')
            return None 


    def display_info(self):
        print(f'Account Holder: ,{self.full_name }')
        print(f'Account Number : ,{self._account_number}')
        print(f'Bank : {BankAccount.bank_name}')



if __name__ == "__main__":
    # Create an object (instance) of BankAccount
    account1 = BankAccount("Alice Johnson", 123456789, 1000.0)

    # Access public methods
    # account1.display_info()
    account1.deposit(500)
    account1.withdraw(200)

    balance = account1.get_balance("Alice Johnson", 123456789)

    print(f"Total amount: {balance}")
    # account1.display_info()