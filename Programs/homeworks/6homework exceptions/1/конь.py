x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2) # модуль разницы координат X
dy = abs(y1 - y2) # модуль разницы координат Y
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
# если разность X1 и X2 равна одной клетке а Y1 и Y2 двум или наоборот X1 и Y1
# двум клектам а Y1 и Y2 одной клетке то выводим на экран YES
    print('YES')
else:
    print('NO')
