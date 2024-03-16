class Animal:
    # Attributes and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")

class Dog(Animal):
    # New method in the subclass
    def display(self):
        # Access the name attribute of the superclass using 'self'
        print("My name is", self.name)

# Create an object of the subclass
labrador = Dog()

# Set the name attribute
labrador.name = "Rohu"

# Call superclass method
labrador.eat()

# Call subclass method
labrador.display()
