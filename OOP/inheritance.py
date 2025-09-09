class Pet:
    def __init__(self,name:str,age:int)-> None:
        self.name = name
        self.age = age

    def show(self)-> None:
        print(f'Name: {self.name}, Age: {self.age}')
    def speak(self)-> None:
        print("I dont know what I say")
        

class Cat(Pet):

    def __init__(self,name: str,age:int,color:str)-> None:
        super().__init__(name,age)
        self.color= color
    def speak(self):
        print("Meow")

    
    def show(self)-> None:
        if self.color:
            print(f'Name: {self.name}, Age: {self.age} and color: {self.color}')
    


class Dog(Pet):
        

    def speak(self):
        print("Woof")



s1= Dog("Toby",4)
s2= Cat("Kitty",2,"Black")

s1.show()
s2.show()
s1.speak()  
s2.speak()



    