def rook_move(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        print('YES')
    else:
        print('NO')


rook_move(int(input()), int(input()), int(input()), int(input()))