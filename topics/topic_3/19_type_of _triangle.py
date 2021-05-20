def triangle(a, b, c):
    c1 = a
    if c1 < b:
        c1 = b
    if c1 < c:
        c1 = c
    if c1 >= a + b:
        print("impossible")
    if (a*a + b*b == c1*c1) or (a*a + c1*c1 == b*b) or (c1*c1 + b*b == a*a):
        print("rectangular")
    elif (a*a + b*b < c*c) or (a*a + c1*c1 < b*b) or (c1*c1 + b*b < a*a):
        print("obtuse")
    else:
        print("acute")


triangle(int(input()), int(input()), int(input()))
