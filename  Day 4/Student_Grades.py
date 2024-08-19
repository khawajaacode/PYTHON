students = (("Alice", "A"), ("Bob", "B"), ("Charlie", "C"))

def find_grade(student_name):
    for student in students:
        if student[0].lower() == student_name.lower():
            return student[1]
    return None

def main():
    student_name = input("What is your name? ")
    grade = find_grade(student_name)

    if grade:
        print(f"{student_name} has a grade of {grade}")
    else:
        print(f"Sorry, {student_name} has no grade")

if __name__ == '__main__':
    main()
