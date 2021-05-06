def the_last_number(number):
    number = str(number)
    number_list = []
    for i in number:
        number_list.append(i)
    print(number_list[-1])
the_last_number(int(input()))
