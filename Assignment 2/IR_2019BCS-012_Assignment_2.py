# IR Assignment 2
# 2019BCS-012  Bharat Chandwani
# BCS1923

import numpy as np
import math as m


Bp = list(map(float, input(
    "\nEnter the coordinates(final coordinates) : ").strip().split()))
check = 'y'
RotationMatrix = np.identity(3)
Bp = np.asarray(np.reshape(Bp, [3, 1]), dtype=float)


def Rx(theta):
    return np.matrix([[1, 0, 0],
                      [0, m.cos(theta), -m.sin(theta)],
                      [0, m.sin(theta), m.cos(theta)]])


def Ry(theta):
    return np.matrix([[m.cos(theta), 0, m.sin(theta)],
                      [0, 1, 0],
                      [-m.sin(theta), 0, m.cos(theta)]])


def Rz(theta):
    return np.matrix([[m.cos(theta), -m.sin(theta), 0],
                      [m.sin(theta), m.cos(theta), 0],
                      [0, 0, 1]])


while check == 'y':
    angle, axis = list(
        input("\nEnter the angle and axis of rotation: ").split())
    angle = m.radians(float(angle))

    if(axis == "x" or axis == "X"):
        matrix = Rx(angle)
        RotationMatrix = RotationMatrix*matrix

    elif(axis == "y" or axis == "Y"):
        matrix = Ry(angle)
        RotationMatrix = RotationMatrix*matrix

    elif(axis == "z" or axis == "Z"):
        matrix = Rz(angle)
        RotationMatrix = RotationMatrix*matrix

    else:
        print("Invalid axis: ")

    check = input("Enter y to continue to add more rotations: ")

Ap = RotationMatrix*Bp
Ap = np.round(Ap, 3)

print("Final coodinatess after Rotation are :")
for i in Ap:
    print(i, end=', ')
