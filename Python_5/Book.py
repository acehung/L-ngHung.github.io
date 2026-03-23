class Book :
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} , {self.author} ({self.year})"
my_Book = Book("Số đỏ", "Vũ Trọng Phụng", 1936)
print(my_Book)
my_Book = Book("Nỗi buồn chiến tranh", "Kim Lân", 1990)
print(my_Book)