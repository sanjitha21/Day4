#Iterator in Python
numbers = [10, 20, 30, 40]


it = iter(numbers)

print(it)          
print(next(it))   
print(next(it))       
print(next(it))      
print(next(it))       

for num in numbers:
    print(num)

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

name = "Python"
name_iter = iter(name)
print(next(name_iter))
print(next(name_iter)) 
print(next(name_iter))

print("Is list iterable?", hasattr([1, 2, 3], "__iter__"))
print("Is list iterator?", hasattr([1, 2, 3], "__next__"))

iter_obj = iter([1, 2, 3])
print("Iterator object has __next__?", hasattr(iter_obj, "__next__"))
print(next(iter_obj))


