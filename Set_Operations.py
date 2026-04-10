my_set = {10, 20, 'A', 'Bike'}
print(my_set)
my_set.add('Apple')
print(my_set)
my_set.update([70, 80])
print(my_set)
my_set.remove('A')
print(my_set)
my_set.discard(10)
print(my_set)
set1 = {2,4,6}
set2 = {3,6,9}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))