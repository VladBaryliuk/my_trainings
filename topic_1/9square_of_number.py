def square_of_number():
    number = "179"
    number_for_sum = "179"
    for i in range (49):
        number = number + number_for_sum
    number = int(number)
    number = number ** 2
    print(number)
square_of_number()
