import mysql.connector


# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="banking"
)

cursor = db.cursor()


# 1. Create Account
def create_account():

    account_no = int(input("Enter account number: "))
    name = input("Enter your name: ")
    account_type = input("Enter account type (Savings/Current): ")
    balance = float(input("Enter initial balance: "))
    pin = int(input("Enter PIN: "))
    mobile = input("Enter mobile number: ")

    if account_type == "Savings" and balance >= 2000:

        query = """
        INSERT INTO accounts
        (account_no, name, account_type, balance, pin, mobile)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (account_no, name, account_type, balance, pin, mobile)

        cursor.execute(query, values)
        db.commit()

        print("Account created successfully")

    elif account_type == "Current" and balance >= 10000:

        query = """
        INSERT INTO accounts
        (account_no, name, account_type, balance, pin, mobile)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (account_no, name, account_type, balance, pin, mobile)

        cursor.execute(query, values)
        db.commit()

        print("Account created successfully")

    else:
        print("Invalid account type or insufficient minimum balance")


# 2. Deposit
def deposit():

    print("\n1. Search using Account Number")
    print("2. Search using Mobile Number")

    choice = input("Enter your choice: ")

    if choice == "1":

        account_no = int(input("Enter account number: "))

        query = "SELECT * FROM accounts WHERE account_no = %s"
        cursor.execute(query, (account_no,))

    elif choice == "2":

        mobile = input("Enter mobile number: ")

        query = "SELECT * FROM accounts WHERE mobile = %s"
        cursor.execute(query, (mobile,))

    else:
        print("Invalid choice")
        return

    data = cursor.fetchone()

    if data:

        print("Account found")

        pin = int(input("Enter PIN: "))

        if pin == data[4]:

            amount = float(input("Enter deposit amount: "))

            if amount > 0:

                balance = data[3]

                new_balance = balance + amount

                operation = (
                    str(balance) + " + " +
                    str(amount) + " = " +
                    str(new_balance)
                )

                query = """
                UPDATE accounts
                SET balance = %s
                WHERE account_no = %s
                """

                cursor.execute(query, (new_balance, data[0]))

                query = """
                INSERT INTO transactions
                (account_no, transaction_type, amount, operation)
                VALUES (%s, %s, %s, %s)
                """

                cursor.execute(
                    query,
                    (data[0], "Deposit", amount, operation)
                )

                db.commit()

                print("Deposit successful")
                print("New balance:", new_balance)

            else:
                print("Invalid deposit amount")

        else:
            print("Invalid PIN")

    else:
        print("Account not found")


# 3. Withdrawal
def withdraw():

    print("\n1. Search using Account Number")
    print("2. Search using Mobile Number")

    choice = input("Enter your choice: ")

    if choice == "1":

        account_no = int(input("Enter account number: "))

        query = "SELECT * FROM accounts WHERE account_no = %s"
        cursor.execute(query, (account_no,))

    elif choice == "2":

        mobile = input("Enter mobile number: ")

        query = "SELECT * FROM accounts WHERE mobile = %s"
        cursor.execute(query, (mobile,))

    else:
        print("Invalid choice")
        return

    data = cursor.fetchone()

    if data:

        print("Account found")

        pin = int(input("Enter PIN: "))

        if pin == data[4]:

            amount = float(input("Enter withdrawal amount: "))

            if amount > 0:

                balance = data[3]

                if amount <= balance:

                    new_balance = balance - amount

                    operation = (
                        str(balance) + " - " +
                        str(amount) + " = " +
                        str(new_balance)
                    )

                    query = """
                    UPDATE accounts
                    SET balance = %s
                    WHERE account_no = %s
                    """

                    cursor.execute(
                        query,
                        (new_balance, data[0])
                    )

                    query = """
                    INSERT INTO transactions
                    (account_no, transaction_type, amount, operation)
                    VALUES (%s, %s, %s, %s)
                    """

                    cursor.execute(
                        query,
                        (data[0], "Withdrawal", amount, operation)
                    )

                    db.commit()

                    print("Withdrawal successful")
                    print("Remaining balance:", new_balance)

                else:
                    print("Insufficient balance")

            else:
                print("Invalid withdrawal amount")

        else:
            print("Invalid PIN")

    else:
        print("Account not found")


# 4. Money Transfer
def transfer():

    sender_account = int(input("Enter sender account number: "))

    query = "SELECT * FROM accounts WHERE account_no = %s"
    cursor.execute(query, (sender_account,))

    sender = cursor.fetchone()

    if sender:

        print("Sender account found")

        receiver_account = int(
            input("Enter receiver account number: ")
        )

        if sender_account == receiver_account:

            print("Sender and receiver account cannot be same")
            return

        query = "SELECT * FROM accounts WHERE account_no = %s"
        cursor.execute(query, (receiver_account,))

        receiver = cursor.fetchone()

        if receiver:

            print("Receiver account found")

            pin = int(input("Enter PIN: "))

            if pin == sender[4]:

                amount = float(
                    input("Enter transfer amount: ")
                )

                if amount > 0:

                    sender_balance = sender[3]

                    if amount <= sender_balance:

                        new_sender_balance = (
                            sender_balance - amount
                        )

                        new_receiver_balance = (
                            receiver[3] + amount
                        )

                        # Sender operation
                        sender_operation = (
                            str(sender_balance) + " - " +
                            str(amount) + " = " +
                            str(new_sender_balance)
                        )

                        # Receiver operation
                        receiver_operation = (
                            str(receiver[3]) + " + " +
                            str(amount) + " = " +
                            str(new_receiver_balance)
                        )

                        query = """
                        UPDATE accounts
                        SET balance = %s
                        WHERE account_no = %s
                        """

                        cursor.execute(
                            query,
                            (new_sender_balance, sender_account)
                        )

                        cursor.execute(
                            query,
                            (new_receiver_balance, receiver_account)
                        )

                        query = """
                        INSERT INTO transactions
                        (account_no, transaction_type, amount, operation)
                        VALUES (%s, %s, %s, %s)
                        """

                        # Sender transaction
                        cursor.execute(
                            query,
                            (
                                sender_account,
                                "Transfer Sent",
                                amount,
                                sender_operation
                            )
                        )

                        # Receiver transaction
                        cursor.execute(
                            query,
                            (
                                receiver_account,
                                "Transfer Received",
                                amount,
                                receiver_operation
                            )
                        )

                        db.commit()

                        print("Money transferred successfully")
                        print(
                            "Sender balance:",
                            new_sender_balance
                        )

                    else:
                        print("Insufficient balance")

                else:
                    print("Invalid transfer amount")

            else:
                print("Invalid PIN")

        else:
            print("Receiver account not found")

    else:
        print("Sender account not found")


