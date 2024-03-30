def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"

print(custom_greeting(name="John", greeting="Good morning"))
print(custom_greeting(name="John"))