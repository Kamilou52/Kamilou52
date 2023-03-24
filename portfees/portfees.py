def portfeescalculator():
    user_command = input("Your command amount please ? : ")
    country = input("Delevery country? (CH, FR, DE, AU, autre) : ")
    devise = "CH, FR, DE, AU, autre"

    try:
        command = int(user_command)
    except:
        print("Try again, You haven't yet a number!")
        quit()

    if country.upper() == "Fr" or country.upper() == "DE":
        if command <= 100 :
            fees = 10
            print("Fees are equal to 10%")
        elif  100 < command <= 1000: 
                    fees = 5
                    print("Fees are equal to 5%")
        elif command > 1000: 
            fees = 1
            print("Fees are equal to 1%")
        
        devise = "Euro"
        
    elif country == "CH":
        if command <= 100:
            fees = 5
            print("fees are equal to 5%")
        elif 100 < command <= 1000:
            fees = 2
            print("Fees are equal to 2%")
        elif command > 1000:
            fees = 0
            print("Fees are equal to 0%")
            
        devise = "CHF"

    elif country == "AU":
        if command <= 100:
            fees = 8
            print("Fees are equal to 8%")
        elif 100 < command <= 1000:
            fees = 6
            print("Fees are equal to 6%")
        elif command > 1000:
            fees = 4
            print("Fees are equal to 4%")
        
        devise = "Euro"

    else:
        if command <= 100:
            fees = 12
            print("Fees are equal to 12%")
        elif 100 < command <= 1000:
            fees = 10
            print("Fees are equal to 10%")
        elif command > 1000:
            fees = 8
            print("Fees are equal to 8%")
        
        devise = "Euro"

    total = command + command*fees / 100
    message = "the amount is : " + str(total) + devise
    return message

def ask_to_continue():
    user_answer = input("Do you want to calculate new portfees ? (yes ou no) ")
    if user_answer.upper() == "YES":
        return True
    else:
        return False
    
print(portfeescalculator())

while ask_to_continue():
    print(portfeescalculator())

