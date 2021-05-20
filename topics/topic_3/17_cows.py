def cows(number):
    if number == 1 or number % 10 == 1 and number != 11:
        print(number, "korova")
    elif 1 < number % 10 < 5 and (number < 11 or number > 15):
        print(number, "korovy")
    else:
        print(number, "korov")


cows(int(input()))
