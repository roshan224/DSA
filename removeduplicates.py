arr=[1,2,2,3,3,4,5,6,7,8,8,8,9,9]

j=0
n=len(arr)
for i in range(0,n-1):
    if arr[i]!=arr[i+1]:
        arr[j]=arr[i]
        j=j+1

arr[j]=arr[n-1]

print(arr[:j+1])
