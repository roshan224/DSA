nums=[1,2,3,4,5]     
k=2   
b=[]
j=0
n=len(nums)
k=k%n
        
for i in range(0,n-k):
    b.append(nums[i])

for i in range(n-k,n):
    nums[j]=nums[i]
    j=j+1

n=len(b)
for i in range(n):
    nums[j] = b[i]
    j=j+1
print(nums)