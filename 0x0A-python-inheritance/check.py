class MyObj:
    pass

class Obj2:
    def __dir__(self):
        return [1, 2, 3]

print(dir(Obj2()))
x = Obj2()
print(dir(x))
