#Sorting in Python: sorting a list of metals which are sorted by the athomic number

earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
#sorting the data alphabetically:
earth_metals.sort()
print(earth_metals)
#sorting the data in reverse order:
earth_metals.sort(reverse=True)
print(earth_metals)

# if you try to do the sorting on a tuple it will crash.
