l=[1,0,2,0,3,0]
for i in l:
    if i==0:
        l.remove(i)
        l.append(i)
print(l)