class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")


if __name__ == "__main__":
    animal = Animal("Generic Animal", 5)
    dog = Dog("Buddy", 3)
    cat = Cat("Whiskers", 2)

    animal.eat()
    dog.eat()
    cat.eat()

    dog.bark()
    cat.meow()