from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    @abstractmethod
    def make_sound(self):
        pass  # This method is abstract and must be implemented by subclasses

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

    def make_sound(self):
        self.bark()  # Implementing the abstract method with specific sound

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

    def make_sound(self):
        self.meow()  # Implementing the abstract method with specific sound


if __name__ == "__main__":
    # Animal class cannot be instantiated directly due to abstraction
    # animal = Animal("Generic Animal", 5)

    dog = Dog("Buddy", 3)
    cat = Cat("Whiskers", 2)

    animal_list = [dog, cat]  # Collection of Animal objects (polymorphism)

    for animal in animal_list:
        animal.eat()
        animal.make_sound()  # Calling the abstract method (polymorphic behavior)