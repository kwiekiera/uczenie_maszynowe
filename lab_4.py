# Zad 1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        marks = ""
        for i in range(len(self.marks)):
            marks += str(self.marks[i]) + ", "
        return "Imię: {}\nOceny: {}".format(self.name, marks)

    def is_passed(self):
        sum = 0
        for i in range(len(self.marks)):
            sum += self.marks[i]
        return sum/len(self.marks) > 50


student1 = Student('zdający', [80, 99, 49])
print(student1.is_passed())
student2 = Student('niezdający', [60, 30, 20])
print(student2.is_passed())


# Zad 2

class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return "Miasto: {}\nUlica: {}\nKod pocztowy: {}\nGodziny otwarcia: {}\nNr telefonu: {}".format(
            self.city, self.street, self.zip_code, self.open_hours, self.phone)


class Employee:

    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return "Imię: {}\nNazwisko: {}\nData zatrudnienia: {}\nData urodzenia: {}\nMiasto: {}\nUlica: {}\nKod pocztowy: {}\nNr telefonu: {}".format(
            self.first_name, self.last_name, self.hire_date, self.birth_date, self.city, self.street, self.zip_code, self.phone)


class Book:
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return "Biblioteka: {}\n\nData publikacji: {}\nImię autora: {}\nNazwisko autora: {}\nLiczba stron: {}".format(
            self.library.__str__(), self.publication_date, self.author_name, self.author_surname, self.number_of_pages)


class Order:
    def __init__(self, employee: Employee, student: Student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books = ""
        for i in range(len(self.books)):
            books += "\n"
            books += self.books[i].__str__()
            books += "\n"
        return "Pracownik: \n{}\n\nStudent: \n{}\n\nKsiążki:\n {}\nData zamówiennia: {}".format(
            self.employee.__str__(), self.student.__str__(), books, self.order_date)


library1 = Library("Katowice", "Adamskiego", "40-069", "9-18", "123456789")
library2 = Library("Warszawa", "Złota", "00-120", "8-17", "112233445")
book1 = Book(library1, "01-01-1980", "Henryk", "Sienkiewicz", 120)
book2 = Book(library1, "02-01-1989", "Stephen", "King", 230)
book3 = Book(library1, "01-01-2015", "Remigiusz", "Mróz", 300)
book4 = Book(library2, "11-09-1970", "J. R. R.", "Tolkien", 500)
book5 = Book(library1, "01-11-2010", "J. K.", "Rowling", 400)
employee1 = Employee("Jan", "Drabina", "01-04-1994", "19-05-1974", "Katowice", "Adamskiego", "40-069", "987654321")
employee2 = Employee("Genowefa", "Burczybrzuch", "11-12-2019", "01.03.2001", "Warszawa", "Złota", "00-120", "012345678")
employee3 = Employee("Lucjan", "Malfoj", "08-11-2020", "22-09-1999", "Bytom", "Tysiąclecia", "41-33", "098765432")
student1 = Student("Anna", [60, 79, 90])
student2 = Student("Łukasz", [2, 100, 50])
student3 = Student("Martyna", [20, 11, 99])
order1 = Order(employee1, student2, [book1, book2, book3], "17-10-2022")
order2 = Order(employee2, student1, [book3, book4], "16-10-2021")
print(order1)
print(order2)


# Zad 3
class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return "Okolica: {}\nLiczba pokoi: {}\nCena: {}\nAdres: {}\n".format(
            self.area, self.rooms, self.price, self.address)


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + "Rozmiar działki: {}".format(self.plot)


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + "Piętro: {}".format(self.floor)


house = House("Koszutka", 3, 400000, "ul. Droga 15", 100)
flat = Flat("Nikiszowiec", 3, 200000, "ul. Tania 1", 2)
print(house)
print(flat)
