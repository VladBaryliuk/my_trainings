def queen_move(x1, y1, x2, y2):
    if abs(x1-x2) <= 1 and abs(y1-y2) <= 1 or x1 == x2 or y1 == y2:
        print('YES')
    else:
        print('NO')

queen_move(int(input()), int(input()), int(input()), int(input()))
