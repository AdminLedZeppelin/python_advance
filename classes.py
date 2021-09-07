class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know what to say")
    
class Cat(Pet):
    def  __init__(self, name, age, color):  /*calling parent class. */
        super().__init__(name, age)
        self.color = color
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")    
    def speak(self):
        print("Meow")
    
class Dog(Pet):
    def speak(self):
        print("Bark")
        
c = Cat("Bill", 15, "Yellow")
d = Dog("John", 10)
c.show()
d.show()

class Fish(Pet):
    pass

f = Fish("ZYT", 19)
f.speak()
