import numpy as np
from sklearn import linear_model

regr=linear_model.LinearRegression()
x_train=np.array([1,9,31,44]).reshape(4,1)
y_train=np.array([6,2.3,1.8,1.9]).reshape(4,1)

regr.fit(x_train,y_train)

print(regr.coef_)
print(regr.intercept_)
print(regr.score(x_train,y_train))
