#!/usr/bin/env python

import numpy as np
import operator
from scipy.optimize import fsolve
from functools import reduce
import math
import matplotlib.pyplot as plt

def binMLEdist(n,p,k,N):
    x=np.random.binomial(k, p, (n,N))
    khat=[]
    for i in xrange(0,N):
        func = lambda z : reduce(operator.mul,(1-x[:,i]*z))-(1-p)**n
        zhat=fsolve(func,0.005)
        khat.append(math.floor(1.0/zhat))
    return khat

def main():
    khat=binMLEdist(20,0.5,200,100)
    plt.hist(khat,15,normed=1)
    plt.show()
    
if __name__ == '__main__':
    main()
