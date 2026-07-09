from typing import List

class BankAccount:
    # Class variable to keep track of the next available account number
    _next_account_number = 1000  # Starting at 1000 for a realistic look

    def __init__(self, owners: List[str], balance: float = 0.0):
        """
        Initializes the bank account.
        Automatically assigns and increments the account number.
        Accepts a list of owners instead of a single string.
        """
        # Automatically assign the current counter value, then increment it for the next account
        self.account_number = str(BankAccount._next_account_number)
        BankAccount._next_account_number += 1
        
        # Ensure owners are stored as a list, even if a single string is passed
        if isinstance(owners, str):
            self.owners = [owners]
        else:
            self.owners = list(owners)
            
        self.balance = balance

    def add_owner(self, new_owner: str):
        """Adds a new co-owner to the account."""
        if not new_owner:
            raise ValueError("Owner name cannot be empty.")
        if new_owner in self.owners:
            print(f"{new_owner} is already an owner of this account.")
            return
        self.owners.append(new_owner)

    def deposit(self, amount: float) -> float:
        """Adds the given amount to the balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Subtracts the given amount from the balance if sufficient funds exist."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Current balance: ${self.balance:.2f}")
        self.balance -= amount
        return self.balance

    def __str__(self) -> str:
        """Returns a string representation of the account with all owners."""
        owners_str = ", ".join(self.owners)
        return f"Account {self.account_number} – Owners: [{owners_str}], Balance: ${self.balance:.2f}"



if __name__ == "__main__":
    print("--- Creating Multiple Accounts (Auto-Incrementing IDs) ---")
    
    # Create account 1 with a single owner
    account1 = BankAccount(owners="Alice", balance=500.0)
    print(account1)
    
    # Create account 2 with multiple owners
    account2 = BankAccount(owners=["Bob", "Charlie"], balance=1200.0)
    print(account2)
    
    # Create account 3 to prove the counter keeps ticking up
    account3 = BankAccount(owners="Diana", balance=50.0)
    print(account3)
   
    #Create account 4 to prove the counter keeps ticking up
    account4 = BankAccount(owners="Kelly", balance=1000.0)
    print(account4)

    print("--- Adding a Co-owner to Account 1 ---")
    # Add an owner to Alice's account
    account1.add_owner("Evan")
    print(account1)