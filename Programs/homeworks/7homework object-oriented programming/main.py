# class Fruit:
#     pass

# a = Fruit()
# b = Fruit()

# a.name = 'Apple'
# a.color = 'Red'
# b.name = 'Banana'
# b.color = 'Yellow'
# print(b.color)




# class Pet:
#     name = ""
    
#     def make_sound(self):
#         print(f"Hello, my name is")
        
# cat = Pet()
# cat.name = "Murzik"
# cat.make_sound()
# dog = Pet()
# dog.name = "Sharik"
# dog.make_sound()



# class Kassa:
#     def pay(self, amount:int):
#         """This is pay method"""
#         print(f"You have paid {amount} tenge")
        
#     def get_change(self, amount:int, price:int):
#         """This is get_change method"""
#         if amount == price:
#             print("You dont have a change")
#         elif price > amount:
#             print("This amount is not enough")
#         else:
#             print(f"You have got {amount-price} tenge change")

# test = Kassa()

# test.pay("5000")
# test.get_change(5000, 3000)


# class Human:
#     def __init__(self, name, age, race, gender, height, weight):
#         self.name = name
#         self.age = age
#         self.race = race
#         self.gender = gender
#         self.height = height
#         self.weight = weight

# ivan = Human("name", 37, "Негоид", "Мужской", 180, 75)

# print(ivan.name)


class Car:
    def __init__(self, model):
        self.__model = model
        
    def get_model(self):
        print(self.__model)
        
kia = Car('Sportage')



# class User:
#     def __init__(self, username, password, email) -> None:
#         self.username = username
#         self.__email = email 
#         self.__password = password
        
# test_user = User('test1', 'test1@gmail.com', 'Str0ngPa$$word!')

# print(test_user.__email)