#Find Unique Elements and Their Frequency without function
data = [1, 2, 2, 3, 4, 4, 4, 5]
unique_elements = []
frequency = []
for item in data:
    if item not in unique_elements:
        unique_elements.append(item)
        frequency.append(1)
    else:
        index = unique_elements.index(item)
        frequency[index] += 1
print("Unique Elements:", unique_elements)
print("Frequency:", frequency)