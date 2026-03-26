arr=[10,5,20,8]

first = second = third = -1

for num in arr:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second and num != first:
        third = second
        second = num
    elif num > third and num != second and num != first:
        third = num

print(third)