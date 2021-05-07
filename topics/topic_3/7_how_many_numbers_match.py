def how_many_numbers_match(number1, number2, number3):
    list_of_numbers = [number1, number2, number3]
    matched_numbers = []
    index = 0
    index2 = 1
    help_variable = list_of_numbers[index]
    help_variable2 = list_of_numbers[index2]
    for i in range(len(list_of_numbers)):
        if help_variable2 == help_variable:
            matched_numbers.append(i)
        index += 1
        index2 += 1
        if index < len(list_of_numbers):
            help_variable = list_of_numbers[index]
            if index2 < len(list_of_numbers):
                help_variable2 = list_of_numbers[index2]
            else:
                help_variable2 = list_of_numbers[0]
    if len(matched_numbers) == 1:
        print(2)
    if len(matched_numbers) == 2:
        print(3)
    if len(matched_numbers) == 3:
        print(3)
    if len(matched_numbers) == 0:
        print(0)



how_many_numbers_match(int(input()), int(input()), int(input()))