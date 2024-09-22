months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
Birthday = input("Input Birthday in this Format DD-MM-YYYY: ")

index = int(Birthday[3:5]) - 1
bd_month = months[index]

print ("You were born in ", bd_month)
        
