#Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self):
        self.eyes = 2
        self.heart = 1
        self.lungs = 2

#is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        #Dog has-a name
        self.name = name
        Animal.__init__(self)

#Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        #Cat has-a name
        self.name = name

#Person is-a object
class Person(object):
    
    def __init__(self, name):
        #Person has-a name
        self.name = name

        #Person has-a pet of some kind
        self.pet = None

#Employee is-a Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ##Employee has-a Person init method
        super(Employee, self).__init__(name)
        #Employee has-a salary
        self.salary = salary

#Fish is-a object
class Fish(object):
    
    def __init__(self):
        self.tail = 1
        self.gills = 2

#Salmon is-a Fish
class Salmon(Fish):
    
    def __init__(self):
        self.skin = "red"

#Halibut is-a Fish
class Halibut(Fish):
    
    def __init__(self):
        self.size = "big"

#rover is-a Dog
rover = Dog("Rover")

#satan is-a cat
satan = Cat("Satan")

#mary is-a person
mary = Person("Mary")

#marry has-a pet cat
mary.pet = satan

#frank is-a Employee
frank = Employee("Frank", 120000)

#frank has-a pet dog
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is a halibut
harry = Halibut()

