#1. Use a function to Square a Number
# Write a function square(x) that returns the square of a number.
def square_number(num):
    return num ** 2
result = square_number(-5)
print("The square of the number is:", result)

#2. Greet a User
#Write a function greet(name="Friend") that prints a message like: Hello, [name]!
def greet_user(name ="Friend"):
    print(f"Hello, {name}!")
greet_user()
greet_user("Sara") 

#3. Add Two Numbers by using functions
#Create a function add(a, b) that returns the sum of a and b.
def add_numbers(num1, num2):
    return(num1 + num2)
result1 = add_numbers(10, 20)
print("The sum of the two numbers is:", result1)
result2 = add_numbers(5, 15)
print("The sum of the two numbers is:", result2) 

#4. Check if a number is Even or Odd
# Write a function check_even_odd(num) that prints whether a number is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        return (f"{num} is an Even number.")
    else:
        return (f"{num} is an odd number.")
result = check_even_odd(10)
print(result) 

#5. Sum Any Number of Inputs
# Create a function sum_all(*args) that takes any number of numbers and returns their total.
def sum_numbers(*args):
    return sum(args)
result1 = sum_numbers(1, 2, 3, 4, 5)
print("The sum of the numbers is:", result1)
result2 = sum_numbers(10, 20, 30)
print("The sum of the numbers is:", result2) 

#6 Print Keyword Info
# Write a function print_user_info(**kwargs) that prints user info like name, age, etc., based on keyword arguments.
def print_keyword_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_keyword_info(name="Ali", age=30, city="Bahawalpur") 

#7. Find the Maximum of Three Numbers
# Make a function find_max(a, b, c) that returns the largest of the three numbers.
def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)
result = find_maximum(10, 20, 15)
print("The maximum number is:", result) 

#8. Create a Menu Function
# Create a function menu(item="Tea") that prints You selected [item]. Test with menu() and menu("Coffee")
def menu(item = "Tea"):
    return(f" You selected {item}.")
result1 = menu()
print(result1)
result2 = menu("Coffee")
print(result2) 

#9. Multiplication Table
# Make a function table(n) that prints the multiplication table of a number up to 10
def multiplication_table(n):
    print(f"Multiplication Table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
multiplication_table(12) 

#10. Reverse Strings from Variable-Length Input
#Write a function reverse_strings(*args) that takes multiple words and prints each in reverse.
def reverse_strings(*args):
    for word in args:
        print(word[::-1])
reverse_strings("hello", "world", "Python", "functions")

