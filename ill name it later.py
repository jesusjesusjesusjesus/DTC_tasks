def bank_procedure(user):
    action = "PENDING"
    emotion = input("hello",user[0],",how are you today?")
    if emotion.upper() == "HAPPY":
        print("Amazing! Me too!")
    if emotion.upper() == "SAD":
        print("Aw man, I feel for ya buddy.")
    else:
        print("Ok, well let's get on with it")
    while action = "PENDING"
    action.upper() = input("what would you like to do?: ")
    print("(withdraw, deposit, view balance)")
    if action == "WITHDRAW":
        while action == "WITHDRAW":
            if user[2] == 0:
                print(user[2])
                print("it looks like you don't have any money in this account")
                empty_deposit.upper() = input("Would you like to deposit?(Y/N): ")
                if empty_deposit == "N":
                    print("OK",user[0])
                while empty_deposit == "Y":
                    deposit_amount = input("how much would you like to deposit?: ")
                    print("(do not include dollar signs)")
                        if deposit_amount >= 1000
                            deposit_large.upper() = input("are you sure? that's alot of money.(Y/N): ")
                            if deposit_large == "Y":
                                user[2] = user[2] + deposit_amount
                                print("this is your new amount.")
                                print(user[2])
                                log_out.upper() = input("would you like to log out?(Y/N): ")
                                    if log_out == "Y":
                                        print("thankyou for visiting the bank, come again")
                                    if log_out == "N"
                                        action = "PENDING"
    if action == "DEPOSIT":
        while action == "DEPOSIT":
            deposit_amount = input("how much would you like to deposit?: ")
            print("(do not include dollar signs)")
            user[2] = user[2] + deposit_amount
            print("your balance is now")
            print(user[2])
            log_out.upper = input("would you like to log out?(Y/N): ")
                if log_out == "Y":
                    print("thankyou for visiting the bank, come again")
                if log_out == "N"
                    action = "PENDING"
     if action == "VIEW BALANCE":
        while action == "VIEW BALANCE":
            print(user[2])
            log_out.upper = input("would you like to log out?(Y/N): ")
                if log_out == "Y":
                    print("thankyou for visiting the bank, come again")
                if log_out == "N"
                    action = "PENDING"

def password(user):
    import time
    password_tries = 3
    password_time = 5
    password_attempts = 0
    if user[1] == 0
        print("you do not seem to have a password")
        while user[1] == 0
            user[1] = int(input("what would you like your new password to be?(numbers): ")
            print("ok, your password is now" user[1])
            print("confirm password")
            print(user[1])
            confirm_password.upper = input("is this this right?(Y/N): ")
            if confirm_password == "N":
                user[1] = 0
            if confirm_password == "Y":
                print("your password is now" user[1])
    password = int(input("what is your password?(numbers): ")
    if password == user[1]:
        print("ok, you're in")
    elif password != user[1]:
        password_attempts + 1
        if password_attempts = 3:
            print()




#main routine
user_number = 0
user_one = [one_name, 0, 0]
user_two = [two_name, 0, 0]
user_three = [three_name, 0, 0]
user_four = [four_name, 0, 0]
user_five = [five_name, 0, 0]
user_six = [six_name, 0, 0]
user_seven = [seven_name, 0, 0]
user_eight = [eight_name, 0, 0]
user_nine = [nine_name, 0, 0]
user_ten = [ten_name, 0, 0]
print("welcome to the bank")
user_name = input("what is your name?: ")
if user_name == user_one[0]:
    bank_procedure(user_one)
if user_name == user_two[0]:
    bank_procedure(user_two)
if user_name == user_three[0]:
    bank_procedure(user_three)
if user_name == user_four[0]:
    bank_procedure(user_four)
if user_name == user_five[0]:
    bank_procedure(user_five)
if user_name == user_six[0]:
    bank_procedure(user_six)
if user_name == user_seven[0]:
    bank_procedure(user_seven)
if user_name == user_eight[0]:
    bank_procedure(user_eight)
if user_name == user_nine[0]:
    bank_procedure(user_nine)
if user_name == user_ten[0]:
    bank_procedure(user_ten)
else:
    print("you do not seem to have a account.")
    create_account = input("would you like to create one?(Y/N): ")
    if create_account.upper == "Y":

