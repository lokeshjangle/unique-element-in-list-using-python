l1=[1,2,3,1,2,5,6,6,7]
d={}
for i in l1:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]==1:
        print(i)