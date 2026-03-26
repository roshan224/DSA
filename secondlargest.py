arr=[1,2,3,4,5]
n=len(arr)
largest=arr[0]
slargest=-1
for i in range(n):
    if arr[i]>largest:
        slargest=largest
        largest=arr[i]
    
    if arr[i]<largest and arr[i]>slargest:
        slargest=arr[i]
print(slargest)