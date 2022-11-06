# dictionary: uses {}, is ordered (since 3.7), changeable and do not allow duplicates.
playstation = {'name': 'playstation', 'color': 'gray'}
print(f"create a dictionary: playstation {playstation}")
print(f"this {playstation['name']} is {playstation['color']}")

# add a new key-value
playstation['model'] = 'psOne'
print(f"\nadd a model key-value: {playstation}")
print(f"this {playstation['name']} is {playstation['color']} and is a {playstation['model']}")

# delete a key-value
del playstation['model']
print(f"\ndeleted the model key-value: {playstation}")

# dictionary loop using the items() method
print(f"\nloop through key-value of: {playstation['name']}")
for key, value in playstation.items():
    print(f"{key}: {value}")

# add a list in a dictionary
games = ['final fantasy vii', 'metal gear solid', 'chocobo racing']
playstation['games'] = games

print(playstation)
print(f"\nloop through key-value of {playstation['name']} with added game list")
for key, value in playstation.items():
    print(f"{key}: {value}")