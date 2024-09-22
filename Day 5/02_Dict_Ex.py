person = { "Name": "Babar", "Age": 20, "Gender": "Male", "Address": "Rwp", "Phone": 151-33344555}

Key = input("What to know about Person: ")


result = person.get(Key, "Info not available")
#person.get("Age", "Invalid Input")
#person.get("Address", "Invalid Input")
#person.get("Phone", "Invalid Input")
print(result)
