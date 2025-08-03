import json
import os
import random
from pathlib import Path

DATABASE_PATH = Path('data.json')

# with open(DATABASE_PATH,'r') as file:
#     data = json.load(file)
#     print(data)
    

def printline():
    print("___________________________________")

def load_data():
    try: 
        if DATABASE_PATH.exists():
            try:
                with open(DATABASE_PATH,"r") as file:
                    data = json.load(file)
                    print("DATA LOADED....")
                    print(data)
                    printline()
                    return data
            except Exception as err:
                print(f"An error occured {err}")
    except Exception as err:
        print(f"2. An error occured {err}")

def save_data(new_data):
    with open(DATABASE_PATH,'w') as file:
        data = json.dump(new_data,file)

# def updateData(new_data):
    try:
        if os.path.exists(DATABASE_PATH): #if path exists then 
            with open(DATABASE_PATH, 'r') as file: #open data.json file read mode
                try: 
                    data = json.loads(file)
                except Exception as err:
                    print(f"An error occured {err}")
                    data = []
        else:
            data = []
        data.extend(new_data)
        with open(DATABASE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as err:
        print(f"An error occurred while updating data: {err}")

# def account_auth(acc_number,acc_pin):
    data = load_data()
    acc_number = input("Enter Your 8-Digit Account Number : ")
    acc_pin = input("Enter Your 4 Digit Pin : ")

    return acc_number, acc_pin

def createAccount():
    new_data = load_data()
    # print(new_data)
    # print("** Data loding")
    new_account = {
        "name" : input("Enter Your Name : "),
        "age" : int(input("Enter Your Age : ")),
        "phone" : input("Enter Your Mobile Number : "),
        "email" : input("Enter Your Email : ")
    }
    
    # if user_details["age"] <= 18 :
    #     print("Sorry You can't able to Open an Account.")
    # if user_details["email"].endswith('@gmail.com') == False:
    #     validate_email = input("Enter Valid Email : ")
    #     user_details["email"] = validate_email


    printline()
    print("Account Created Successfully.")
    printline()

    #Generate Account Number
    accountNum = random.randrange(10000000,99999999)
    new_account['accountNo'] = str(accountNum)
    print(f"Account Number is {new_account["accountNo"]}")

    #Ask for Pin
    new_account['pin'] = input("Enter 4 Digit Pin : ")

    printline()
    new_data.append(new_account)
    print(new_data)
    save_data(new_data)
    
def viewAccount():
    data = load_data()
    acc_number = input("Enter Your 8-Digit Account Number : ")
    acc_pin = input("Enter Your 4 Digit Pin : ")
    print(type(data))
    print(type(acc_number))
    printline()

    try:
        found_data = [i for i in data if i['accountNo'] == acc_number]
        print(found_data)
    except Exception as err:
        print(f"An error occured in {err}")


    printline()
    print("Here's Your Account Details : \n")
    for i in found_data[0]:
        print(f"{i} : {found_data[0][i]}")
    # if found_data == True:
    # else :
    #     print("Not Data Found")
    
def depositInAccount():
    data = load_data()
    acc_number = input("Enter Your 8-Digit Account Number : ")
    acc_pin = input("Enter Your 4 Digit Pin : ")

    



    deposit_amount = input("Enter Your Deposit Amount : ")

    
    


def withdrawFromAccount():
    pass

def updateAccount():
    pass

def deleteAccount():
    pass

def main():
    printline()
    print("Bank Account Manager Project :")
    printline()
    print("1. Create/Open Bank Account.")
    print("2. View Your Bank Account.")
    print("3. Deposit to Your Bank Account.")
    print("4. Withdraw from Your Bank Account.")
    print("5. Update Your Account Details.")
    print("6. Delete Your Bank Account.")

    printline()
    user_input = int(input("Enter Your Input for proceesed :"))
    printline()

    match user_input:
        case 1:
            createAccount()
        case 2:
            viewAccount()
        case 3:
            depositInAccount()
        case 4:
            withdrawFromAccount()
        case 5:
            updateAccount()
        case 6:
            deleteAccount()

main()