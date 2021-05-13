def kings_move(x1, y1, x2, y2):
    if (x1-x2 == 1 or x1-x2  == -1 or x1-x2  == 0) and (y1-y2 == 1 or y1-y2 == -1 or y1-y2 == 0):
        print('YES')
    else:
        print('NO')
kings_move(int(input()), int(input()), int(input()), int(input()))