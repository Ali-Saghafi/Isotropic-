import numpy as np
import gaus2d_imp
def gausian_kern5x5_gen(n = 5,sgima = 1):
    a = 2
    x = np.linspace (-a,a,n) 

    x, y = np.meshgrid(x, x) # get 2D variables instead of 1D
    z = gaus2d_imp.gaus2d(x, y,sgima)
    zsum = np.sum(z)
    z = z/zsum
    return z
