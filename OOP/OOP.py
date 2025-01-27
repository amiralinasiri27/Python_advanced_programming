class Car:
    def __init__(self, brandName, modelName, countryName, num):
        self.brandName = brandName
        self.modelName = modelName
        self.countryName = countryName
        self.num = num


car1 = Car("Porsche", "Macon", "Germany", 27)


# print(car1.num)
# --------------------------------------------------------

# to inherit of a class you should do this:

class BMW(Car):
    def __init__(self, brandName, modelName, countryName, num):
        super().__init__(brandName, modelName, countryName, num)
        self.num = num * 10


bmw = BMW("", "", "", 10)

# print(bmw.num)
# --------------------------------------------------------

class employee:
    def __init__(self, name, project, salary):
        self.salary = salary
        self.name = name
        self.project = project

    def show(self):
        print(self.name, "is working on", self.project)


emp1 = employee("Ali", "Django", 1000)
emp2 = employee("Amir", "React", 1500)

# emp1.show()
# emp2.show()
# --------------------------------------------------------

from abc import ABC, abstractmethod


class absClass(ABC):
    def print(self, x):
        print("Value:", x)

    def task(self):
        print("We are in abcClass")

    @abstractmethod
    def absMM(self):
        pass


class test(absClass, ABC):
    # Override
    def task(self):
        print("Test Class")


# testOBJ = test()
# testOBJ.print(100)
# testOBJ.task()
#
# absOBj = absClass()
# absOBj.task()
# --------------------------------------------------------

# Polymorphism
class Rabbit:
    def __init__(self, name):
        self.name = name

    def age(self):
        print(self.name, "is 18 Rabbit")

class Horse:
    def __init__(self, name):
        self.name = name

    def age(self):
        print(self.name, "is 18 Horse")


ob1 = Rabbit("R1")
ob2 = Horse("H2")

# for type in (ob1, ob2):
#     type.age()

# --------------------------------------------------------

# Inheritance Class Polymorphism

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
  # print(x.brand)
  # print(x.model)
  # x.move()

