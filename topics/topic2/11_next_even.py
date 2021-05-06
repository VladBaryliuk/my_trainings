def next_even(number):
    if number % 2 == 0:
        number += 2
        print(number)
    else:
        number += 1
        print(number)
next_even(int(input()))
