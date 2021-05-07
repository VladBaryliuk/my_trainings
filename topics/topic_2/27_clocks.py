def clocks(x, y, a, b, x2, y2):
    a = a - x
    b = b - y
    if b < 0:
        b = 60 + b
        a = a - 1
    if a < 0:
        a = 24 + a
    a2 = x2 + a
    b2 = y2 + b
    if b2 >= 60:
        b2 = b2 - 60
        a2 = a2 + 1
    if a2 >= 24:
        a2 = a2 - 24
    print(a2, b2)
clocks(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))