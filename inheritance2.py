class Animal:
    def speak(self):
        print("Animal Speaking")

#child class Dog inherits the base Animal

class Dog(Animal):
    def bark(self):
        print("dog is barking")
d = Dog()
d.bark()
d.speak()
