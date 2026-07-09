class BankAccount:
    """A class representing a standard bank account."""

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


class SavingsAccount(BankAccount):
    """A subclass of BankAccount that yields interest over time."""

    def __init__(self, account_number: str, owner: str, balance: float = 0.0, interest_rate: float = 0.0):
        """
        Initializes the savings account.
        Uses super() to hand off base attributes to BankAccount, then sets interest_rate.
        """
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate  # Represented as a percentage (e.g., 5.0 for 5%)

    def apply_interest(self) -> float:
        """Calculates interest based on current balance and interest_rate, and adds it to the balance."""
        interest_earned = self.balance * (self.interest_rate / 100)
        self.balance += interest_earned
        return self.balance

    def __str__(self) -> str:
        """Overrides the base class __str__ to include the interest rate."""
        # We can leverage the parent string representation or build a custom one:
        return f"Savings Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f} (Interest Rate: {self.interest_rate}%)"


# ==========================================
# TEST CODE
# ==========================================
if __name__ == "__main__":
    print("--- 1. Creating a SavingsAccount Instance ---")
    # Create an instance of SavingsAccount (5% interest rate)
    savings = SavingsAccount(account_number="67890", owner="Bob", balance=1000.0, interest_rate=5.0)
    print(savings)
    print()

    print("--- 2. Demonstrating Inherited Functionalities ---")
    # Demonstrate inherited deposit
    savings.deposit(500.0)
    print(f"Deposited $500.00 -> New Balance: ${savings.balance:.2f}")

    # Demonstrate inherited withdrawal
    savings.withdraw(300.0)
    print(f"Withdrew $300.00  -> New Balance: ${savings.balance:.2f}")
    print(savings)
    print()

    print("--- 3. Applying Interest ---")
    # Current balance is $1200.00. 5% of 1200 is $60.00. New balance should be $1260.00.
    savings.apply_interest()
    print("Interest applied!")
    print(savings)