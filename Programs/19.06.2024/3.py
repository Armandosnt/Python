class Animal:
    def speak(self):
        print("Животное говорит")

    def speak(self):
        print("Не Гав")    

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Гав")
        
dog = Dog()
dog.speak()  