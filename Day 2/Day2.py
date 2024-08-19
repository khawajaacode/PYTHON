#number = float(input("Enter a number: "))

#if number % 2 == 0:
 #else:
 #   print("Odd")

score = int(input("Enter a score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is:", grade)

