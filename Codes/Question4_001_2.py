import cv2
import matplotlib.pyplot as plt 
import dif_do_step
import math
import psnr_cal
import numpy as np

io = cv2.imread('office.png')
io = cv2.cvtColor(io,cv2.COLOR_RGB2GRAY)
fig = plt.figure()
ax = fig.add_subplot(111)
u = np.zeros((255,255),dtype=float)
landa = 10
for i in range (1,256-1):
    for j in range (1, 256-1):
        uxx = (io[i+1,j] - 2*io[i,j] + io[i-1,j])
        uyy = (io[i,j+1] - 2*io[i,j] + io[i,j-1])        
        #D = (1/(1+ (uxx**2 + uyy**2)/landa**2)).astype(np.uint8); 
        #D = (1/(1+ (uxx**2 + uyy**2)/landa**2)).astype(np.uint8); 
        #D = (1/(1+ (uxx**2 + uyy**2)/landa**2)); 
        D = ((255*(1/(1+ abs((uxx**2 + uyy**2))/landa**2)))).astype(np.uint8); 
        print(D)
        u[i,j] =  D

ax.imshow(u.copy(), cmap='gray', vmin=0, vmax=255)

fig.subplots_adjust(right=0.85)

plt.show()


