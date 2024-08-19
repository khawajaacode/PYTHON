# for i in range (5):
   # print(i)

#print("While Loops")

    # i = 0
   # while i < 5:
  #      print(i)
 #       i +=1

"""""
import random

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")

    else:
        print("Correct")


for i in range(0, 31, 3):
    print(i)



"""
"""
n = int(input("Enter a positive integer: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("The sum of numbers from 1 to", n, "is:", total)

"""

string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
    print( "The reversed String is : ", reversed_string)
