#CODECLAUSE PVT LTD
#Python Development Intern
#August-2023
#Task-2
'''Calculator in Python'''

#SOURCE CODE
# Function to perform addition
def add(numbers):
    return sum(numbers)

# Function to perform subtraction


def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# Function to perform multiplication


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Function to perform division


def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Cannot divide by zero"
        result /= num
    return result

# Main calculator function


def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Quitting calculator...")
            break

        num_count = int(input("Enter the number of numbers: "))
        numbers = []
        for i in range(num_count):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)

        if choice == '1':
            print("Result:", add(numbers))
        elif choice == '2':
            print("Result:", subtract(numbers))
        elif choice == '3':
            print("Result:", multiply(numbers))
        elif choice == '4':
            print("Result:", divide(numbers))
        else:
            print("Invalid input")


# Run the calculator
calculator()

#OUTPUT FORMAT
'''Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit
Enter choice (1/2/3/4/5): 1
Enter the number of numbers: 5
Enter number 1: 7
Enter number 2: 9
Enter number 3: 8
Enter number 4: 4
Enter number 5: 0
Result: 28.0
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit
Enter choice (1/2/3/4/5): 2
Enter the number of numbers: 3
Enter number 1: 80
Enter number 2: 65
Enter number 3: 32
Result: -17.0
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit
Enter choice (1/2/3/4/5): 5
Quitting calculator...'''
