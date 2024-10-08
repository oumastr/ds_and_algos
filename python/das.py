# Lists
# Might contain items of different types, but usually the items
# all have the same type
squares = [1, 4, 9, 16, 25]
print(squares) # Outputs: 1, 4, 9, 16, 25
# Lists can be indexed
print(squares[2]) # Output: 9
# Lists are mutable(changeable cintent):
squares[2] = 400
print(squares) # Output: 1, 4, 400, 9, 16, 25
# To add new item to the list: append()
print(squares.append(0)) # Output: 1, 4, 400, 9, 16, 25, 0
# List length: len()
print(len(squares)) # Output: 7
# Lists can be nested: Creating list that contains lists
list_one = ['a', 'b', 'c']
list_two = [1, 2, 3]
list_three = [list_one, list_two]
print(list_three) # Output: ['a', 'b', 'c'], [1, 2, 3]
# Methods on Lists
#
sample_list = [1, 2, 3, 4]
# .append(): add an item to the end of list. Equivalent to a[len(a):] = [x]
print(sample_list.append(5)) # Output: 1, 2, 3, 4, 5
# .extend(iterable): Extend the list by appending all items from the iterable. Equivalent to a[len(a):] = iterable
print(list_one.extend(list_two)) # Just like nesting
# .insert(i, x): Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x)
print(sample_list.insert(5, 6)) # Output: 1, 2, 3, 4, 5,6
# .remove(x): Remove the first item from the list whose value is equal to x. Raises ValueError if there is no such item
sample_list = [1, 2, 3, 4, 7]
print(sample_list.remove(7)) # Returns: None because there is no first item whose value = 7
# .pop([i]): remove the item at a given position in the list, and return it. 
sample_list = [1, 2, 3, 4, 7]
print(sample_list.pop(2)) # Returns: 3
# if no index is specified, a.pop() removes and returns the last item in the list.
# returns IndexError if the list is empty or the index is outiside the list range.
# .clear(): remove all items from the list. Equvalent to del a[:]
# .index(x[, start[, end]]): return zero-based index in the first item whose value is equal to x. Raises ValueError if there is no such item.
# .count(x): return number of times x appears in the list.
sample_list = [1, 2, 3, 4, 7]
print(sample_list.count(3)) # Should return 1
# .sort(*, key=None, reverse=False): sort the items of the list in place
# .reverse(): reverse the elements of the list in place
# .copy(): return a shalloe copy of the list. Equivalent to a[:]
#
# Using Lists as Ques (first-in, first-out) but it is not effective
# Use collections.deque to implement a queue
from collections import deque

queue = deque(['John', 'Jane', 'Doe'])
queue.append('Oloo') # Oloo arrives
queue.append('Flopp') # Flopp arrives
queue.popleft() # The first to arrive now leaves
# 'John'
queue.popleft() # The second to arrive now leaves
# 'Jane'
queue # >>> deque(['Doe', 'Oloo', 'Flopp'])
#
# List Comprehensions: Provide a concise way to create lists.
sq = []
for x in range(10):
    sq.append(x**2)
    print(sq) # >>> [0, 1, 4, ..., 81]
#
sq = list(map(lambda x: x**2, range(10))) # or
sq = [x**2 for x in range(10)]
#
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# equivalent to
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
# >>> combs
# [(1, 3), (1, 4), (2, 3), ..., (3, 4)]
#
#
# 


# Tuples: Consist of a number of values separated by comma enclosed in parentheses.
# empty tuple sample:
empty_tuple = ()
filled_tuple = (23, 'Hello', 'Jane Doe')
another_tuple = x, y, z # The reverse op is possible:
x, y, z = another_tuple


# Sets: An unordered collection with no duplicate elements.
# Uses: 1. Membership testing. 2. Eliminating duplicate entries.
# To create sets: set() or {} are used.
# To create an empty set we use, set() and not {} which creates an empty dictionary
girlfriends = {'Jane', 'Doe', 'Joyce', 'Lavy'}
print(girlfriends) # Outputs the list and removes the duplicates
# Set comprehensions are also supported
sample_set = {i for i in 'abracadabra' if i not in 'abc'}
print(sample_set) # Output: {'r', 'd'}
#

# Dictionary: {} creates an empty dictionary.
book_store = {'Tom Clancy': 3004, 'Rudolph Onyango': 2003, 'Tolstoy Oloo': 1002}
book_store['Jacob Aliet'] = 2009
print(book_store) # Output: {'Tom Clancy': 3004, 'Rudolph Onyango': 2003, 'Tolstoy Oloo': 1002, 'Jacob Aliet': 2009}
# 
# Looping Techniques: When looping through a sequence, the key and corresponding value can be retrieved at the same time using the items() method.
swords = {'longclaw': 'house mormont', 'heartsbane': 'house tarlly', 'ice': 'house stark'}
for k, v in swords.items():
    print(k, v) # longclaw house mormont, ..., ice house stark
# position index and corresponding value use enumerate()
# loop over more sequences at the same time use: zip() function
m = []
n = []
for x, y in zip(m, n):
    print('what is your{0}? It is {1}.'.format(x, y))
# to loop over a sequence in reverse: reversed()
for i in reversed(range(1, 10, 2)):
    print(i)
# 9
# 7
# 5
# 3
# 1
#
# To loop over a sequence in a sorted order: sorted()
x = []
for i in sorted(x):
    print(i)
