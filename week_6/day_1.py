# Composition
# Meaning Is building complex objects by combining simple ones


class A:
    def __init__(self):
        self.name = "This is class A"


class B:
    def __init__(self):
        self.name = "This is class B"
        self.a = A()


b = B()
print(b.a.name)