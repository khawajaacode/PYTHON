import random

number = random.randint(0,100)

guess = int(input("Thinking about the Number btw 0 to 10 can you Guess it? "))


while True:
   if number == guess:
    break
   else:
       guess = int(input("Nope, Try the Number again: "))

print ("You guess the Number Correctly", number)
       
       

    
