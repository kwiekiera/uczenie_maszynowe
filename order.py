from employee import Employee
from student import Student

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