arr=[4,6,8,9,89,889,8889]
n=len(arr)
for i in range(n-1):
    if arr[i]>arr[i+1]:
        print(False)
print(True)