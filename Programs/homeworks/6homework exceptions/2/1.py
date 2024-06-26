def plus_two(x):
    if (type(x) is int) or (type(x) is float):
        return x+2
    else:
        raise ValueError("Неверный тип данных")
        
print(plus_two(5))
print(plus_two("aaa"))