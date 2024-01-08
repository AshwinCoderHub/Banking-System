from datetime import datetime

# Decorator to log deposit transactions
def log_deposit(func):
    def wrapper(self, amount):
        # Get current timestamp
        timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S")

        # Generate unique transaction ID
        transaction_id = self.generate_transaction_id()

        # Create a transaction dictionary
        transaction = {"id": transaction_id, "action": "deposit", "timestamp": timestamp, "amount": amount,
                       "balance": self._balance}

        # Append the transaction to the history
        self._history.append(transaction)
        # Call the original method
        result = func(self, amount)
        return result

    return wrapper

# Decorator to log withdraw transactions
def log_withdraw(func):
    def wrapper(self, amount):
        # Get current timestamp
        timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S")

        # Generate unique transaction ID
        transaction_id = self.generate_transaction_id()

        # Create a transaction dictionary
        transaction = {"id": transaction_id, "action": "withdraw", "timestamp": timestamp, "amount": amount,
                       "balance": self._balance}

        # Append the transaction to the
        self._history.append(transaction)

        # Call the original method
        result = func(self, amount)
        return result

    return wrapper




class Account:
    transaction_id_counter = 1

    # Constructor
    def __init__(self, name, initial_balance):
        self.name = name
        self._balance = initial_balance
        self._history = []  # Transaction history list

    # Method to generate a unique transaction ID
    def generate_transaction_id(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        transaction_id = f"{timestamp}{Account.transaction_id_counter:00d}"
        Account.transaction_id_counter += 1
        return transaction_id

    # Decorate the deposit method with the log_deposit decorator
    @log_deposit
    def deposit(self, amount):
        # Increase balance by the deposit amount
        self._balance += amount

    # Decorate the withdraw method with the log_withdraw decorator
    @log_withdraw
    def withdraw(self, amount):
        # Check if there are sufficient funds
        if amount > self._balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            # Decrease balance by the withdrawal amount
            self._balance -= amount

    # Display the current balance
    def display_balance(self):
        print(f"Balance: ₹{self._balance}")

    # Display the transaction history
    def display_transaction_history(self):
        if not self._history:
            print("No transaction history.")
        else:
            print("\nTransaction History:")
            print("{:<15} {:<10} {:<23} {:<15} {:<20}".format("Transaction ID", "Action", "Date Time", "Amount",
                                                              "Current Balance"))
            for transaction in self._history:
                print("{:<15} {:<10} {:<23} ₹{:<15} ₹{:<20}".format(
                    transaction["id"], transaction["action"],
                    transaction["timestamp"], transaction["amount"],
                    transaction["balance"]))

