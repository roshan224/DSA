#kthrotation
arr=[4,5,1,2,3]
n=len(arr)
l,h=0,n-1
ans=0
mid=l+(h-l)//2
l=mid-1
h=mid+1

while l<=h:
    if arr[mid]<arr[l] and arr[mid]<arr[h]:
        print(mid)

    if arr[h]>mid:
        h=mid-1
    else:
        ans=mid
        l=mid+1
        break
        


