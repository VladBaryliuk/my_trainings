def sum_of_numbers(number):
    number = str(number)
    sum_of_numbers_variable = 0
    for i in number:
        i = int(i)
        sum_of_numbers_variable += i
    print(sum_of_numbers_variable)
sum_of_numbers(int(input()))
