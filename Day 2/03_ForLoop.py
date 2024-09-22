for num in range(1,20):
    print(num)


print("---------------------------------------------------------------")


string  = "This is My String"

for char in string:
    print(char)


print("---------------------------------------------------------------")


list = ["Python", "C++","" , "JavaScript", "Java","C"]

for lst in list:
    if lst == "":
        continue
    else:
        print(lst)
        

print("---------------------------------------------------------------")



for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))

print("---------------------------------------------------------------")


for x in range(1, 5):
    for y in range(1, 5):
        print('%d * %d = %d' % (x, y, x*y))

print("---------------------------------------------------------------")
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)
print("---------------------------------------------------------------")
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for x in my_range(1, 5, 0.5):
    print(x)
print("---------------------------------------------------------------")

person = {"name":"Babar", "age":20,"gender":"M"}

for key in person:
    print (person[key])


print("---------------------------------------------------------------")



