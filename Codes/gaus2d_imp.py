import numpy as np
# define normalized 2D gaussian
def gaus2d(x=0, y=0, sigma =1):
    return 1. / (2. * np.pi * sigma**2.)**(1/2) * np.exp(-(x**2. + y**2.) / (2. * sigma**2.))

