# тут ввод с клавиатуры нужных координат для оси x первой клеточки
x1 = int(input())

# ввод с клавиатуры нужных координат для оси y первой клеточки
y1 = int(input())

# ввод с клавиатуры нужных координат для оси x второй клеточки
x2 = int(input())

# ввод с клавиатуры нужных координат для оси y второй клеточки
y2 = int(input())

# когда ладья ходит, координата по одной из осей не меняется
# (если не понятно, нарисуйте шахматную доску и подпишите координаты клеточек)
if x1 == x2 or y1 == y2:
    print('YES') 
else:
    print('NO')