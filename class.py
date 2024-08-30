
num1 = int (input("enter num1 :"))
num2 = int(input("enter num2 :"))
# adding two number given by user
sum = num1+num2
# printing sum of two number given by user
print("The sum of ",num1,"and",num2,"is",sum)

# new program of printing favourite animal of user

# taking input from user to print favourite animal
animal = (input("what is your favourite animal "))

# printing user favourite animal
print("my favourite animal is also",animal, "!")

# new program of converting fahrenheit into Celsius

# taking input from user in fahrenheit
fahrenheit = float(input("Enter temperature in fahrenheit: "))

# converting fahrenheit into celsius
celsius = (fahrenheit - 32) *5/9

# displaying the result
print(f"temperature in fahrenheit is: {fahrenheit} F temperature in celsius is: {celsius} C")

# new program of printing the perimeter of triangle
side1 = float(input("Enter first side of triangle :"))
side2 = float(input("Enter second side of triangle :"))
side3 = float(input("Enter third side of triangle :"))

# calculating the perimeter
perimeter = side1 + side2 + side3

# printing the perimeter of triangle
print("The perimeter of triangle is : ",perimeter)

# new program of printing squre of a number
number = int(input("Enter the number :"))

# calculating the square 
num = number ** 2

# printing the square of a number
print("The square of",number, "is :",num)

# new program of removing a number from list 
# create list
numbers = [1, 2, 3, 4, 5]

# Remove the number 3
numbers.remove(3)

# Print the updated list
print(numbers)

# new program of adding list2 in list1
list1 = [1,2,3,4]
list2 = [5,6,7,8]

# add list2 in list1
list1.extend(list2)

# print the new list 
print(list1)

# new program of using pop method

#initial list
list = [20,30,40,50] 

# remove and print last number
removed_item = list.pop()

# print the new list and removed list
print("updated list:", list)
print("removed item:", removed_item)

# new program of printing index of green 

# create list 
colors = ['red', 'blue', 'green', 'yellow']
# print the index of green 
index_of_green = colors.index("green")
# print index of green
print("The index of 'green' is ",index_of_green)

# new program of removing last number from list
list =[1,2,3,4]
# print the list 
print(list[-1])
