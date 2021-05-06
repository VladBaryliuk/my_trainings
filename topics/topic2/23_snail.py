def snail(h, a, b):
    now_high = 0
    d = 0
    while now_high < h:
        now_high += a
        if now_high < h:
            now_high -= b
        d += 1
    print(d)


snail(int(input()), int(input()), int(input()))

