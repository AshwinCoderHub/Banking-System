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

    def __init__(self, account_id, name, mobile_number, email, city, state, pincode, initial_balance):
        # Initialize account attributes
        self.account_id = account_id
        self.name = name
        self.mobile_number = mobile_number
        self.email = email
        self.city = city
        self.state = state
        self.pincode = pincode
        self._balance = initial_balance
        self._history = []

    def generate_transaction_id(self):
        # Generate a unique transaction ID based on timestamp and counter
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        transaction_id = f"{timestamp}{Account.transaction_id_counter:00d}"
        Account.transaction_id_counter += 1
        return transaction_id

    @log_deposit
    def deposit(self, amount):
        # Increase balance with a deposit
        self._balance += amount

    @log_withdraw
    def withdraw(self, amount):
        # Check for sufficient funds before withdrawing
        if amount > self._balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            # Decrease balance with a withdrawal
            self._balance -= amount

    def display_balance(self):
        # Display current account balance
        print(f"Account ID: {self.account_id}, Balance: ₹{self._balance}")

    def display_transaction_history(self):
        # Display transaction history
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


