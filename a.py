import numpy as np

a=np.array([[[[1,13,3],[4,5,6],[7,8,9],[10,11,12]],[[1,13,3],[4,5,6],[7,8,9],[10,11,17]]]])
whole_size=a.size
tmp=np.ravel(a)
for i in range(tmp.size):
    if tmp[i]>5:
        tmp[i]=0
tmp=np.reshape(tmp, a.shape)
print(tmp)