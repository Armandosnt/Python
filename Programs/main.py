my_set = {1, 2, 3, 4, 5, "CS", "John"} 

print("До обновления: ", my_set ) 

data = input("Введите данные через пробел: ").split()
data = set(data)
data.update(my_set)
print(data)
