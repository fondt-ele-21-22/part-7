import random
from matplotlib import pyplot as plt

class RWState2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def nextState(self):
        # Parto dallo stato corrente
        nx, ny = self.x, self.y
        # Determino a caso la direzione
        v = random.randint(1, 4)
        if v == 1:
            nx -= 1 # sx
        elif v == 2:
            ny += 1 # su
        elif v == 3:
            nx += 1 # dx
        else:
            ny -= 1
        # Restituisco il nuovo stato
        return RWState2D(nx, ny)
    
    def __repr__(self):
        return f'RWState2D(x={self.x}, y={self.y})'    