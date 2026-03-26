arr=[1,0,0,1,0]
i,j,k=0,0,len(arr)-1
while j<=k:
    if arr[j]==0:
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
        j=j+1
    else:
        arr[j],arr[k]=arr[k],arr[j]
        k=k-1
    
print(arr)