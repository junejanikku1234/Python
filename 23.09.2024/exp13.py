stat_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("This is a statically created filled dictionary:")
print(stat_dict)

dynamic_dict = dict()
print("This is an empty dictionary:")
print(dynamic_dict)

stat_dict.update({"city": "Agra"}) # Can't duplicate key, updates previous key's value
print(stat_dict)

for key, value in stat_dict.items(): # since python 3.7+ order of dictionary maintained
    print(key, value)

print(stat_dict["name"])
stat_dict["age"] = 42
print(stat_dict)

def add_to_dict(dictionary):
    n = int(input("Enter the number of key:value pairs to add: "))
    i = 0
    while i<n:
        new_key = input("Enter the {}th key to add: ".format(i+1))
        new_value = input("Enter the {}th value to add: ".format(i+1))
        print()
        dictionary.update({new_key: new_value})
        i += 1

stat_dict.setdefault("gender","male")
print(stat_dict)
add_to_dict(dynamic_dict)
print(dynamic_dict)
del dynamic_dict["apple"]
print(dynamic_dict)
dynamic_dict.clear()
print(dynamic_dict)
