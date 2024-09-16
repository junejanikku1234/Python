fruit_lst = ["Pineapple", "Kiwi", "Strawberry", "Pear", "Watermelon"]

print("The length of this fruit list is {}", len(fruit_lst))

print("Is Mango present in this list? {}".format("Mango" in fruit_lst))

copy_of_list = fruit_lst[::]
print("The original fruit list is {}".format(fruit_lst))
print("The copied fruit list is {}".format(copy_of_list))
