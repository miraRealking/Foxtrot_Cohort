# class Person: # Blue print
#     pass


# miracle = Person() # Object also called an instance
# clinton = Person() # Object - instance
# tivsue = Person() # Object - instance


class Footballer:
    #--------- Attributes here -------------
    # Class Attribute
    game = "Football" 
    ball = "Sphere"

    # Instance Attribute
    def __init__(self, name, age, role): # Constructor
        self.name = name
        self.age = age
        self.role = role


    #--------- Methods here ----------
    def information(self):
        return f"{self.name} plays {Footballer.game}. The ball is {Footballer.ball}"


zinedine_zidane = Footballer("Zinedine Zidane", 34, "Attacking Midfielder")
cristiano_ronaldo = Footballer(name="Ronaldo", age=39, role="Striker")

# print(zinedine_zidane.information())
# print(cristiano_ronaldo.information())


'''
class Person:
    def __init__(self):
        self.name = "Joe"


class Employee(Person):
    def __init__(self):
        super().__init__()


joe = Employee()
print(joe.name)
'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Employee(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)


joe = Employee(name="Joe Sanders", age=22, gender="Male")
print(joe.age)

