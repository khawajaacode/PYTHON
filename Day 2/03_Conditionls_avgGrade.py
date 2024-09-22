grade1 = float( input("Enter First Grade : ") )
grade2 = float(input("Enter Second Grade : "))
absent = int(input("Enter Number of Absents: "))
total_classes = int(input("Enter Total Classes: "))

avg_grade = (grade1 + grade2)/2
attendence = (total_classes - absent)/total_classes

print("Average Grade : ", round(avg_grade,2))
print ("Attendance rate: ", str(round((attendence * 100),2))+'%')


if(avg_grade >= 6 and attendence >= 0.8):
    print("The Student has been Approved")
elif(avg_grade <= 6 and attendence <= 0.8):
    print("The Student has been Failed due to average grade less than 6 and attendance rate lower than 80% ")
elif(attendence >= 0.8):
    print("Student Failed due to Avg Grade is Lower than 6.0")
else:
    print("Student Failed Due to attendence rate is Lower than 80%")
