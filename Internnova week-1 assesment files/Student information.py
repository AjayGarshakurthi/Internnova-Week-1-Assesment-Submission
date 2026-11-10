# Task 5: Student Information Program

student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
student_age = int(input("Enter student age: "))
student_city = input("Enter student city: ")


print("\nEnter marks for four  subjects:")

subject1 = float(input("Enter Python marks: "))
subject2 = float(input("Enter C Programming marks: "))
subject3 = float(input("Enter Embedded C marks: "))
subject4 = float(input("Enter VLSI marks: "))

total_marks = subject1 + subject2 + subject3 + subject4
average_marks = total_marks / 4

# Calculating percentage
percentage = (total_marks / 300) * 100

# Displaying student information
print("\n========== STUDENT REPORT ==========")

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Age:", student_age)
print("City:", student_city)

print("\n---------- Academic Details ----------")

print("Python Marks:", subject1)
print("C Programming Marks:", subject2)
print(" Embedded C Marks:", subject3)
print("VLSI Marks:", subject4)


print("\nTotal Marks:", total_marks)
print("Average Marks:", round(average_marks, 2))
print("Percentage:", round(percentage, 2), "%")


if subject1 >= 35 and subject2 >= 35 and subject3 >= 35 and subject4 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("=====================================")