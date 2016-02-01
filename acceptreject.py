#!/usr/bin/env python
#acceptance rejection algorithm for generating
# normally distributed variables 
import random, math
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np


def quotient(y):
    fY = 1/math.sqrt(2 * math.pi) * math.e**( -(y**2 / 2) )
    fV = 1/(math.sqrt(2) * math.pi) * 1 / ( 1 + y**2 / 2 )
    return fY/fV
def generateNormal(n,i):
    x=[] # empty list
    counter = 0

    while counter < n:
        U=random.random() # (0,1) uniform
        V=math.sqrt(2)*math.tan( math.pi * (random.random()-1/2) )
    
        if U<1/math.sqrt(math.pi) * quotient(V):
            x.append(V)
            counter = counter + 1
    
    plt.figure(i)
    z, bins, patches = plt.hist(x,20,normed = 1)
    pdf = mlab.normpdf( np.linspace(-4,4,1000) , 0 , 1)
    plt.plot(np.linspace(-4,4,1000), pdf,'r--', linewidth = 2)
    

def main():
    generateNormal(100,1)
    generateNormal(1000,2)
    generateNormal(10000,3)
    plt.show()

if __name__ == '__main__':
       main()
