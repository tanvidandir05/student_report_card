name = str(input("Enter your name:"))
maths = float(input("Enter your maths marks:"))
chemistry = float(input("Enter your chemistry marks:"))
physics = float(input("Enter your physics marks:"))
if (maths < 0 or maths > 100 or
    chemistry < 0 or chemistry > 100 or 
    physics < 0 or physics > 100):
    print("Invalid Marks! Enter marks between 0 and 100.")
else:
    print("Marks are valid!")

    total_marks = (maths + chemistry + physics)
    average_marks = (total_marks / 3)

    print("Student Report Card")
    print("Name:", name)
    print("Maths Marks:", maths)
    print("Chemistry Marks:", chemistry)
    print("Physics Marks:", physics)
    print("Total_Marks:", total_marks)
    print("Average_Marks:", average_marks)

    if average_marks >= 90:
        grade = "A+"
    elif average_marks >= 80:
        grade = "A"
    elif average_marks >= 70:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    elif average_marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    if maths >= 40 and chemistry >= 40 and physics >= 40:
        result = "PASS"
    else:
        result = "FAIL"
       
    print("Result:", result)