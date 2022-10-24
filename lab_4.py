from student import Student
from library import Library
from employee import Employee
from book import Book
from order import Order
from house import House
from flat import Flat

# Zad 1

student1 = Student('zdający', [80, 99, 49])
print(student1.is_passed())
student2 = Student('niezdający', [60, 30, 20])
print(student2.is_passed())


# Zad 2

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

house = House("Koszutka", 3, 400000, "ul. Droga 15", 100)
flat = Flat("Nikiszowiec", 3, 200000, "ul. Tania 1", 2)
print(house)
print(flat)
