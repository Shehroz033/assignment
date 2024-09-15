
# Python Programs

## 1. Sum of Two Numbers
```python
num1 = int (input("enter num1 :"))
num2 = int(input("enter num2 :"))
# adding two numbers given by user
sum = num1 + num2
# printing sum of two numbers given by user
print("The sum of ", num1, " and ", num2, " is ", sum)
```

## 2. Favourite Animal
```python
# taking input from user to print favourite animal
animal = (input("what is your favourite animal "))

# printing user favourite animal
print("my favourite animal is also", animal, "!")
```

## 3. Convert Fahrenheit to Celsius
```python
# taking input from user in fahrenheit
fahrenheit = float(input("Enter temperature in fahrenheit: "))

# converting fahrenheit into celsius
celsius = (fahrenheit - 32) * 5/9

# displaying the result
print(f"Temperature in Fahrenheit: {fahrenheit}°F | Temperature in Celsius: {celsius:.2f}°C")
```

## 4. Perimeter of Triangle
```python
# taking input from user for the sides of the triangle
side1 = float(input("Enter first side of triangle: "))
side2 = float(input("Enter second side of triangle: "))
side3 = float(input("Enter third side of triangle: "))

# calculating the perimeter
perimeter = side1 + side2 + side3

# printing the perimeter of triangle
print("The perimeter of triangle is: ", perimeter)
```

## 5. Square of a Number
```python
# taking input from user
number = int(input("Enter the number: "))

# calculating the square
num = number ** 2

# printing the square of the number
print("The square of", number, "is:", num)
```

## 6. Removing a Number from a List
```python
# create list
numbers = [1, 2, 3, 4, 5]

# remove the number 3
numbers.remove(3)

# print the updated list
print(numbers)
```

## 7. Adding List2 to List1
```python
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# add list2 to list1
list1.extend(list2)

# print the new list
print(list1)
```

## 8. Pop Method in Lists
```python
# initial list
list = [20, 30, 40, 50] 

# remove and print last number
removed_item = list.pop()

# print the updated list and removed item
print("Updated list:", list)
print("Removed item:", removed_item)
```

## 9. Index of 'Green' in List
```python
# create list 
colors = ['red', 'blue', 'green', 'yellow']

# print the index of 'green' 
index_of_green = colors.index("green")

# print index of green
print("The index of 'green' is", index_of_green)
```

## 10. Last Number in List
```python
# create list
list = [1, 2, 3, 4]

# print the last number in the list
print(list[-1])
```
