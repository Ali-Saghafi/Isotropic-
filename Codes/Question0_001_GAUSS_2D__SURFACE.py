import gaus2d_imp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(1,6,subplot_kw={"projection": "3d"})



sigma = [1,2,10,20,50,100]
for lc in range(6):
    x = np.linspace(-sigma[lc]*5, sigma[lc]*5)
    y = np.linspace(-sigma[lc]*5, sigma[lc]*5)
    x, y = np.meshgrid(x, y) # get 2D variables instead of 1D
    z = gaus2d_imp.gaus2d(x, y,sigma[lc])
    surf = ax[lc].plot_surface(x, y, z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    ax[lc].set_title(f'Sigma= {sigma[lc]}', fontsize=10, fontweight='bold',color='#30302f', loc='center')

    #fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


