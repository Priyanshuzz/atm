# ATM System

# Function to read account data from file
def read_accounts():
    accounts = {}
    with open("accounts.txt", "r") as file:
        for line in file:
            account_info = line.strip().split(",")
            account_number = account_info[0]
            account_name = account_info[1]
            pin = account_info[2]
            balance = float(account_info[3])
            accounts[account_number] = {"name": account_name, "pin": pin, "balance": balance}
    return accounts

# Function to update account data to file
def update_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for account_number, account_info in accounts.items():
            line = f"{account_number},{account_info['name']},{account_info['pin']},{account_info['balance']:.2f}\n"
            file.write(line)

# Function to display account balance
def display_balance(account):
    print(f"Account Balance: ${account['balance']:.2f}")

# Function to withdraw funds
def withdraw(account, amount):
    if amount > 0 and amount <= account['balance']:
        account['balance'] -= amount
        update_accounts(accounts)
        print(f"Withdrawn: ${amount:.2f}")
    else:
        print("Invalid amount or insufficient balance.")

# Function to deposit funds
def deposit(account, amount):
    if amount > 0:
        account['balance'] += amount
        update_accounts(accounts)
        print(f"Deposited: ${amount:.2f}")
    else:
        print("Invalid amount.")

# Main function
if __name__ == "__main__":
    accounts = read_accounts()

    while True:
        print("\nWelcome to the ATM")
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if account_number in accounts and accounts[account_number]["pin"] == pin:
            account = accounts[account_number]
            print(f"Welcome, {account['name']}!")

            while True:
                print("\nMenu:")
                print("1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    display_balance(account)
                elif choice == "2":
                    amount = float(input("Enter withdrawal amount: $"))
                    withdraw(account, amount)
                elif choice == "3":
                    amount = float(input("Enter deposit amount: $"))
                    deposit(account, amount)
                elif choice == "4":
                    print("Thank you for using the ATM. Have a nice day!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid account number or PIN. Please try again.")
