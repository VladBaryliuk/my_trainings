def chocolate(n, m, k):
    s = n * m
    if s / 2 == k or s == k or n + m == k or k == n or k == m:
        print("YES")
    elif k > s or s % 2 != 0:
        print("NO")
    else:
        print("NO")


chocolate(int(input()), int(input()), int(input()))
