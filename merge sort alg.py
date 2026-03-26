def mergesort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        left=mergesort(arr[:mid])
        right=mergesort(arr[mid:])
        return merge(left,right)
        

def merge(left,right):
    result=[]
    i,j=0,0
    m=len(left)
    n=len(right)
    while i<m and j<n:
        if left[i]<right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    
    while i<m:
        result.append(left[i])
        i=i+1

    while j < n:
        result.append(right[j])
        j=j+1
        
    return result


print(mergesort([5,8,2,7]))