import numpy as np
import matplotlib.pyplot as plt

def profile_naca_plot(NACA_NUMBER):
    """
    NACA ABCD:
    A  -> curvatura máxima
    B  -> distância da curvatura máxima do bordo de ataque
    CD -> espessura máxima do aerofólio

    """
    if(len(NACA_NUMBER) != 4):
        print("Este código só funciona para perfis NACA de 4 dígitos")
        return

    A  = int(NACA_NUMBER[0])
    B  = int(NACA_NUMBER[1])
    CD = int(NACA_NUMBER[2:])


    x = np.arange(0,1,0.0001)

    t = CD/100 # espessura máxima

    y_t = 5*t*(0.2969*np.sqrt(x)-0.126*(x)-0.3516*(x)**2+0.2843*(x)**3-0.1015*(x)**4);

    # Para perfis simétrios
    if (A == 0 and B == 0):
        yl = -y_t;
        xu = x;
        xl = x;

        #plot
        plt.plot(xu,y_t,'b',xl,yl,'b')
        plt.axis('equal')


    else:
        y_c = lambda x: (A/B**2)*(2*B*x - x**2) if 0<= x <= B else (A/(1-B)**2)*((1-2*B)+2*B*x-x**2)

        theta = lambda dy_dx: (2*A/B**2)*(B - dy_dx) if 0<= dy_dx <= B else (2*A/(1-B)**2)*(B-dy_dx)

        xu = np.zeros(len(x))
        yu = np.zeros(len(x))
        xl = np.zeros(len(x))
        yl = np.zeros(len(x))

        for i in range(len(x)):

            xu[i] = x[i] - y_t[i]*np.sin(np.arctan(theta(x[i])))
            yu[i] = y_c(x[i]) + y_t[i]*np.cos(np.arctan(theta(x[i])))

            xl[i] = x[i] + y_t[i]*np.sin(np.arctan(theta(x[i])))
            yl[i] = y_c(x[i]) - y_t[i]*np.cos(np.arctan(theta(x[i])))

        plt.plot(xu,yu,'b',xl,yl,'b')
        plt.axis('equal')


profile_naca_plot("0009")
