# class Time:
#     def __init__(self, minutes, seconds):
#         self.minutes = minutes
#         self.seconds = seconds
        
#     def __add__(self, other):
#         min = self.minutes + other.minutes
#         sec = self.seconds + other.seconds
#         min += sec // 60                    # Деление без остатка 10 // 3 = 3
#         sec = sec % 60                      # Остаток от деления  10 % 3 = 1
#         return Time(min, sec)
    
#     def __str__(self):
#         return f"Minutes: {self.minutes}\nSeconds: {self.seconds}"
    
# x = Time(8, 44)
# y = Time(3, 54)

# print(x + y)

# class Stdium:
#     def __init__(self, capacity):
#         self.capacity = capacity
    
#     def __eq__(self, other) -> bool:
#         if self.capacity == other.capacity:
#             return True
#         return False
        
# CapmNou = Stdium(75000)
# AlianzArena = Stdium(75000)

# print(CapmNou == AlianzArena)

# import datetime

# now = datetime.datetime.now()

# report = repr(now)

# print(report)

# class Ship:
#     """Class of the Ship object blah blah blah blah"""
#     def __init__(self, name, color, capacity):
#         self.name = name
#         self.color = color
#         self.capacity = capacity
        
#     def __repr__(self):
#         return f"Ship({self.name}, {self.color}, {self.capacity})"
    
    
# x = Ship('Frigat', 'white', 5000)
# report = repr(x)

# print(report)

# class Word:
#     def __init__(self, value):
#         self.value = value
        
#     # >
#     def __gt__(self, other):
#         return len(self.value) > len(other.value)
#     # <
#     def __lt__(self, other):
#         return len(self.value) < len(other.value)
#     # >=
#     def __ge__(self, other):
#         return len(self.value) >= len(other.value)
#     # <=
#     def __le__(self, other):
#         return len(self.value) <= len(other.value)
#     # ==
#     def __eq__(self, other):
#         return len(self.value) == len(other.value)
#     # !=
#     def __ne__(self, other):
#         return len(self.value) != len(other.value)


# a = Word("Hello")
# b = Word("World")

# print(a==b)

# import datetime

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @classmethod
#     def fromBirthYear(class_, name, year):
#         return class_(name, datetime.datetime.now().year - year)
    
#     @staticmethod
#     def isAdult(age):
#         return age > 18
    
# john = Person('John', 37)
# kate = Person.fromBirthYear('Kate', 1992)

# # print(kate.age)

# print(john.isAdult(john.age))


# class Plane:
#     counter = 0
    
#     def __init__(self, model, capacity):
#         self.model = model
#         self.capacity = capacity
#         Plane.counter += 1
        
#     @staticmethod
#     def get_counter():
#         return Plane.counter
#     @classmethod
#     def inc(class_, num):
#         return class_(num, num)
    

# x = Plane('Boeng 747', 250)
# a = Plane('Boeng 748', 2250)
# b = Plane('Boeng 749', 20)
# c = Plane('Boeng 746', 210)

# Plane.inc(10)

# print(x.capacity)

# x.inc()

# print(x.capacity)


class Point:
    counter = 0
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        Point.counter += 1
        
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self
        else:
            raise TypeError(f"Unable to add {other} to the {self} instance")
        
    def __str__(self):
        return f"{self.x}, {self.y}"
    
    @staticmethod
    def sum(*points):
        assert len(points) > 0, "Number of points are equal to 0!"
        
        result = 0
        
        for point in points:
            result += point
            
        return result
        
point = Point(4, 3)


try:
    x = Point.sum()
    print(x)
except AssertionError as e:
    print(f"Error: {e}")
    
    