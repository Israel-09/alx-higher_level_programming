from random import randint

class warrior:
    def __init__(self, name= '', total_live = 0):
        self.name = name
        self.t_live = 19
        
    def left_live(self, damage):
        self.t_live -= damage

sam = warrior()
sam.name = "sam"
dave = warrior()
sam.name = "dave"

while True:
    hit = randint(0, 10)
    



print(f"{sam.total_live}")
