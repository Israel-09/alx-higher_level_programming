#!/usr/bin/python3
class_to_json = __import__('8-class_to_json').class_to_json 

class MyClass:
    """ My class
     """
    def __init__(self, name):
         self.name = name
         self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)


m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

class MyClass:
        
    """ My class
    
    """
    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
    
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)


print('\n-----------------------------------\n')
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
