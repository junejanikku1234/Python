fruit_lst = ["Apple","Banana","Orange","Mango","Grapes"]

for fruit in fruit_lst:
    print(fruit)

fruit_lst.append("Pineapple")
fruit_lst.insert(2,"Pear")
print(fruit_lst)
print(fruit_lst.pop())
fruit_lst.remove("Mango")
del fruit_lst[1]
print(fruit_lst)