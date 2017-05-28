import matplotlib.pyplot as plt
import numpy as np

N=100
D=2


X=np.random.randn((100,2))
X[:50,:]=X[:50,:]-2*np.ones((50,D))
X[50:,:]=X[50:,:]+2*np.ones((50,D))

T=np.array([0]*50+[1]*50)



def sigmoid(z):
    return 1/(1+np.exp(-z))
