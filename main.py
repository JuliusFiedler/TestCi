import numpy as np
import sys
import os
import matplotlib.pyplot as plt



def main():
    xx = np.linspace(0, 10, 1000)
    yy = np.cos(xx)
    plt.plot(xx, yy)
    plt.show()



if __name__ == "__main__":
    main()