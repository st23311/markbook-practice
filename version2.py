# Function to work out the grade
def calculate_grade(score):
    if score < 50:
        return "NA"
    elif score < 70:
        return "A"
    elif score < 90:
        return "M"
    else:
        return "E"


while True:
    # Get class details
    test_name = input("Enter test name: ")
    teacher_name = input("Enter teacher name: ")

    students = []

    number = int(input("How many students? "))

    # Enter student data
    for i in range(number):

        # Check name is not blank
        name = input("Student name: ")
        while name == "":
            print("Name cannot be blank.")
            name = input("Student name: ")

        # Check score is between 0 and 100
        score = int(input("Score: "))
        while score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            score = int(input("Score: "))

        students.append([name, score])

    # Calculate results
    total = 0
    highest = students[0]
    lowest = students[0]

    for student in students:
        total += student[1]

        if student[1] > highest[1]:
            highest = student

        if student[1] < lowest[1]:
            lowest = student

    average = total / len(students)

    # Display results
    print("\n" + test_name)
    print("Teacher:", teacher_name)
    print("---------------------------")
    print("Name\t\tScore\tGrade")

    for student in students:
        grade = calculate_grade(student[1])
        print(student[0], "\t", student[1], "\t", grade)

    print("---------------------------")
    print("Average:", round(average, 1))
    print("Highest:", highest[0], highest[1])
    print("Lowest:", lowest[0], lowest[1])

    again = input("\nAnalyse another class? (y/n): ")

    if again.lower() != "y":
        break