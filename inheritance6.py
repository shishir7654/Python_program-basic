class Child:

    # constructor
    def __init__(self , name):
        self.name = name

    # get name
    def getName(self):
        return self.name

    # check if this Person is student

    def isStudent(self):
        return False


    #Detrive class

class Student(Child):

    def isStudent(self):
        return True

std = Child("Ram")
print(std.getName(),std.isStudent())

std = Student("Shishir")
print(std.getName(),std.isStudent())


