# Bharat Chandwani
# 2019BCS-012


import math
from matplotlib.pyplot import plot, show, style, text
import matplotlib.pyplot as plt
import numpy as np
# Input: The joint positions pi for i = 1,...,n, the
# target position target and the distances between each
# joint


class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.X = x
        self.Y = y

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def getXY(self):
        return np.asarray([self.X, self.Y], dtype=np.float64)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx**2 + dy**2)


def fabrik():
    # n=int(input())
    style.use('seaborn-whitegrid')
    n = int(input("Enter Number of Links: "))
    p = []
    sum = 0
    for i in range(n):
        x, y = list(
            map(float, input("Enter {} coordinate: ".format(i+1)).strip().split(),))[:3]
        p.append(Point(x, y))

    for i in range(n-1):
        plot([p[i-1].getX(), p[i].getX()],  [p[i-1].getY(), p[i].getY()],
             color='red', marker='X', linestyle=':', linewidth=1)

    x, y = list(
        map(float, input("Enter Goal coordinate: ").strip().split(),))[:3]
    target = (Point(x, y))
    plot(target.getX(), target.getY(), 'X', label='Goal')
    final = target.getXY()
    tol = float(input("Enter Tolerence: "))
    iteration = 0
    d = []
    for i in range(1, n):
        d.append(p[i].distance(p[i-1]))
        sum += p[i].distance(p[i-1])
    if(sum < target.distance(p[0])):
        print(" The target is unreachable")

        for i in range(0, n-1):
            # Find the distance ri between the target target and the joint
            r = target.distance(p[i])
            lambd = d[i-1]/r
            arr = ((1-lambd)*(p[i].getXY()) + lambd*(target.getXY())).tolist()
            p[i+1] = Point(arr[0], arr[1])
    else:
        dist = p[-1].distance(target)
        while dist > tol:
            iteration += 1
            # STAGE 1: FORWARD REACHING
            # Set the end effector pn as target target
            p[-1] = Point(final[0], final[1])
            for i in range(n-2, 0, -1):
                r = p[i].distance(p[i+1])
                lambd = d[i]/r
                arr = ((1-lambd)*p[i+1].getXY()+lambd*p[i].getXY()).tolist()
                p[i] = Point(arr[0], arr[1])

            # STAGE 2: BACKWARD REACHING
            # Set the root p1 its initial position
            initial = p[0].getXY()
            for i in range(0, n-1):
                p[0] = Point(initial[0], initial[1])
                r = p[i+1].distance(p[i])
                lambd = d[i]/r
                arr = ((1-lambd)*p[i].getXY()+lambd*p[i+1].getXY()).tolist()
                p[i+1] = Point(arr[0], arr[1])

            dist = p[-1].distance(target)
            for i in range(1, n):
                plot([p[i-1].getX(), p[i].getX()],  [p[i-1].getY(), p[i].getY()],
                     marker='o', linestyle='dashed', linewidth=1, label='Line{}'.format(i+1))
    show(block=True)
    print("------Results------")
    print("Iterations: ", iteration)
    print("Link position:",)
    for i in range(n):
        print(p[i])
    print("Goal Position:", target)


if __name__ == '__main__':
    fabrik()
