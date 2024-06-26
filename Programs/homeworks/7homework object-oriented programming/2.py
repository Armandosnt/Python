# class Book:

#    def __init__(self, book_name=None, year=None, publisher=None, genre=None, author=None, price=None):

#        self.book_name = book_name

#        self.year = year

#        self.publisher = publisher

#        self.genre = genre

#        self.author = author

#        self.price = price

#    def set_book_name(self, book_name):

#        self.book_name = book_name

#    def set_year(self, year):

#        self.year = year

#    def set_publisher(self, publisher):

#        self.publisher = publisher

#    def set_genre(self, genre):

#        self.genre = genre

#    def set_author(self, author):

#        self.author = author

#    def set_price(self, price):

#        self.price = price

#    def get_book_name(self):

#        return self.book_name

#    def get_year(self):

#        return self.year

#    def get_publisher(self):

#        return self.publisher

#    def get_genre(self):

#        return self.genre

#    def get_author(self):

#        return self.author

#    def get_price(self):

#        return self.price

#    def display_book_info(self):

#        print("Book name:", self.book_name)

#        print("Year:", self.year)

#        print("Publisher:", self.publisher)

#        print("Genre:", self.genre)

#        print("Author:", self.author)

#        print("Price:", self.price)

#    def input_book_info(self):

#        self.set_book_name(input("Enter book name: "))

#        self.set_year(input("Enter year of publication: "))

#        self.set_publisher(input("Enter publisher: "))

#        self.set_genre(input("Enter genre: "))

#        self.set_author(input("Enter author: "))

#        self.set_price(input("Enter price: "))
       

class Book:

    def __init__(self):

        self.book_name = ""

        self.year = ""

        self.publisher = ""

        self.genre = ""

        self.author = ""

        self.price = ""
        
        self.manufacturer = ""
        
        



    def set_model(self, book_name):

        self.book_name = book_name



    def set_year(self, year):

        self.year = year



    def set_publisher(self, publisher):

        self.publisher = publisher



    def set_genre(self, genre):

        self.genre= genre



    def set_author(self, author):

        self.author = author



    def set_price(self, price):

        self.price = price



    def get_book_name(self):

        return self.book_name



    def get_year(self):

        return self.year



    def get_publisher(self):

        return self.publisher



    def get_genre(self):

        return self.genre



    def get_author(self):

        return self.author



    def get_price(self):

        return self.price



    def input_data(self):

        self.model = input("Write Book name:")

        self.year = input("Write Year:")

        self.manufacturer = input("Write Publisher:")

        self.engine_capacity = input("Write Genre:")

        self.color = input("WriteAuthor:")

        self.price = input("Write Price:")



    def print_data(self):

        print("Book name:", self.model)

        print("Year:", self.year)

        print("Publisher:", self.manufacturer)

        print("Genre:", self.engine_capacity)

        print("Author:", self.color)

        print("Price:", self.price)





# Пример использования класса

book = Book()

book.input_data()

book.print_data()