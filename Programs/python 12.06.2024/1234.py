class Car:
    mark = ""
    model = ""
    year = ""
    def get_info1(self):
        print(f"Марка:{self.mark} ") 
    def get_info2(self):
        print(f"Модель:{self.model}") 
    def get_info3(self):
        print(f"Год выпуска:{self.year}") 
              
Description = Car()
Description.mark = "Toyota"
Description.get_info1()
Description = Car()
Description.model = "Camry"
Description.get_info2()
Description = Car()
Description.year = "1997"
Description.get_info3()




