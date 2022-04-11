import cv2
import matplotlib.pyplot as plt 
import noise_addition


image_office_dir = 'office.png'
img_office = cv2.imread(image_office_dir)#,cv2.IMREAD_GRAYSCALE)

plt.figure()
for lc in range(1,5):
    plt.subplot(2,4, lc)
    plt.title('office') 
    plt.imshow(img_office)

title = ['a)gauss', 'b)speckle' , 'c)s&p','d)uniform' ]
noise_type = ['gauss', 'speckle' , 's&p','uniform' ]
for lc in range(0,4):
    noisy_img = noise_addition.noisy(noise_type[lc],img_office)
    plt.subplot(2,4,5 + lc )
    plt.title(f'{title[lc]}') 
    plt.imshow(noisy_img,cmap='gray', vmin=0, vmax=255)

plt.show()