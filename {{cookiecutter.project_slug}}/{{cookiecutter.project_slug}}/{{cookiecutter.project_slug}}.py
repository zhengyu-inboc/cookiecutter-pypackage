"""Main module."""

def fun_sample(a,b):
    return a+b

class class_sample:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        class_sample.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % class_sample.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
