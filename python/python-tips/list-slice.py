"""
Explain Python's slice notation
In short, the colons (:) in subscript notation (subscriptable[subscriptarg]) make slice notation, which has the optional 
arguments start, stop, and step:

sliceable[start:stop:step]
Python slicing is a computationally fast way to methodically access parts of your data.

Important Definitions
To begin with, let's define a few terms:

start: the beginning index of the slice, it will include the element at this index unless it is the same as stop, 
defaults to 0, i.e. the first index. If it's negative, it means to start n items from the end.

stop: the ending index of the slice, it does not include the element at this index, defaults to length of the sequence 
being sliced, that is, up to and including the end.

step: the amount by which the index increases, defaults to 1. If it's negative, you're slicing over the iterable in reverse.

"""
e = ["a", "b" , "c", "d", "e", "f"]
e[2:4] = [2, 3]
print(e)
# ['a', 'b', 2, 3, 'e', 'f']
e[2:4] = [1, 2, 3, 4, 5]
print(e)
# ['a', 'b', 1, 2, 3, 4, 5, 'e', 'f']
e[2:7] = []
print(e)
# ['a', 'b', 'e', 'f']




