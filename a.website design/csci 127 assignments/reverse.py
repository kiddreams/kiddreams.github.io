#Kirtia Spence
#kirtia.spence59@myhunter.cuny.edu
#This program print reverse twice

phrase = input("Enter a message: ")
last_idx = len(phrase)-1
for i in phrase[::-1]:
    print(i + " " + i)
