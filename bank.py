class BankAccount:
    """A class representing a simple bank account."""

    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        """Initializes the bank account with an account number, owner, and starting balance."""
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Adds the given amount to the balance. Only allows positive amounts."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Subtracts the given amount from the balance if sufficient funds exist."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError(
                f"Insufficient funds. Trying to withdraw ${amount:.2f} "
                f"but current balance is ${self.balance:.2f}."
            )
        
        self.balance -= amount
        return self.balance

    def __str__(self) -> str:
        """Returns a user-friendly string representation of the account."""
        return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}"



if __name__ == "__main__":
    print("--- Initializing Account ---")
    # 1. Create an instance of BankAccount
    my_account = BankAccount(account_number="12345", owner="Alice", balance=500.0)
    print(my_account)
    print()

    print("--- Demonstrating Successful Transactions ---")
    # 2. Demonstrate a successful deposit
    my_account.deposit(150.0)
    print(f"Deposited $150.00 -> New Balance: ${my_account.balance:.2f}")

    # Demonstrate a successful withdrawal
    my_account.withdraw(200.0)
    print(f"Withdrew $200.00  -> New Balance: ${my_account.balance:.2f}")
    print(my_account)
    print()

    print("--- Testing Exception Handling ---")
    # 3. Attempt a withdrawal that exceeds the balance to trigger/catch the exception
    try:
        excessive_amount = 1000.0
        print(f"Attempting to withdraw: ${excessive_amount:.2f}")
        my_account.withdraw(excessive_amount)
    except ValueError as e:
        print(f"Caught expected error: {e}")
        
    # Bonus: Attempting a negative deposit to test that safeguard
    try:
        print(f"\nAttempting to deposit a negative amount (-$50):")
        my_account.deposit(-50)
    except ValueError as e:
        print(f"Caught expected error: {e}")