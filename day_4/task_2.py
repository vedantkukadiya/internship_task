#Function to Find Maximum and Minimum Values
def find_max_min(numbers):
    if not numbers:
        return None, None
    return max(numbers), min(numbers)
data = [56, 78, 90, 45, 67, 89]
max_value, min_value = find_max_min(data)
print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")