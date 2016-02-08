#!/usr/bin/env python
import random
import matplotlib
def sample(n,theta):
    x=[]
    for i in xrange(0,n):
        U=random.random()
        if U<theta:
            x.append(1.0)
        else:
            x.append(0.0)
    return x


def MLE(x):
    return min(sum(x)/len(x),0.5)

def methodofmoments(x):
    return sum(x)/len(x)

def main():
    x=sample(10,0.5)
    print('10 points. MLE:  %f and Mom: %f' % (MLE(x), methodofmoments(x)) )
    x=sample(1000,0.5)
    print('100 points. MLE:  %f and Mom: %f' % (MLE(x), methodofmoments(x)) )
    x=sample(1000,0.5)
    print('1000 points. MLE:  %f and Mom: %f' % (MLE(x), methodofmoments(x)) )
if __name__ == '__main__':
     main()

