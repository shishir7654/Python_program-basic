# Python Non-Parameterized Constructor Example
class Student:
    def __init__(self):
        print("This is non parametized constructor")

    def show(self,name):
        print("Hello",name)
student = Student()
student.show("john")
