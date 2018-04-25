import numpy as np

R=100
C=2
X=np.random.randn(R,C)
ones=np.ones((R,1))
Xb=np.concatenate((X,ones),axis=1)

w=np.random.randn(C+1)

z=Xb.dot(w)

def sigmoid(z):
    return 1/(1+np.exp(-z))

print(sigmoid(z))
