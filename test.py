arr=[2,4,1,3,5]
n=len(arr)
count=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j] or arr[i]>arr[j]:
            count=count+1


print(count)