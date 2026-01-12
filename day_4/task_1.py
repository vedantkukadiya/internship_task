#Function to Calculate Mean of a List
def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
data = [56, 78, 90, 45, 67, 89]
mean_value = calculate_mean(data)
print(f"The mean of the list is: {mean_value}")