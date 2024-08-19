
"""
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowels_count = 0

for char in string:
   if char in vowels:
       vowels_count += 1
print( "Number of Vowels : " , vowels_count)
"""

#numbers = 10, 21 ,33
#print(max(numbers))
"""
num = int(input("Enter a number: "))
for i in range(1,11):
    result = i*num

    print(result)

"""
num = int(input("Enter a number: "))

print(f"Multiplication table for {num}:")

for i in range(1,11):
    print(f"{num} x {i} = ", i*num)
