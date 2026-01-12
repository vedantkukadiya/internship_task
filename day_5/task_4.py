#Dictionary Comprehension for Data Transformation
raw_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
squared_data = {key: value**2 for key, value in raw_data.items()}
print(f"Transformed Dictionary: {squared_data}")