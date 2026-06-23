# Q1. Print all Python keywords
print("Q1")
import keyword
print(keyword.kwlist)

# Q2. Create a variable x = 10 and print its type
print("\nQ2")
x = 10
print("Value of x:", x)
print("Type of x:", type(x))

# Q3. Create a tuple with 4 numbers and print its last and second element
print("\nQ3")
t = (10, 20, 30, 40)
print("Last element:", t[-1])
print("Second element:", t[1])

# Q4. Convert string "123" into an integer and add 10
print("\nQ4")
num = int("123")
result = num + 10
print("Result:", result)

# Q5. Convert a float number into an integer
print("\nQ5")
f = 12.75
print("Float value:", f)
print("Integer value:", int(f))

# Q6. Join strings "Hello" and "World" and find length
print("\nQ6")
new_string = "Hello" + " " + "World"
print("Joined String:", new_string)
print("Length:", len(new_string))

# Q7. Create boolean variable flag = True and print its type
print("\nQ7")
flag = True
print("Flag:", flag)
print("Type:", type(flag))

# Q8. Find length of a tuple
print("\nQ8")
t2 = (10, 20, 30, 40, 50)
print("Length of tuple:", len(t2))

# Q9. Create "Python3.13" using variables
print("\nQ9")
language = "Python"
version = 3.13
result = language + str(version)
print(result)

# Q10. Accept user inputs and calculate percentage
print("\nQ10")

student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course_name = input("Enter Course Name: ")

marks1 = float(input("Enter Marks in Subject 1: "))
marks2 = float(input("Enter Marks in Subject 2: "))
marks3 = float(input("Enter Marks in Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\nStudent Details")
print("Name:", student_name)
print("Age:", age)
print("City:", city)
print("Course:", course_name)
print("Percentage:", percentage)

# Q11. List operations
print("\nQ11")

subjects = ["Python", "SQL", "Excel", "Tableau"]

# a
print("Complete List:", subjects)

# b
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

# c
subjects.insert(1, "Power BI")
print("After Inserting:", subjects)

# d
subjects.remove("Excel")
print("After Deleting Excel:", subjects)

# e
new_list = subjects.copy()
print("Copied List:", new_list)

# f
new_list.sort()
print("Sorted List:", new_list)

# g
print("Is Excel present?", "Excel" in new_list)

# Q12. Logical operators
print("\nQ12")

attendance = True
assignment_submitted = False

# a
print("To get True:", attendance or assignment_submitted)

# b
print("To get False:", attendance and assignment_submitted)

# c
print("False value of attendance:", not attendance)