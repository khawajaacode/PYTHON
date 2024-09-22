import random

people = []

for x in range(0,8):
    person = input("Type the name of a person: ")
    people.append(person)

index = random.randint(0,7)

random_person = people[index]

print ("Picking a Random person: ",random_person)


print("_-------------------")

      
print ( "SECOND QUESTION")



import random

colors = ["red", "black", "blue", "yellow"]

while True:
    color = colors[random.randint(len(colors)-1)]
    guess = input("I was Thinking about the color can you guess it ?")

    while True:
        if color == guess.lower():
            break

        else:
            guess = input ("Nope. Try again: ")
            
        

    print("You Guessed it!, i was thinking about ,",color)

    play_again = input ("Lets Play Again? Type 'No' to Quit.")

    if play_again.lower() == 'No':
        break

print ("It was Fun")
            
                
