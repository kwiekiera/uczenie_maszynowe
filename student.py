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