class DrugState:
    def __init__(self, x=0, half_life=1):
        self.x = x
        self.half_life = half_life
    
    def nextState(self):
        # Calcolo il valore di alpha
        alpha = 0.5**(1/self.half_life)
        # Calcolo il prossimo valore della quantità in circolo
        nx = alpha * self.x
        return DrugState(x=nx, half_life=self.half_life)
    
    def __repr__(self):
        return f'DrugState(x={self.x}, half_life={self.half_life})'


class DrugState2:
    def __init__(self, x=0, k=0, half_life=1, dose=1, period=8):
        self.x = x
        self.k = k
        self.half_life = half_life
        self.dose = dose
        self.period = period
    
    def nextState(self):
        # Calcolo il valore di alpha
        alpha = 0.5**(1/self.half_life)
        # Calcolo il prosismo valore del tempo
        nk = self.k + 1
        # Verifico se il farmaco vada ri-somministrato
        if nk % self.period == 0:
            nx = alpha * self.x + self.dose # prossimo valore di x
        else:
            nx = alpha * self.x
        return DrugState2(x=nx, k=nk,
                          half_life=self.half_life, dose=self.dose, period=self.period)
    
    def __repr__(self):
        s = f'x={self.x}'
        s += f', k={self.k}'
        s += f', half_life={self.half_life}'
        s += f', dose={self.dose}'
        s += f', period={self.period}'
        return f'DrugState({s})'