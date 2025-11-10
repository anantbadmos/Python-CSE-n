import os
from datetime import datetime

BALANCE_FILE = "balance.txt"
PIN_FILE = "pin.txt"
STATEMENT_FILE = "statement.txt"

ACCOUNT_HOLDER = {
    "Name": "Archit Vashisth",
    "Account No.": "123456789012",
    "Bank": "Vashisth Industries Bank",
    "Mobile": "+91 9876543210",
    "Account Type": "Savings",
    "IFSC": "VIBK0001234"
}

def initialize_files():
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as file:
            file.write("0")

    if not os.path.exists(PIN_FILE):
        with open(PIN_FILE, "w") as file:
            file.write("0000")  

    if not os.path.exists(STATEMENT_FILE):
        with open(STATEMENT_FILE, "w") as file:
            file.write("")

def get_balance():
    with open(BALANCE_FILE, "r") as file:
        return float(file.read())

def update_balance(new_balance):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(new_balance))

def get_pin():
    with open(PIN_FILE, "r") as file:
        return file.read().strip()

def update_pin(new_pin):
    with open(PIN_FILE, "w") as file:
        file.write(new_pin)

def record_transaction(entry):
    with open(STATEMENT_FILE, "a") as file:
        file.write(entry + "\n")

def show_mini_statement():
    print("\n📜 Last 5 Transactions:")
    if not os.path.getsize(STATEMENT_FILE):
        print("No transactions yet.")
        return

    with open(STATEMENT_FILE, "r") as file:
        lines = file.readlines()
        last_five = lines[-5:]
        for line in last_five:
            print(line.strip())

def show_account_holder_details():
    print("\n===== ACCOUNT HOLDER DETAILS =====")
    for key, value in ACCOUNT_HOLDER.items():
        print(f"{key}: {value}")

def atm_menu():
    print("\n===== MINI ATM INTERFACE =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Mini Statement")
    print("6. Account Details") 
    print("7. Exit")

def main():
    initialize_files()

    print("\n👋 Welcome to ATM!")
    print("User: **Archit Vashisth**")

    attempts = 3
    while attempts > 0:
        user_pin = input("Enter ATM PIN: ")
        if user_pin == get_pin():
            print("✅ Login Successful!")
            break
        else:
            attempts -= 1
            print(f"❌ Incorrect PIN! {attempts} attempts left.")
    else:
        print("⚠ Card Blocked! Too many incorrect attempts.")
        return

    while True:
        atm_menu()
        choice = input("Enter your choice: ")

        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if choice == '1':
            print(f"💰 Current Balance: ₹{get_balance()}")

        elif choice == '2':
            amt = float(input("Enter amount to deposit: ₹"))
            if amt > 0:
                new_balance = get_balance() + amt
                update_balance(new_balance)
                record_transaction(f"{now} - Deposited ₹{amt}")
                print("✅ Amount Deposited Successfully!")
            else:
                print("❌ Invalid amount!")

        elif choice == '3':
            amt = float(input("Enter amount to withdraw: ₹"))
            curr_balance = get_balance()
            if amt > 0 and amt <= curr_balance:
                update_balance(curr_balance - amt)
                record_transaction(f"{now} - Withdrawn ₹{amt}")
                print("✅ Withdrawal Successful!")
            else:
                print("❌ Insufficient Balance or Invalid Amount!")

        elif choice == '4':
            old_pin = input("Enter Current PIN: ")
            if old_pin == get_pin():
                new_pin = input("Enter New PIN: ")
                update_pin(new_pin)
                record_transaction(f"{now} - PIN Changed")
                print("✅ PIN Updated Successfully!")
            else:
                print("❌ Incorrect Current PIN!")

        elif choice == '5':
            show_mini_statement()

        elif choice == '6':
            show_account_holder_details()

        elif choice == '7':
            print("👋 Thank you for using ATM, Archit Vashisth!")
            break

        else:
            print("❌ Invalid Choice! Try again.")

if __name__ == "__main__":
    main()
