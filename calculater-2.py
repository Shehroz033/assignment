# calculator in python using functions
# addition function 

def add(x,y):
    return(x+y)

# subtraction function

def subtract(x,y):
    return(x-y)

# multiplication function

def multiply(x,y):
    return(x*y)

# division function

def dividing(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
    
# modulation function    

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x % y


num1 = float(input("Enter the num 1 : "))
num2 = float(input("Enter the num 2 : "))
 
 #selecting the operation

operation = input("Choose an operation (+, -, *, /, %): ")

# performing the selected operation

if operation == "+":
    print(f"Result: {add(num1, num2)}")
elif operation == "-":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "*":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "/":
    print(f"Result: {dividing(num1, num2)}")
elif operation == "%":
    print(f"Result: {modulus(num1, num2)}")    
else:
    print("Invalid operation")