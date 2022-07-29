testable = {'September': '16°C', 'December': '-10°C', 'July': '23°C'}

# this will remove both the key and the value from dictionary object
del testable['September']  
print(testable)  # {'December': '-10°C', 'July': '23°C'}

# throws a KeyError because there's no such key in the dictionary
# del testable['May']
 
# throws a KeyError, as we've already deleted the object by the key
# del testable['September']
print(testable)
# deletes the whole dictionary
del testable
print(testable)
