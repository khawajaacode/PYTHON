print ("This Program calculates the Body Mass Index.")

height = float(input("Input The Height of a Person in meters: "))
weight = float(input("Input The Weight of a Person in Kg: "))

BMI = weight / (height*height)
print ("Body Mass Index of a Person is: ", round((BMI),2))

if(BMI <= 18.5):
    print ("Underweight")
elif(BMI > 18.5 and BMI <= 24.9):
    print ("Normal Weight")
elif(BMI > 24.9 and BMI <= 29.9):
    print ("Over Weight")
else:
    print ("Obesity")
