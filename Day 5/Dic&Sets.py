"""

from collections import Counter

text = "Hello world Hello world Hello world Hello world"
dictionary = Counter(text)
print(dictionary)

def add():
    students["Jake"] = 99
    students[ "Bob" ] = 88



students = {"Alice": 85,"Charlie": 92,}

# Add a new student
# Update marks for Bob
# Display all students
print(students, add())


from importlib.resources.readers import remove_duplicates

sentence = "Python is fun and Python is easy"
# Output: {'Python', 'is', 'fun', 'and', 'easy'}

remove_duplicates(sentence)

print(sentence)



def common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_ele =  set1 & set2
    return common_ele






list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
commom_ele = common(list1, list2)


print(commom_ele)


"""
def create_dic():
    empty_dict = {}

    for num in range(1,11):
        empty_dict[num] = num **2
    return empty_dict



squares = create_dic()
print("Dictionary of squares ",squares)




























