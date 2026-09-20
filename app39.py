"""Iterator in Python

An iterator is an object that allows you to traverse through a collection one element at a time.
It implements two methods:
    - __iter__() -> returns the iterator object itself
    - __next__() -> returns the next item, or raises StopIteration at the end

Key Points:
- Iterables are objects like lists, tuples, strings, dictionaries, sets, etc.
- An iterator is the object used to iterate over an iterable.
- We can get an iterator using the iter() function.
- We move through items using next().
"""

# Example 1: Using a list as an iterable
numbers = [10, 20, 30, 40]

# get an iterator object
it = iter(numbers)

print(it)              # <list_iterator object at ...>
print(next(it))        # 10
print(next(it))        # 20
print(next(it))        # 30
print(next(it))        # 40
# print(next(it))      # raises StopIteration

# Example 2: Iterating with a for loop
for num in numbers:
    print(num)

# Example 3: Creating a custom iterator
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        value = self.start
        self.start += 1
        return value

r = MyRange(1, 5)
for x in r:
    print("Custom iterator:", x)

# Example 4: Using iter() and next() with a string
name = "Python"
name_iter = iter(name)
print(next(name_iter))  # P
print(next(name_iter))  # y
print(next(name_iter))  # t

# Example 5: Difference between iterable and iterator
# A list is iterable, but not an iterator itself.
print("Is list iterable?", hasattr([1, 2, 3], "__iter__"))
print("Is list iterator?", hasattr([1, 2, 3], "__next__"))

# A real iterator has __next__
iter_obj = iter([1, 2, 3])
print("Iterator object has __next__?", hasattr(iter_obj, "__next__"))
print(next(iter_obj))

# Summary:
# - iter(obj) creates an iterator from any iterable.
# - next(iterator) returns the next item.
# - StopIteration is raised when there are no more items.
# - Iterators are useful for lazy processing and memory efficiency.
