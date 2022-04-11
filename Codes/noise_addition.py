#Parameters
#----------
#image : ndarray
#    Input image data. Will be converted to float.
#mode : str
#    One of the following strings, selecting the type of noise to add:
#
#    'gauss'     Gaussian-distributed additive noise.
#    'speckle'   Multiplicative noise using out = image + n*image,where
#                n is uniform noise with specified mean & variance.
#    's&p'       Replaces random pixels with 0 or 1.
#    'uniform'   
# https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv
# https://datahacker.rs/opencv-common-types-of-noise/
import numpy as np
import random
import os
import cv2
def noisy(noise_typ,image):
   if noise_typ == "gauss":
      image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
      gaussian_noise = np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8)
      cv2.randn(gaussian_noise, 128, 20)
      gaussian_noise = (gaussian_noise*0.5).astype(np.uint8)
      noisy = cv2.add(image,gaussian_noise)
      return noisy
   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.01
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out
   elif noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)        
      noisy = image + image * gauss
      noisy = np.array(2*noisy, dtype = 'uint8')
      return noisy
   elif noise_typ =="uniform":
      image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
      uniform_noise = np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8)
      cv2.randu(uniform_noise,0,255)
      uniform_noise = (uniform_noise*0.5).astype(np.uint8)
      noisy = cv2.add(image,uniform_noise)
      return noisy
