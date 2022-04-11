import cv2
import matplotlib.pyplot as plt 
import dif_do_step
import math
import psnr_cal

io = cv2.imread('office.png')
io = cv2.cvtColor(io,cv2.COLOR_RGB2GRAY)
ion0 = cv2.imread('office_noisy.png')
#ion0 = cv2.imread('office.png')
ion0 = cv2.cvtColor(ion0,cv2.COLOR_RGB2GRAY)

ion = ion0.copy();
ion00 = ion0.copy();

iter_t = [1,5,10,30,100]
# Number of timesteps
nsteps = 11

mfig = [10]

dx = dy = 1
landa = [0.5,1,2,5,10]
dt = 1
fignum = 0
fig = plt.figure()
for j in range(5):
    ion0 = ion00.copy();
    ion = ion0.copy();
    for m in range(nsteps):
        if m in mfig:
            fignum += 1
            print('\u03BB=',landa[j],m, fignum)
            psnr_val = "{:.2f}".format(psnr_cal.PSNR(ion00, ion))
            ax = fig.add_subplot(230 + fignum)
            im = ax.imshow(ion.copy(), cmap='gray', vmin=0, vmax=255)
            ax.set_axis_off()
            ax.set_title(f'\u03BB= {landa[j]}\n PSNR = {psnr_val}')
            print("PSNR = ", psnr_val)
        ion0, ion = dif_do_step.do_timestep_persona_malek(ion0, ion, dt, dx, dy, landa[j])

fig.subplots_adjust(right=0.85)
plt.show()


