class publisher:
    def get_publisher(self):
            self.pub=input("publisher :")
    def display_publisher(self):
            print("publisher :",self.pub)

class book(publisher):
    def get_book(self):
        self.title=input("enter title :")
        self.author=input("author :")
    def display_book(self):
        print("title :",self.title)
        print("author : ",self.author)

class python(book):
    def get_python(self):
        self.price=input("price of book :")
        self.page=input("no of pages :")
    def display_python(self):
        print("price :",self.price)
        print("no of page :",self.page)


b=python()
b.get_publisher()
b.get_book()
b.get_python()
b.display_publisher()
b.display_book()
b.display_python()
    

