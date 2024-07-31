class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

class Customer:
    def __init__(self, customer_id, name, balance=0):
        self.customer_id = customer_id
        self.name = name
        self.balance = balance
        self.loan = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdraw amount or insufficient funds.")

    def borrow(self, amount):
        if amount > 0:
            self.loan += amount
            self.balance += amount
            print(f"Borrowed {amount}. New balance is {self.balance}. Total loan is {self.loan}.")
        else:
            print("Borrow amount must be positive.")

    def repay_loan(self, amount):
        if 0 < amount <= self.loan and amount <= self.balance:
            self.loan -= amount
            self.balance -= amount
            print(f"Repaid {amount}. Remaining loan is {self.loan}. New balance is {self.balance}.")
        else:
            print("Invalid repayment amount or insufficient funds.")

def main():
    # Create a bank
    bank = Bank("MyBank")

    while True:
        print("\n1. Create new account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Borrow")
        print("5. Repay loan")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = int(input("Enter account number: "))
            name = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            new_customer = Customer(customer_id, name, initial_balance)
            bank.add_customer(new_customer)
            print(f"Account created for {name} with account number {customer_id}.")

        elif choice == '2':
            customer_id = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            customer = bank.get_customer(customer_id)
            if customer:
                customer.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            customer_id = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            customer = bank.get_customer(customer_id)
            if customer:
                customer.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            customer_id = int(input("Enter account number: "))
            amount = float(input("Enter amount to borrow: "))
            customer = bank.get_customer(customer_id)
            if customer:
                customer.borrow(amount)
            else:
                print("Account not found.")

        elif choice == '5':
            customer_id = int(input("Enter account number: "))
            amount = float(input("Enter amount to repay loan: "))
            customer = bank.get_customer(customer_id)
            if customer:
                customer.repay_loan(amount)
            else:
                print("Account not found.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
