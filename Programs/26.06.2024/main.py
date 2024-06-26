import openpyxl

class Dish:
    def __init__(self, name, price, ingredients, type):
        self.name =name
        self.price = price
        self.ingredients = ingredients
        self.type = type
        
    def __str__(self):
        return f"{self.name} ({self.type})-{self.price}$"

class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish) 
        return self.dish

    def remove_dish(self, dish):
        for d in self.dishes:
            if d.name == dish.name:
                self.dishes.remove(d)
                break

    def edit_dish(self,dish):
        for d in self.dishes:
            if d.name == dish.name:
                print("What do you want to update?")
                print("1. Name")
                print("2. Type")
                print("3. Ingredients")
                print("4. Price")
                choice = int(input(""))
                if choice == 1:
                    d.Name = input("New name")
                elif choice == 2:
                    d.type = input("New type: ")
                elif choice == 3:
                    d.Ingredients == input("New ingredients")
                elif choice == 4:
                    d.price = int(input("New price: "))
                break

    def get_dishes(self):
        for dish in self.dishes:
          print(dish)

class Order:
    id = 1
    def __init__(self):
        self.dishes = []
        Order.id += 1
        self.id = Order.id
        self.total_price = 0

    def add_dish(self, dish):
        self.dishes.append(dish)
        self.total_price += dish.price
        
    def checkout(self):
        wb = openpyxl.Workbook()  
        ws = wb.active
        ws.append(["Order ID", "Dish Name", "Price"])
        for dish in self.dishes:
            ws.append ([self.id, dish.name, dish.price])
        wb.save(f"order{self.id}.xlsx")    
        

pasta = Dish("Pasta", 10, ["pasta","tomato sauce"], "main course")
burger = Dish("Burger", 15, ["beef","buns"],"main course")

menu = Menu()
menu.add_dish(pasta)
menu.add_dish(burger)
menu.get_dishes(pasta)

menu.remove_dish(pasta)
menu.get_dishes(pasta)


# x = 10
# print(pasta)



