from account import Account






print("Welcome to the Banking System")

# user input for creating an account
name = input("Enter your name: ")
initial_balance = float(input("Please enter your first deposit: "))
account = Account(name, initial_balance)

# menu loop
while True:
    print("\nMenu: a. Withdraw b. Deposit c. Check Balance d. Transaction History e. Exit")
    choice = input("Choose an option (a/b/c/d/e): ").lower()

    if choice == 'a':
        # Withdraw
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 'b':
        # Deposit
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)

    elif choice == 'c':
        # Check Balance
        account.display_balance()

    elif choice == 'd':
        # Transaction History
        account.display_transaction_history()

    elif choice == 'e':
        # Exit the program
        print("Thank you for using the Banking System. Goodbye!")
        break

    else:
        # Invalid choice
        print("Invalid choice. Please choose a valid option.")