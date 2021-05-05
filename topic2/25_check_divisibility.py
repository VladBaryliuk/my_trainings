def check_divisibility(n, m):
    if n % m == 0 or m % n == 0:
        print(1)
    else:
        print(2)


check_divisibility(int(input()), int(input()))