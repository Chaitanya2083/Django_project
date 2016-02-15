user_name = 'admin'
password = '1234'
print("*"*30)
print("WELCOME TO BMS".center(30))
print("*"*30)
uname = input("Please Enter Username: ")
pwd = input("Please Enter Password: ")
if uname == user_name and pwd == password:
    print("You are successfully logged in to BMS")
    print ("1. Accounts \n2. Transactions \n3. Reports \n4. Exit")
    try:
        ch = int(input("Please Enter your choice: "))
    #except ValueError as Error:
        #print("Error:Please Enter only integers from 1 to 4")
        #ch = int(input("Please Enter your choice: "))
        if ch == 1:
            print("Your Selected choice is:1. Accounts")
            print("1: Add Account \n2: List Accounts \n3: Update Account \n4: Delete Account \n5: Go to main menu \n6: Exit")
        elif ch == 2:
            print("Your Selected choice is:2. Transactions")
            print("1: Withdraw \n2: Deposit \n3: Show balance \n4: Go to main menu \n5: Exit")
        elif ch == 3:
            print("Your Selected choice is:3. Reports")
            print("1: Mini statement \n2: Monthly statement \n3: Quarterly statement \n4: Exit")
        elif ch == 4:
            print("Your Selected choice is:4. Exit")
    except ValueError as Error:
        print("Error:Please Enter only integers from 1 to 4",Error)
        ch = int(input("Please Enter your choice: "))

else:
    number_attempts = 0
    while number_attempts < 3:
        print("Username or Password mismatch, please try again")
        number_attempts = number_attempts + 1
    print("Your account got locked, please talk to admin")

