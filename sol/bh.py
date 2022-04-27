class BHState:
    def __init__(self, x, r, N=1):
        self.x = x
        self.r = r
        self.N = N
    
    def nextState(self):
        x, r, N = self.x, self.r, self.N # Rinomino per compattezza
        xnext = r * x / (1 + x/N) # Calcolo il prossimo stato
        return BHState(xnext, r, N)
    
    def __repr__(self):
        return f'BHState(x={self.x}, r={self.r}, N={self.N})'