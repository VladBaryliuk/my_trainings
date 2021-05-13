def elephant_move(x1, y1, x2, y2):
    if abs(x1 - x2) == abs(y1 - y2):
        print('YES')
    else:
        print('NO')


elephant_move(int(input()), int(input()), int(input()), int(input()))