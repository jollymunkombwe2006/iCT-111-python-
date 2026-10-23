balance = 1000.0
password = "1234"

# Store transaction history
transaction_history = []

print("===== AIRTEL MONEY =====")

# LOGIN
entered_password = input("Enter your password: ")

if entered_password != password:
    print("Incorrect password.")
else:
    print("\nLogin successful!")

    while True:
        print("\n===== MAIN MENU =====")
        print("  1. View Balance")
        print("  2. Send Money")
        print("  3. Deposit Money")
        print("  4. Reverse Transaction")
        print("  5. Make Payment")
        print("  6. Transaction History")
        print("  7. Change Password")
        print("  8. Exit")

        choice = input("Choose an option: ")

        # VIEW BALANCE
        if choice == "1":
            print(f"Your balance is K{balance:.2f}")

        # SEND MONEY
        elif choice == "2":
            number = input("Enter Airtel number: ")
            try:
                amount = float(input("Enter amount to send: K"))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                transaction_history.append(f"Sent K{amount:.2f} to {number}")
                print(f"K{amount:.2f} sent to {number}")
                print(f"New balance: K{balance:.2f}")

        # DEPOSIT MONEY
        elif choice == "3":
            try:
                amount = float(input("Enter amount to deposit: K"))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if amount > 0:
                balance += amount
                transaction_history.append(f"Deposited K{amount:.2f}")
                print(f"K{amount:.2f} deposited successfully.")
                print(f"New balance: K{balance:.2f}")
            else:
                print("Amount must be greater than zero.")

        # REVERSE TRANSACTION
        elif choice == "4":
            try:
                amount = float(input("Enter amount to reverse: K"))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if amount > 0:
                balance += amount
                transaction_history.append(f"Reversed K{amount:.2f}")
                print(f"K{amount:.2f} has been reversed.")
                print(f"New balance: K{balance:.2f}")
            else:
                print("Amount must be greater than zero.")

        # MAKE PAYMENT
        elif choice == "5":
            business_name = input("Enter business/merchant name: ")
            try:
                amount = float(input("Enter amount to pay: K"))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                transaction_history.append(f"Paid K{amount:.2f} to {business_name}")
                print(f"Payment of K{amount:.2f} to {business_name} was successful.")
                print(f"New balance: K{balance:.2f}")

        # TRANSACTION HISTORY
        elif choice == "6":
            print("\n===== TRANSACTION HISTORY =====")
            if not transaction_history:
                print("No transactions available.")
            else:
                for i, trans in enumerate(transaction_history, start=1):
                    print(f"{i}. {trans}")

        # CHANGE PASSWORD
        elif choice == "7":
            old_password = input("Enter old password: ")
            if old_password == password:
                new_password = input("Enter new password: ")
                password = new_password
                print("Password changed successfully.")
            else:
                print("Incorrect old password.")

        # EXIT
        elif choice == "8":
            print("Thank you for using Airtel Money.")
            break

        else:
            print("Invalid option. Please try again.")