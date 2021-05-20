def swimming(N, M, x, y):
    temp_x = N - x
    temp_y = M - y
    if temp_x > x:
        temp_x = x
    if temp_y > y:
        temp_y = y

    if temp_y < 0 or temp_x < 0 or N == 0 or M == 0 or x == 0 or y == 0:
        print(0)
    elif temp_x > temp_y:
        print(temp_y)
    elif temp_x < temp_y:
        print(temp_x)

swimming(int(input()), int(input()), int(input()), int(input()))
