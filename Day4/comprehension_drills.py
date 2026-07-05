# List Comprehension Drills

numbers = list(range(1, 21))
div_by_3 = [x for x in numbers if x % 3 == 0]

words = ["python", "cat", "computer", "book", "science"]
long_words = [word.title() for word in words if len(word) > 4]

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

nested = [[1, 2], [3, 4], [5, 6], [7, 8]]
flat = [item for sublist in nested for item in sublist]

dict_example = {x: x*x for x in range(5)}
set_example = {x*x for x in range(5)}

print(div_by_3)
print(long_words)
print(fahrenheit)
print(flat)
print(dict_example)
print(set_example)