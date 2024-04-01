def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True
    return old_dict, is_modified

product = {'id': 1, 'name': 'Laptop', 'price': 999.99}

product, was_modified = modify_dict(old_dict=product, name='Laptop')

print(product)
print(was_modified)