#myapproach
arr=[1,2,0,3,4]
result=[]
zero=0
for num in arr:
    if num==0:
        zero=zero+1   ##counts zero
    else:
        result.append(num)

result.extend([0]*zero)  ##multiplies that much zeroes counted
print(result)

##courseapproach
#arr=[1,2,0,3,4]
n=len(arr)
j=0
    	
for i in range(n):
    if arr[i]!=0:
    	arr[j]=arr[i]  ##arr=[1,2,3,4]
    	j=j+1
    	        
for i in range(j,n):
    arr[i]=0   ##arr=[1,2,3,4,0]
