class LogiState:
    def __init__(self, x, r, N=1):
        self.x = x
        self.r = r
        self.N = N
    
    def nextState(self):
        x, r, N = self.x, self.r, self.N # Rinomino per compattezza
        xnext = r * x * (1 - x / N) # Calcolo il prossimo stato
        return LogiState(xnext, r, N)
    
    def __repr__(self):
        return f'LogiState(x={self.x}, r={self.r}, N={self.N})'