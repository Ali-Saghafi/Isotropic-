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
D = [1,5,10]
dt = 0.01
fignum = 0
fig = plt.figure()
for j in range(3):
    ion0 = ion00.copy();
    ion = ion0.copy();

    for m in range(nsteps):
        if m in mfig:
            fignum += 1
            print('D=',D[j],m, fignum)
            psnr_val = "{:.2f}".format(psnr_cal.PSNR(io, ion))
            ax = fig.add_subplot(230 + fignum)
            im = ax.imshow(ion.copy(), cmap='gray', vmin=0, vmax=255)
            ax.set_axis_off()
            ax.set_title(f'D= {D[j]}\n PSNR = {psnr_val}')
            print("PSNR = ", psnr_val)
        ion0, ion = dif_do_step.do_timestep(ion0, ion, dt, dx, dy, D[j])

fig.subplots_adjust(right=0.85)
plt.show()


