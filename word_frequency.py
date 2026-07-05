sentence = "python is easy and python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_frequency = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

for word, count in sorted_frequency:
    print(f"{word}: {count}")