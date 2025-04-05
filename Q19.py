# Aliasing
x=[10,20,30,40]
y=x
y[1]=999
print("x:",x)
print("y:",y)
print("==============================")

# cloning
x=[10,20,30,40]
y=x[:]   #OR  y=x.copy()
print("x:",x)
print("y:",y)
