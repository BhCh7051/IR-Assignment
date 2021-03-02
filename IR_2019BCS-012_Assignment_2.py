# IR Assignment 2
# 2019BCS-012  Bharat Chandwani
# BCS1923

import numpy as np
import math as m
def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(theta),-m.sin(theta)],
                   [ 0, m.sin(theta), m.cos(theta)]])
  
def Ry(theta):
  return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])
  
def Rz(theta):
  return np.matrix([[ m.cos(theta), -m.sin(theta), 0 ],
                   [ m.sin(theta), m.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])

Bp = np.matrix([2,3,0])

Ap = Rz(30)*Ry(30)*Rx(30)*np.transpose(Bp);

print(np.round(Ap, 3))