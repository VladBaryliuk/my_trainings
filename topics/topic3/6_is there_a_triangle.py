def is_there_a_triangle(a, b, c):
    if a != b and a != c and b != c:
        print("Yes")
    else:
        print("NO")


is_there_a_triangle(int(input()), int(input()), int(input()))
