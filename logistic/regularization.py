import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))


def plotcosts(X,Y,w,l1):
    learning_rate=0.001
    costs=[]
    for i in range(5000):
        Yhat=sigmoid(X.dot(w))
        delta=Yhat-Y
        w=w-learning_rate*(X.T.dot(w)+l1*np.sign(w))
        cost = -(Y*np.log(Yhat) + (1-Y)*np.log(1 - Yhat)).mean() + l1*np.abs(w).mean()
        costs.append(cost)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(costs)
    plt.xlabel("l1: %d"%l1)
    plt.ylabel("cross entropy cost")
    plt.subplot(212)
    plt.plot(true_w, label='true w')
    plt.plot(w, label='w_map')
    plt.legend()
    plt.show()
    print("final w:{}".format(w))
    print("true w: {}".format(true_w))



N=50
D=50

X=(np.random.random((N,D))-0.5)*10
true_w=np.array([1,-0.5,0.5]+(D-3)*[0])
Y=np.round(sigmoid(X.dot(true_w))+np.random.randn(N)*0.5)

w=np.random.randn(D)/np.sqrt(D)

l=[0.03,0.3,3,30,300,30000,300000]

for l1 in l:
    plotcosts(X,Y,true_w,l1)