# 5. Account Details
def account_details():

    print("\n1. Search using Account Number")
    print("2. Search using Mobile Number")

    choice = input("Enter your choice: ")

    if choice == "1":

        account_no = int(input("Enter account number: "))

        query = "SELECT * FROM accounts WHERE account_no = %s"
        cursor.execute(query, (account_no,))

    elif choice == "2":

        mobile = input("Enter mobile number: ")

        query = "SELECT * FROM accounts WHERE mobile = %s"
        cursor.execute(query, (mobile,))

    else:
        print("Invalid choice")
        return

    data = cursor.fetchone()

    if data:

        print("\n-----------------------------")
        print("       ACCOUNT DETAILS")
        print("-----------------------------")

        print("Account Number :", data[0])
        print("Name           :", data[1])
        print("Account Type   :", data[2])
        print("Balance        :", data[3])
        print("Mobile Number  :", data[5])

        print("-----------------------------")

    else:
        print("Account not found")


# 6. Transaction History
def transaction_history():

    print("\n1. Search using Account Number")
    print("2. Search using Mobile Number")

    choice = input("Enter your choice: ")

    if choice == "1":

        account_no = int(input("Enter account number: "))

    elif choice == "2":

        mobile = input("Enter mobile number: ")

        query = """
        SELECT account_no
        FROM accounts
        WHERE mobile = %s
        """

        cursor.execute(query, (mobile,))

        data = cursor.fetchone()

        if data:
            account_no = data[0]

        else:
            print("Account not found")
            return

    else:
        print("Invalid choice")
        return

    query = """
    SELECT *
    FROM transactions
    WHERE account_no = %s
    """

    cursor.execute(query, (account_no,))

    data = cursor.fetchall()

    if data:

        print("\n----------------------------------------")
        print("          TRANSACTION HISTORY")
        print("----------------------------------------")

        for row in data:

            print("Transaction ID :", row[0])
            print("Type           :", row[2])
            print("Amount         :", row[3])
            print("Operation      :", row[4])
            print("----------------------------------------")

    else:
        print("No transactions found")


# 7. Change PIN
def change_pin():

    print("\n1. Change PIN using existing PIN")
    print("2. Change PIN if existing PIN is forgotten")

    choice = input("Enter your choice: ")

    # Existing PIN
    if choice == "1":

        account_no = int(input("Enter account number: "))

        query = """
        SELECT *
        FROM accounts
        WHERE account_no = %s
        """

        cursor.execute(query, (account_no,))

        data = cursor.fetchone()

        if data:

            old_pin = int(input("Enter existing PIN: "))

            if old_pin == data[4]:

                new_pin = int(input("Enter new PIN: "))

                query = """
                UPDATE accounts
                SET pin = %s
                WHERE account_no = %s
                """

                cursor.execute(
                    query,
                    (new_pin, account_no)
                )

                db.commit()

                print("PIN changed successfully")

            else:
                print("Invalid existing PIN")

        else:
            print("Account not found")


    # Forgot PIN
    elif choice == "2":

        print("\n1. Search using Account Number")
        print("2. Search using Mobile Number")

        search_choice = input("Enter your choice: ")

        if search_choice == "1":

            account_no = int(
                input("Enter account number: ")
            )

            query = """
            SELECT *
            FROM accounts
            WHERE account_no = %s
            """

            cursor.execute(query, (account_no,))

        elif search_choice == "2":

            mobile = input("Enter mobile number: ")

            query = """
            SELECT *
            FROM accounts
            WHERE mobile = %s
            """

            cursor.execute(query, (mobile,))

        else:
            print("Invalid choice")
            return

        data = cursor.fetchone()

        if data:

            new_pin = int(input("Enter new PIN: "))

            query = """
            UPDATE accounts
            SET pin = %s
            WHERE account_no = %s
            """

            cursor.execute(
                query,
                (new_pin, data[0])
            )

            db.commit()

            print("PIN changed successfully")

        else:
            print("Account not found")

    else:
        print("Invalid choice")


# Main Menu
while True:

    print("\n========== BANKING APPLICATION ==========")

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Money Transfer")
    print("5. Account Details")
    print("6. Transaction History")
    print("7. Change PIN")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        transfer()

    elif choice == "5":
        account_details()

    elif choice == "6":
        transaction_history()

    elif choice == "7":
        change_pin()

    elif choice == "8":

        print("Thank you for using Banking Application")

        cursor.close()
        db.close()

        break

    else:
        print("Invalid choice")