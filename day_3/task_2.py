#Find Second Largest Element in a List without function
data = [1, 2, 2, 3,5]
largest = float('-inf')
second_largest = float('-inf')
for item in data:
    if item > largest:
        second_largest = largest
        largest = item
    elif item > second_largest and item != largest:
        second_largest = item
print("Second Largest Element:", second_largest)
