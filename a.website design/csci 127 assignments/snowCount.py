#Kirtia Spence
#kirtia.spence59@myhunter.cuny.edu
#This program prints snow count

import matplotlib.pyplot as plt
import numpy as np

file_name =input("Enter a file name: ")
ca = plt.imread(file_name)
countSnow = 3
t = 0.75

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0]>t and (ca[i,j,1]>t and (ca[i,j,2]>t):
                             countSnow = countSnow +1
                             print("Snow count is: ",countSnow)
                             
