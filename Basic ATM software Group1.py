accounts={}
def create_account():
    global accounts
    print ("Create an account if you don't have one")
    username= input("Enter your preferred username: ").strip().title()
    if username in accounts:
        print("\n\nAccount already exists.\n\nLogin or enter another account name")
        return
    else:
     pin= input("Enter your pin: ").strip()
    if len(pin) != 4 or pin.isalpha():
            print("\nIncorrect PIN.\n Pin must be 4 digits")
            return
    else:

     accounts[username]={
            "pin":pin,
            "balance":0,
        }
    print("\n\nAccount created successfully\n\n")

#Login function
def login_account():
    global accounts
    print("Login your account")
    username = input("Enter your username: ").strip().title()
    pin = input("Enter your pin: ").strip()


    if username in accounts and accounts[username]["pin"] == pin:
        print("\n\nLogin successful")

        return username
    else:
        print("\nLogin failed.\nInvalid account.\n\n Try again")
        return None

#to change user's pin
def update_account(username):
    global accounts
    print ("Update your 4-digit pin")
    current_Pin = (input("Enter your 4-digit pin: "))
    if current_Pin != accounts[username]['pin'] or current_Pin.isalpha():
        print("incorrect pin.\n Check details and try again")
        return
    else:
        new_Pin= (input("Enter your new 4-digit pin: "))
        accounts[username]['pin']=new_Pin
        print("Account Pin updated successfully!")

#To deposit money
def deposit_cash(username):
    global accounts
    print("Deposit to your account")
    amount=float(input("Enter your amount: "))
    accounts[username]['balance']=accounts[username]['balance']+amount
    print("\n\nAccount balance updated successfully!\n\n New account balance is: ", accounts[username]['balance'])
#withdraw money function
def withdraw_cash(username):
    global accounts
    print("\nWithdraw from your account")
    amount=float(input("\nEnter your amount: "))

    if amount > accounts[username]['balance']:
        print("Insufficient funds")
    else:
        accounts[username]['balance'] -= amount
        print("\n\nWithdraw successful!")
        print("\n\nYour new balance is: ", accounts[username]['balance'])
def check_balance(username):
    print("CHECK CURRENT BALANCE")
    print("\n\nYour current balance is: ", accounts[username]['balance'])
#main program
while True:
    print("Welcome to Group 1 ATM software\n\n\nSelect an option to proceed")
    print("1. Create account")
    print("2. Login account")
    print("3. Exit")
    option = int(input("Select an option: "))

    if option == 1:
        create_account()

    elif option == 2:
        username = login_account()

        if username is None:
            continue
        while True:
            print("\nSelect an option to proceed: ")
            print("\n\n1. Withdraw cash")
            print("2. Check balance")
            print("3. Update pin")
            print("4. Deposit cash")
            print("5. Exit")
            option = int(input("Select option: "))

            if option == 1:
               withdraw_cash(username)
            elif option == 2:
               check_balance(username)
            elif option == 3:
               update_account(username)
            elif option == 4:
               deposit_cash(username)
            elif option == 5:
              break
            else:
                print("Invalid option.")
    elif option == 3 :
        break
    else:
        print("Invalid option.\n Please select a valid option.")























