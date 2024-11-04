class Person:
    def __init__(self, name, age, gender, salary):
        self.name = name
        self._age = age
        self.__gender = gender
        self.salary = salary

    def get_name(self):
        return self.name
    def get_age(self):
        return self._age
    def get_gender(self):
        return self.__gender
    def get_salary(self):
        return self.salary

    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self._age = age
    def set_gender(self, gender):
        self.__gender = gender
    def set_salary(self, salary):
        self.salary = salary

    def display(self):
        print(self.name, self._age, self.__gender, self.salary)

obj1 = Person("Alice", 25, "Female", 35000)
obj2 = Person("Bob", 32, "Male", 52000)
obj3 = Person("Charlie", 28, "Male", 48000)
obj4 = Person("Daisy", 22, "Female", 38000)
obj5 = Person("Ethan", 30, "Male", 55000)

obj1.display()
obj2.set_age(69)
obj3.set_gender("Female")
obj2.display()
obj3.display()
print(obj4.get_name())

obj5.name = "Random"        # works because its public access
obj5.__gender = "Undefined" # doesn't change the value because its private
obj5.display()
obj5._Person__gender = "LOL" # works because we provided mangled name
obj5.display()