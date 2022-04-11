import cv2
import matplotlib.pyplot as plt 

import gaus_fil_conv
import gaus_kernel

image_office_dir = 'office.png'
img_office = cv2.imread(image_office_dir)
plt.figure()
for lc in range(1,8):
    plt.subplot(2,7, lc)
    plt.title('office') 
    plt.imshow(img_office)


image_office_noisy_dir = 'office_noisy.png'
img_office_noisy = cv2.imread(image_office_noisy_dir)

plt.subplot(2,7,8)
plt.title('office_noisy') 
plt.imshow(img_office_noisy)


img_office_noisy = cv2.cvtColor(img_office_noisy,cv2.COLOR_RGB2GRAY)
print(type(img_office_noisy))
print(img_office_noisy.shape)
print('\n')
sigma = [0.5,1,2,5,10,50]
for lc in range(0,6):
    print(f'Calculating for sigma =  {sigma[lc]} ....')
    kernel = gaus_kernel.gausian_kern5x5_gen(5,sigma[lc])
    filtered_img = gaus_fil_conv.gaus_fico(img_office_noisy,kernel)
    plt.subplot(2,7,8 + lc + 1 )
    plt.title(f'office_filtered\n Sig = {sigma[lc]}') 
    plt.imshow(filtered_img,cmap='gray', vmin=0, vmax=255)
    print(f'Sigma =  {sigma[lc]} done\n\n')


plt.show()