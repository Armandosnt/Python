from random import randint

N = 10
array = [ ]

for number in range(N):
      array.append(randint(1,99))
array.sort()
print(array)


#Модуль re - regular expressions регулярные выражения