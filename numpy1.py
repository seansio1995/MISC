import numpy as np
a=[[1,2,3],[4,5,6]]
a=np.matrix(a)
# print(a)

b=[[1,2],[2,3],[4,5]]
b=np.matrix(b)
print(np.matmul(a,b))
c=np.matmul(a,b)

print(np.array(c).T)
