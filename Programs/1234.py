x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

def distance(x1, y1, x2, y2):
  catet1 = x2 - x1 if x2 > x1 else x1 - x2
  catet2 = y2 - y1 if y2 > y1 else y1 - y2
  hypotenuse = (catet1 * catet1 + catet2 * catet2) ** 0,5
  return hypotenuse

answer = distance(x1 ,y1, x2, y2) # Число
print(answer)
