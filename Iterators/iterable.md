Iterator - an object that can be iterated upon. An object which returns data,
 one element at a time when next() is called on it

Iterable -  An object which will return an Iterator when iter() is called on it.

iter("HELLO") returns an iterator

"HELLO" is an iterable, but it is not an iterator.

NEXT
When next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error.