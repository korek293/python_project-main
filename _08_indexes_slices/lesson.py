greeting = "Hello, world!"

indexes = []
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        count += 1
        indexes.append(i)
print(count)
print(indexes)