a=[1,2,3,2]
b=[2,5,6]
result=[]

for i in range(len(a)):
    flag=0
    for k in range(len(result)):
        if a[i]==result[k]:
            flag=1

    if flag==0:
        result.append(a[i])

for i in range(len(b)):
    flag=0
    for k in range(len(result)):
        if b[i]==result[k]:
            flag=1

    if flag==0:
        result.append(b[i])

print(result)