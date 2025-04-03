# Python Basics Tutorial

# 1. Printing to the console
print("Welcome to Python Basics!")

# 2. Variables
name = "John"  # String variable
age = 30       # Integer variable
height = 5.9   # Float variable
is_student = True  # Boolean variable

print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

# 3. Data Types
# Strings
greeting = "Hello, World!"
print(greeting)

# Lists
fruits = ["Apple", "Banana", "Cherry"]
print(f"Fruits: {fruits}")

# Tuples (Immutable)
coordinates = (10.0, 20.0)
print(f"Coordinates: {coordinates}")

# Dictionaries (Key-Value pairs)
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person Info: {person}")

# 4. Control Structures
# Conditional Statements
if age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")

# Loops
# For loop
print("Fruits List:")
for fruit in fruits:
    print(f"- {fruit}")

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # Increment count

# 5. Functions
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

print(greet("Alice"))

def calculate_area_of_circle(radius):
    """Calculate the area of a circle given the radius."""
    import math
    area = math.pi * (radius ** 2)
    return area

print(f"Area of circle with radius 5: {calculate_area_of_circle(5):.2f}")

# 6. Exception Handling
try:
    x = int(input("Enter a number: "))
    print(f"You entered: {x}")
except ValueError:
    print("That's not a valid number!")

# 7. Classes and Objects
class Dog:
    """A simple Dog class."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# Creating an instance of Dog
my_dog = Dog("Buddy", 3)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
print(my_dog.bark())

# 8. File Handling
with open("example.txt", "w") as file:
    file.write("This is an example file.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# 9. Importing Libraries
import random

print("Random number between 1 and 10:", random.randint(1, 10))

# 10. List Comprehensions
squares = [x ** 2 for x in range(10)]
print(f"Squares: {squares}")

# 11. Lambda Functions
add = lambda x, y: x + y
print(f"Lambda add function result (3 + 5): {add(3, 5)}")

# End of Python Basics Tutorial
print("End of tutorial.")
