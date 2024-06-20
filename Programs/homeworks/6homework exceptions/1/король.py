# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#     print('YES')
# else:
#     print('NO')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1-x2 == 1 or x1-x2  == -1 or x1-x2  == 0) and (y1-y2 == 1 or y1-y2 == -1 or y1-y2 == 0):
    print ('YES')
else:
    print ('NO')
