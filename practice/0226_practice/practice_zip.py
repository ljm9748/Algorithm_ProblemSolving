a=[1,2,3,10]
b=[1,3,5,7]
temp=zip(a,b)
print(list(temp))
temp3=[a,b]
temp2=sorted(temp3,key=lambda x:x[2],reverse=True)

print(temp2)