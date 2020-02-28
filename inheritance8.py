#Multiple Inheritance
class  Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)




class Father:
    fathername = ""
    def father(self):
        print(self.mothername)


class Son(Mother, Father):
    def parent(self):
        print("Father :", self.fathername)
        print(" Mother :",self.mothername)


s1 = Son()
s1.fathername = "Ram"
s1.mothername = "Sita"
s1.parent()
