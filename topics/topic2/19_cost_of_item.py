def cost_of_item(a, b, n):
    a = a * n
    b = b * n
    while b >= 100:
        a += 1
        b -= 100
    print(a, b)
cost_of_item(int(input()), int(input()), int(input()))