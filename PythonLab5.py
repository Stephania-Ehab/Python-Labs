class Animal:
    def __init__(self):
        pass
    def sleep (self):
        print ("I can sleep in my bed")
    def eat (self):
        print ("I can eat eveywhere")
    def speak (self):
        print("My sound is very unique")
    def move (self):
        print ("I can move on four legs")
    def live (self):
        print ("I can live in .....")

class Cat (Animal):
    def __init__(self):
        super().__init__()
    def meow (self):
        print ("Meow Meow Meow")
    def eat(self):
        print ("I can eat fish, vegatables, fruits, meats")
    def live(self):
        print ("I can live with human")
    

# Example 

print("\nCat:")

whiskers = Cat()
whiskers.sleep()   
whiskers.eat()     
whiskers.move()    
whiskers.live()
whiskers.meow()