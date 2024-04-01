#Kirtia Spence
#kirtia.spence59@myhunter.cuny.edu
#This program prints purple and yellow stripes

import matplotlib.pyplot as plt
import numpy as np

num = int(input("Eneter the size: "))
file = input("Enter output file: ")

img = np.zeros((num,num,3))
img[::2,:,0::2]=1
img[1::2,:,0:2]=1

plt.imsave(file,img)

