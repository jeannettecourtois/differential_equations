import numpy as np
import matplotlib.pyplot as plt


#N for numbers of points 

def champ(F, a, b, c, d, N, x0=None):
    x = np.linspace(a, b, N) 
    y = np.linspace(c, d, N)
    X, Y = np.meshgrid(x, y) #we obtain two matrices of dimensions x*x and y*y
    print(np.meshgrid(x, y))

    FX, FY = F(X, Y)

    plt.figure()
    plt.streamplot(X, Y, FX, FY, density=2.0, linewidth=1)  #streamplot helps building vector fields 
    plt.axis([a, b, c, d])

    if x0 is not None:
        plt.streamplot(X, Y, FX, FY, color='r', start_points=x0, linewidth=2)

def main():
    print("Trying functions.\n")
    
    #Syntax of np.ones_like: numpy.ones_like(array, dtype = None...)
    def F(t, y):
        return np.ones_like(t), y - y**2

    x0 = np.array([
        [0, 0],
        [0, 2],
        [0, 0.5],
        [0, 1]
    ])

    champ(F, 0, 3, 0, 2, 50, x0=x0)
    plt.title(r"$y' = y - y^2$") #Latex syntax 
    plt.show()

if __name__ == "__main__":
    main()