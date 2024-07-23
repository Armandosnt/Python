# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self) -> float:
#         pass
    
#     @abstractmethod
#     def perimeter(self) -> float:
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (self.radius ** 2) * 3.14

#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def perimeter(self):
#         return 4 * self.side


# def print_shape_info(shape:Shape):
#     print(f"Area = {shape.area()}, perimeter = {shape.perimeter()}")


# wheel = Circle(5)
# table = Square(5)

# # print_shape_info(wheel)
# # print_shape_info(table)


# class House:
#     def __init__(self, capacity):
#         self.capacity = capacity
        
#     def __add__(self, other):
#         return House(self.capacity + other.capacity)
#     def __mul__(self, other):
#         return "House can not be multiplied by another house"
    
# A = House(10)
# B = House(15)
# C = A + B
# print( A * B )



class Vehicle:
    year = 0
    def __init__(self, brand, year, color, country):
        self.brand = brand
        self.year = year
        self.color = color
        self.country = country
        
    def info(self):
        return f"{self.brand} ({self.year})"
    
    
        
class Car(Vehicle):
    def __init__(self, brand, year, color, country, num_of_wheels, horse_power):
        super().__init__(brand, year, color, country)
        self.num_of_wheels = num_of_wheels
        self.horse_power = horse_power
        
    def info(self):
        info = super().info()
        return info + " " + f"{self.horse_power}" 
        
lamb_v = Vehicle('Lamborgini', 2020, 'red', 'Italy')
lamb_c = Car('Lamborgini', 2020, 'red', 'Italy', 4, 400)

print(lamb_v.info())
print(lamb_c.info())

