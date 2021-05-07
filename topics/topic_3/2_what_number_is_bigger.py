def what_number_is_bigger(number1, number2):
    if number1 > number2:
        print(1)
    elif number2 > number1:
        print(2)
    else:
        print(0)
what_number_is_bigger(int(input()), int(input()))