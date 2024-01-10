from datetime import datetime
from account import Account, log_deposit, log_withdraw

class BankingSystem:
    def __init__(self, system_name):
        # Initialize banking system attributes
        self.system_name = system_name
        self.accounts = {}

    def create_account(self, name, mobile_number, email, city, state, pincode, initial_balance):
        # Check if the mobile number and email are unique
        if any(acc.mobile_number == mobile_number or acc.email == email for acc in self.accounts.values()):
            print("Error: Mobile number or email is already associated with an existing account.")
            return

        # Generate a unique account ID
        account_id = self.generate_account_id()

        # Create a new account and add it to the banking system
        new_account = Account(account_id, name, mobile_number, email, city, state, pincode, initial_balance)
        self.accounts[account_id] = new_account
        print(f"Account created for {name} with Account ID: {account_id} and initial deposit of ₹{initial_balance}.")

    def generate_account_id(self):
        # Generate a unique account ID based on timestamp and the number of existing accounts
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{timestamp}{len(self.accounts) + 1:03d}"

    def get_account(self, account_id):
        # Get the account object for a specific account ID
        return self.accounts.get(account_id)

    def access_account(self):
        account_id = input("Enter Account ID: ")
        account = self.get_account(account_id)
        if account:
            email_or_mobile = input("Enter email or mobile number: ")
            if email_or_mobile == account.email or email_or_mobile == account.mobile_number:
                return account
            else:
                print("Email or mobile number does not match the account.")
                return None
        else:
            print(f"No account found for Account ID: {account_id}.")
            return None

    def display_all_accounts(self):
        # Display information for all accounts in the banking system
        print("\nAll Accounts in the Banking System:")
        for account_id, account in self.accounts.items():
            print(f"Account ID: {account_id}, Customer: {account.name}, Balance: ₹{account._balance}")

# Program Flow for Banking System
if __name__ == "__main__":
    print("Welcome to the Banking System")

    banking_system = BankingSystem("GlobalBank")

    while True:
        print("\nMenu: a. Create Account b. Access Account c. Display All Accounts d. Exit")
        choice = input("Choose an option (a/b/c/d): ").lower()

        if choice == 'a':
            name = input("Enter customer name: ")
            mobile_number = input("Enter mobile number: ")
            email = input("Enter email: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            pincode = input("Enter pincode: ")
            initial_balance = float(input("Enter initial deposit amount: "))
            banking_system.create_account(name, mobile_number, email, city, state, pincode, initial_balance)

        elif choice == 'b':
            account = banking_system.access_account()
            if account:
                while True:
                    print(f"\nAccount Menu for Account ID: {account.account_id}: "
                          f"a. Withdraw b. Deposit c. Check Balance d. Transaction History e. Exit")
                    account_choice = input("Choose an option (a/b/c/d/e): ").lower()

                    if account_choice == 'a':
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)

                    elif account_choice == 'b':
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)

                    elif account_choice == 'c':
                        account.display_balance()

                    elif account_choice == 'd':
                        account.display_transaction_history()

                    elif account_choice == 'e':
                        break

                    else:
                        print("Invalid choice. Please choose a valid option.")

        elif choice == 'c':
            banking_system.display_all_accounts()

        elif choice == 'd':
            print("Thank you for using the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
