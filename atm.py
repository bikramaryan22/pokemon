from time import sleep

def password():
    pin = int(input("please, enter your account pin: "))
    if pin == 5241:
        print("Correct account, Please wait were fetching your info")
        sleep(2)
        return True
    else:
        print("Incorrect password, Authentication error")
        return False


def atm_start():

    balance = 0

    print("Welcome to Bikrams ATM")
    if password():
        while True:
            print("press '1' for checking balance")
            print("press '2' for withdrawl")
            print("press '3' for deposit")
            print("press '4' for exiting out of the Atm")

            choose = int(input("\nchoose which money transaction fits for your transaction"))

            if choose == 1:
                print("Please wait were fetching your data")
                sleep(2)
                print("hello your account balance is ",balance)

            elif choose == 2:
                withdrawl = int(input("how much money do you want to take from your account "))
                balance = balance - withdrawl
                print(f"you have successfully taken{withdrawl}money from your account ")
            elif choose == 3:
                deposit = int(input("how much money do you want to add in your account"))
                balance = balance + deposit
                print(f"you have successfully added{deposit}money to your account ")
            elif choose == 4:
                print("thanks for using the atm,hope you have a good day")
                break

atm_start()
