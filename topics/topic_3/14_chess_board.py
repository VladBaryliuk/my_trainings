def chess_board(x1, y1, x2, y2):
    if (x1 + y1 + x2 + y2) % 2 == 0:
        print('YES')
    else:
        print('NO')


chess_board(int(input()), int(input()), int(input()), int(input()))