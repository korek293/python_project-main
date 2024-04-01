fruits = ["banana", "apple", "cherry", "date"]

longest_word = max(fruits, key=lambda element: len(element))
print(longest_word)