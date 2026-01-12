# word frequency counter
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}
for word in data:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word Frequency:", word_count)
