import math
import cv2
import numpy as np
def gaus_fico(img_gray,kernel):
    h,w = img_gray.shape
    k_h,k_w = kernel.shape
    for i in range(int(k_h/2),h-int(k_h/2)):
        for j in range(int(k_h/2),w-int(k_h/2)):
            sum = 0
            for k in range(0,k_h):
                for l in range(0,k_h):
                    sum += img_gray[i-int(k_h/2)+k,j-int(k_h/2)+l]*kernel[k,l]
            img_gray[i,j] = sum
    return img_gray