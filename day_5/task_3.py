#Real-World Data Analysis Workflow (Mini Simulation) try and expection
raw_data = ["23", "45", "NA", "34", "", "56", "error", "42"]

clean_data = []

for value in raw_data:
    try:
        clean_data.append(int(value))
    except ValueError:
        continue

average = sum(clean_data) / len(clean_data)

print("Cleaned Data:", clean_data)
print("Average Value:", average)
