# Shallow cloning
import copy
x=[10,20,[30,40],50]
y=copy.copy(x)
y[2][0]= 333
print("x:",x)
print("y:",y)
print("==========================")

# Deep cloning
x=[10,20,[30,40],50]
y=copy.deepcopy(x)
y[2][0]=333
x[2][1]=999
print("x:",x)
print("y:",y)