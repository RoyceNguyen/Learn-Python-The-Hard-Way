# Animal is-a object
class Animal(object):
    pass

#Dog is-a object
class Dog(Animal):
    def __init__(self, name):
        #Dog has-a name
        self.name = name

#Cat is-a object
class Cat(Animal):
    def __init__(self, name):
        #Cat has-a name
        self.name = name

#Person is-a object
class Person(object):
    def __init__(self, name):
        #Person has-a name
        self.name = name
        #Person has-a pet
        self.pet = None

#Person is-a object
class Employee(Person):
    def __init__(self, name, salary):
        #Employee has-a name
        super(Employee,self).__init__(name)
        #Employee has-a salary
        self.salary = salary

#Fish is-a object
class Fish(object):
    pass


#Salmon is-a object
class Salmon(Fish):
    pass


#Halibut is-a object
class Halibut(object):
    pass

#rover is-a Dog
rover = Dog("Rover")

#satan is-a Cat
satan = Cat("Satan")

#Mary is-a Person
Mary = Person("Mary")

#mary has-a pet satan
mary.pet = satan

#frank is-a Employee
frank = Employee("Frank", 120000)

#frank has-a pet rover
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a Halibut
harry = Halibut
