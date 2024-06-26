lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
 
# ловим границу
for i in range(len(lst)):
    try:
        print('сравниваем {} и {} => {}'.format(lst[i], lst[i+1], lst[i] == lst[i+1]))
    except IndexError:
        print(i+1, 'это заграница ;)')
print('последний легальный индекс', i)
 
# без try
# simple
print('простая проверка:', 'все одинаковые' if len(set(lst)) == 1 else 'разные')
 
# not simple
def show(i, j, msg):
    print('элементы списка с индексами {} и {} {}'.format(i, j, msg))
 
for i in range(1, len(lst)):
    if lst[i-1] == lst[i]:
        show(i-1, i, 'одинаковые')
    else:
        show(i-1, i, 'разные')
        print('detected different elements in list')
        break
else:
    print('list is ok')