a=[1,2,3]
b=[3,1,2]
freq={}
for num in a:
    freq[num]=freq.get(num,0)+1

for num in b:
    if num not in freq:
        print(False)

    freq[num]-=1
    if freq[num]==0:
        del freq[num]
    
print(True)