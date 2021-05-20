def tickets(n):
    number1 = 0
    number10 = 0
    number60 = 0

    while n > 0:
        if n > 34:
            number60 += 1
            n -= 60
        elif n > 8 and n <= 34:
            number10 += 1
            n -= 10
        elif n >= 1 and n <= 8:
            number1 += 1
            n -= 1

    print(number1, number10, number60)

tickets(int(input()))