in_currency = input("Enter currency EUR, USD, GBP: ")
if in_currency == "EUR":
    out_currency = input("What currency to convert USD or GBP: ")
    if out_currency == "USD":
        in_money = int(input("Enter money: "))
        data_EUR_to_USD_rate = 1.13
        out_money = in_money * data_EUR_to_USD_rate
        print(out_money, "USD")
    elif out_currency == "GBP":
        in_money = int(input("Enter money: "))
        data_EUR_to_GBP_rate = 0.86
        out_money = in_money * data_EUR_to_GBP_rate
        print(out_money, "GBP")
    else:
        print("Currency for conversion was entered incorrectly!")

elif in_currency == "USD":
    out_currency = input("What currency to convert EUR or GBP: ")
    if out_currency == "EUR":
        in_money = int(input("Enter money: "))
        data_USD_to_EUR_rate = 0.87
        out_money = in_money * data_USD_to_EUR_rate
        print(out_money, "EUR")
    elif out_currency == "GBP":
        in_money = int(input("Enter money: "))
        data_USD_to_GBP_rate = 0.76
        out_money = in_money * data_USD_to_GBP_rate
        print(out_money, "GBP")
    else:
        print("Currency for conversion was entered incorrectly!")
    
elif in_currency == "GBP":
    out_currency = input("What currency to convert EUR or USD: ")
    if out_currency == "EUR":
        in_money = int(input("Enter money: "))
        data_GBP_to_EUR_rate = 1.14
        out_money = in_money * data_GBP_to_EUR_rate
        print(out_money, "EUR")
    elif out_currency == "USD":
        in_money = int(input("Enter money: "))
        data_GBP_to_USD_rate = 1.24
        out_money = in_money * data_GBP_to_USD_rate
        print(out_money, "USD")
    else:
        print("Currency for conversion was entered incorrectly!")
else:
    print("The currency is not entered correctly!")
