class Animal: 
    def speak(self): 
        return "Some sound"
    
class Cat(Animal):
    def speak(self):
        return "Meow"

my_animal = Animal()
print(my_animal.speak())


my_cat = Cat()
print(my_cat.speak())