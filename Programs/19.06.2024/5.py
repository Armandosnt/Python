class Pet:
  def __init__(self, sound ,name, type):
    self.name = name
    self.type = type
    self.sound = sound
    
class Dog(Pet):
  
  def __init__(self, name, type):
        super().__init__(
        sound = "Гав",
        name = name,
        type = type
        )

class Cat(Pet):

  def __init__(self, name, type ):
        super().__init__(
        sound = "Мяу",
        name = name,
        type = type
        )

class Parrot(Pet):

  def __init__(self, name, type ):
        super().__init__(
        sound = "Я попугай",
        name = name,
        type = type
        )

class Hamster(Pet):

  def __init__(self, name, type):
        super().__init__(
        sound = "Пи",
        name = name,
        type = type
        )

dog = Dog() 
print(dog())
cat = Cat() 
print(cat())
parrot = Parrot() 
print(Parrot())
hamster = Hamster() 
print(Hamster())





