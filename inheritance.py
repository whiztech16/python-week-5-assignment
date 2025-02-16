class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True


        def eat(self):
            print(f"{self.name}is eating")

        def sleep(self):
              print(f"{self.name}is sleeping") 

class Dog(Animal):
    def speak(self):
        print("woof")
class cat(Animal):
     def speak(self):
          print("meow")
class Horse(Animal):
     def speak(self):
          print("kick")

dog = Dog("scoob")
cat= cat("meow")
horse=Horse("horse")
print(dog.name)
print(dog.is_alive)
horse.speak()
cat.speak