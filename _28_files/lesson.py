import csv

persons = [
    {'name': 'Jack', 'age': 26, 'occupation': 'Artist'},
    {'name': 'Emma', 'age': 32, 'occupation': 'Programmer'}
]

file = open("files/persons.csv", "a")

fields = ['name', 'age', 'occupation']
csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
csv_dict_writer.writerows(persons)

file.close()
