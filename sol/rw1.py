import random

class RWState1D:
    def __init__(self, x=0):
        self.x = x
    
    def nextState(self):
        # Parto dallo stato corrente
        nx = self.x
        # Determino a caso la direzione
        v = random.randint(1, 2)
        if v == 1:
            nx -= 1 # giù
        else:
            nx += 1 # su
        # Restituisco il nuovo stato
        return RWState1D(nx)
    
    def __repr__(self):
        return f'RWState1D(x={self.x})'


class RWIState1D:
    def __init__(self, x=0, v=1, p=0.5):
        self.x = x
        self.v = v
        self.p = p
    
    def nextState(self):
        # Parto dallo stato corrente
        x, v = self.x, self.v
        # Determino a caso se la direzione viene mantenuta o cambiata
        val = random.random()
        if val < self.p:
            nx, nv = x+v, v # mantengo la direzione
        else:
            nx, nv = x-v, -v # cambio direzione
        # Restituisco il nuovo stato
        return RWIState1D(x=nx, v=nv, p=self.p)
    
    def __repr__(self):
        return f'RWIState1D(x={self.x}, v={self.v})'