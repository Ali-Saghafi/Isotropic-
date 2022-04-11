import numpy as np
import matplotlib.pyplot as plt
import cv2


def do_timestep(u0, u, dt = 0.1 ,dx = 1,dy = 1,D = 1):
    
    u = u0.copy();

    for i in range (2,256-1):
        for j in range (2, 256-1):
            uxx = (u0[i+1,j] - 2*u0[i,j] + u0[i-1,j])
            uyy = (u0[i,j+1] - 2*u0[i,j] + u0[i,j-1])

            u[i,j] =  u0[i,j] + D * dt *(uxx + uyy)

    u0 = u.copy()
    return u0, u


def do_timestep_persona_malek(u0, u, dt = 0.1 ,dx = 1,dy = 1,landa = 0.5):
    
    u = u0.copy();

    for i in range (2,256-1):
        for j in range (2, 256-1):
            uxx = (u0[i+1,j] - 2*u0[i,j] + u0[i-1,j])
            uyy = (u0[i,j+1] - 2*u0[i,j] + u0[i,j-1])
            

            D = (1/(1+ (abs((uxx**2 + uyy**2))/landa**2)));

            #D = (((1/(1+ (abs((uxx**2 + uyy**2)))/landa**2)))).astype(np.uint8); 
            u[i,j] =  u0[i,j] + D * dt *(uxx + uyy)

    u0 = u.copy()
    return u0, u
