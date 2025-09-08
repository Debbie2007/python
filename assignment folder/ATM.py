"""
for this one
it will also be a console app
just like everything else
the atm simulator should look something like this
ATM Menu:
1. Check Balance
2. Deposit
3. Withdraw
Choose an option: 3
Enter withdrawal amount: $150
Transaction successful! New balance: $850
"""

balance = 1000  # starting balance

print("Welcome to the ATM Simulator!")
print("Options: check | deposit | withdraw")

choice = input("What would you like to do? ").lower()

if choice == "check":
    print(f"Your current balance is: ${balance}")

elif choice == "deposit":
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"You deposited ${amount}. New balance is: ${balance}")

elif choice == "withdraw":
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print(f"You withdrew ${amount}. New balance is: ${balance}")
    else:
        print("Insufficient funds. Transaction cancelled.")

else:
    print("Invalid option. Please select check, deposit, or withdraw.")