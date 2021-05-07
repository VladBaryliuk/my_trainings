import math


def motor_rally(n, m):
    t = m / n
    t = math.ceil(t)
    print(t)


motor_rally(int(input()), int(input()))
