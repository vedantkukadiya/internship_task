#Clean a List Using List Comprehension
data = [56, -78, 90, -45, 67, -89]
cleaned_data = [num for num in data if num >= 0]
print(f"Cleaned list: {cleaned_data}")
