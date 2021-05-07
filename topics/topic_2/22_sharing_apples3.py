import math

def sharing_apples(n, k):
    col = k / n
    col = math.ceil(col)
    col2 = col * n
    col2 -= k
    print(col2)
sharing_apples(int(input()), int(input()))