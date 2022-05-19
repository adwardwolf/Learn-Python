# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

capitals = {
    'USA': 'Washington DC',
    'India': 'New Dehli',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

print("Capital of Russia:", capitals['Russia'])
print("Capital of Germany:", capitals.get('Germany'))
print("All keys in dictionary:", capitals.keys())
print("All values in dictionary:", capitals.values())
print("All items in dictionary:", capitals.items())

for key, value in capitals.items():
    print(key, value)

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'New York'})
capitals.pop('China')
