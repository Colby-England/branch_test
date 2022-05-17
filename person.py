

class Person:

    def __init__(self, name, age):
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
 
    def say_hello(self):
        print(f'Hello {self.name}')
