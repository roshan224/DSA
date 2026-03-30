'''
arr=[2,3,4,2,3,4]
n=len(arr)
occ={}
for i in range(n):
    count=1
    for j in range(n):
        if arr[i]==arr[j]:
            count=count+1
    occ[arr[i]]=count
print(occ)
'''
arr1=[1,2,3,4]
arr2=[2,6,7,8]
n=len(arr1)
m=len(arr2)
occ={}

for i in range(n):
    count=0
    for j in range(m):
        if arr1[i]==arr2[j]:
            count=count+1
    occ[arr1[i]]=count

print(occ)
