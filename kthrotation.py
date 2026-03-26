arr=[5,1,2,3,4]
n=len(arr)
h=n-1
k=0
i=0
while i<=n-1:
    if arr[i]>arr[h]:
        k=k+1

print(k)
        