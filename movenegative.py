arr=[1,2,-1,-2,3]
pos=[]
neg=[]

for num in arr:
    if num >=0:
        pos.append(num)
    else:
        neg.append(num)


for i in range(len(pos)):
    arr[i]=pos[i]

for i in range(len(neg)):
    arr[len(pos)+i]=neg[i]

print(arr)
