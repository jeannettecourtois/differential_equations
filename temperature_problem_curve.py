import numpy as np 
import matplotlib.pyplot as plt 
from collections.abc import Sequence 
import math as mt 

#different types 

type Coordinates = list[float]
type Matrix = list[list[float]]

def champ(F: Matrix, a:float, b:float, c:float, d:float, N:int, xo):
    x = np.linspace(a, b, N)
    y = np.linspace(c, d, N)
    X, Y = np.meshgrid(x, y)
    
    #we use streamplot for vector fields 
    
    FX, FY = F(X, Y)
    
    
    plt.streamplot(X, Y, FX, FY, density=2.0, linewidth=1)  #streamplot helps building vector fields 
    plt.axis([a, b, c, d])
    
    if(xo is not None):
        plt.streamplot(X, Y, FX, FY, color = 'r',  start_points=xo, linewidth=2.0)
    
    
    return 



def main():
    print("Try your functions here: \n")
    
    x_start = np.linspace(-3, 3, 20)
    y_start = np.linspace(-3, 3, 20)
    starting_points = np.column_stack((x_start, y_start))
    
    #tangent field associates to every point of form (t, y(t)) the vector (1, f(t, y))
    def Temperature(t, T):
        return np.ones_like(t), -(T-2*np.cos(t))
    
    plt.figure()
    champ(Temperature, -3, 3, -3, 3, 100, starting_points)
    plt.title(r"$ T'(t) = -(T(t) - 2*cos(t))$")
    plt.show()
    

if __name__ == "__main__":
    main()
    