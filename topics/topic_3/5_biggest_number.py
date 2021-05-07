def the_biggest_number(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c>b:
        print(c)
    else:
        print(a)

the_biggest_number(int(input()), int(input()), int(input()))
