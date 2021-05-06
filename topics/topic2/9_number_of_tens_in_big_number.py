def number_of_tens(number):
    number = str(number)
    while len(number) > 2:
        number_to_del = number[0]
        number = number.replace(number_to_del, "")
    number = int(number)
    print(number // 10)
number_of_tens(int(input()))
