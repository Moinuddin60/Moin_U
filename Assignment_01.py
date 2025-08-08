# First problem

numbers = int(input("Enter a number: "))

if numbers % 2 == 0:
    print(f"{numbers} is an Even Number.")
else:
    print(f"{numbers} is an Odd Number.")

# Second Problem

    
number_1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
number_2 = float(input("Enter the second number: "))

if operator == '+':
    result = number_1 + number_2
    print(f"The result is: {result}")
elif operator == '-':
    result = number_1 - number_2
    print(f"The result is: {result}")
elif operator == '*':
    result = number_1 * number_2
    print(f"The result is: {result}")
elif operator == '/':
    if number_2 != 0:
        result = number_1 / number_2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please use one of +, -, *, /.")


# Third problem

sum_of_even_number = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum_of_even_number += number

print("The sum of even numbers from 1 to 100 is:", sum_of_even_number)