#Kirtia Spence
#kirtia.spence59@myhunter.cuny.edu
#This program prints Turtle control

import turtle

kir = turtle.Turtle()
twoTrack = turtle.Screen()
direction = input("Please enter a command string: ")

for ch in direction:
    if ch == 'F':
        kir.forward(50)
    elif ch == 'L':
        kir.left(90)
    elif ch == 'R':
        kir.right(90)
    elif ch == '^':
        kir.penup()
    elif ch == 'v':
        kir.pendown()
    elif ch == 'B':
        kir.backward(50)
    elif ch == 'S':
        kir.stamp()
    elif ch == 'l':
        kir.left(45)
    elif ch == 'r':
        kir.right(45)
    elif ch == 'p':
        kir.color("purple")
else:
    print("Error do not know the command:",ch)

print("See graphics window for your image")
twoTrack.exitonclick()
