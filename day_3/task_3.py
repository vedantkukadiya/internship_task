# Remove duplicate entries from a list while preserving the original order without function
data = [1, 2, 2, 3, 4, 4, 5]
unique_data = []
for item in data:
    if item not in unique_data:
        unique_data.append(item)    
print("List after removing duplicates:", unique_data)
