#Multilevel Inheritance
class Grandfather: 
    grandfathername =""  
    def grandfather(self): 
        print(self.grandfathername) 
  
# Intermediate class 
class Father(Grandfather): 
    fathername = "" 
    def father(self): 
        print(self.fathername) 
  
# Derived class 
class Son(Father): 
    def parent(self): 
        print("GrandFather :", self.grandfathername) 
        print("Father :", self.fathername) 
  
# Driver's code 
s1 = Son() 
s1.grandfathername = "Srinivas"
s1.fathername = "Ankush"
s1.parent() 
