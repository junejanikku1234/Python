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

obj1 = Person("Nipun",20,"Male",42000)
obj1.display()
obj1.set_age(69)
obj1.set_gender("Female")
obj1.display()
print(obj1.get_name())

obj1.name = "Random"        # works because its public access
obj1.__gender = "Undefined" # doesn't change the value because its private
obj1.display()
obj1._Person__gender = "LOL" # works because we provided mangled name
obj1.display()