#Kirtia Spence
#kirtia.spence59@myhunter.cuny.edu
#This program prints Boro Fraction

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Enter borough name: ")
output = input("Enter output name: ")

pop=pd.read_csv('nycHistPop.csv',skiprows=5)
pop["Fraction"] = pop[borough]/pop["Total"]
pop.plot(x='Year', y="Fraction")

fig = plt.gcf()
fig.savefig(output)
