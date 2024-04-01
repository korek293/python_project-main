people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30},
]

def is_adult(person: dict) -> bool:
    return person["age"] >= 18

filered_people = list(filter(is_adult, people))
print(filered_people)