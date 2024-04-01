#Kirtia Spence
#kirtia.spence59@myhunter.cuny.edu
#This program prints population stats

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
borough = input("Enter a Borough: ")
average= pop[borough].mean()
maximum = pop[borough].max()

print("Average population: ", average)
print("Maximum population: ", maximum)
