from matplotlib import pyplot as plt

def simulate(x0, n):
    res = [x0]
    for i in range(1, n+1):
        xnext = res[-1].nextState() # Ottengo il prossimo stato
        res.append(xnext) # Memorizzo lo stato
    return res


def plot_sim(x, title=None, figsize=(20, 4)):
    plt.figure(figsize=figsize)
    plt.plot(range(len(x)), x)
    if title is not None:
        plt.title(title)
    plt.show()

    
def plot_2d_trajectory(x, y, xlabel=None, ylabel=None, figsize=None, title=None):
    plt.figure(figsize=figsize)
    plt.plot(x, y)
    if xlabel is not None:
        plt.xlabel(xlabel) # Nome dell'asse x
    if ylabel is not None:
        plt.ylabel(ylabel) # Nome dell'asse y
    if title is not None:
        plt.title(title)
    plt.show()