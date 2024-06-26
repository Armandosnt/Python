class Stadium:

   def __init__(self):

       self.name = ""

       self.opening_date =  ""

       self.country =  ""

       self.city =  ""

       self.capacity =  ""

   

   def input_data(self):

       self.name = input("Enter stadium name: ")

       self.opening_date = input("Enter opening date: ")

       self.country = input("Enter country: ")

       self.city = input("Enter city: ")

       self.capacity = input("Enter capacity: ")

   

   def print_data(self):

       print(f"Stadium name: {self.name}")

       print(f"Opening date: {self.opening_date}")

       print(f"Country: {self.country}")

       print(f"City: {self.city}")

       print(f"Capacity: {self.capacity}")

   

   def get_name(self):

       return self.name

   

   def set_name(self, name):

       self.name = name

   

   def get_opening_date(self):

       return self.opening_date

   

   def set_opening_date(self, opening_date):

       self.opening_date = opening_date

   

   def get_country(self):

       return self.country

   

   def set_country(self, country):

       self.country = country

   

   def get_city(self):

       return self.city

   

   def set_city(self, city):

       self.city = city

   

   def get_capacity(self):

       return self.capacity

   

   def set_capacity(self, capacity):

       self.capacity = capacity
       
       
book = Stadium()

book.input_data()

book.print_data()