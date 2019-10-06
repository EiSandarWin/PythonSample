# Week 5B 6.10.2019

x = [1,2,3]
list.append(4)
x = [1,2,3,4]


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
list.extend()---------insert the last place
list.insert(1,5)--------insert value at key place
list.remove(3) ------delete seleted 
list.pop()------delete the last word and show
list.clear() ----all delete
list.reverse()-----all reverse
list.count('apple') -----count the quantity
list.index('kiwi') -------show the place 
list.sort()-----sort alphabatically



>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.append('coconut')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut']
>>> fruit.extend('cucumber')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruit' is not defined
>>> friots.extend('cucumber')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'friots' is not defined
>>> fruits.extend('cucumber')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut', 'c', 'u', 'c', 'u', 'm', 'b', 'e', 'r']
>>> fruits.extend('apple')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut', 'c', 'u', 'c', 'u', 'm', 'b', 'e', 'r', 'a', 'p', 'p', 'l', 'e']
>>> fruits.remove([8:]
  File "<stdin>", line 1
    fruits.remove([8:]
                    ^
SyntaxError: invalid syntax
>>> fruits.clear()
>>>
>>> fruits
[]
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.append('coconut')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut']
>>> fruits.reverse()
>>> fruits
['coconut', 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.index('kiwi')
3
>>> fruits.index('apple')
2
>>> fruits.index('apple')
2
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'coconut', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
>>> fruits
['apple', 'apple', 'banana', 'banana', 'coconut', 'kiwi', 'orange']
>>> fruits.remove()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: remove() takes exactly one argument (0 given)
>>> fruits.remove('kiwi')
>>> fruits
['apple', 'apple', 'banana', 'banana', 'coconut', 'orange']


>>> students = ['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko']
>>> students
['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko']
>>> students.append('Phyu Phyu')
>>> students.append('Ni Ni')
>>> students
['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko', 'Phyu Phyu', 'Ni Ni']
>>> students.remove('Mya Mya')
>>> students
['Mg Mg', 'Aye Aye', 'Ko Ko', 'Phyu Phyu', 'Ni Ni']
>>> students.pop('Ni Ni')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> students.pop()
'Ni Ni'
>>> students
['Mg Mg', 'Aye Aye', 'Ko Ko', 'Phyu Phyu']


>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")
>>> queue.append("Graham")
>>> queue
deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
>>> queue.popleft()
'Eric'
>>> queue.popleft()
'John'


>>> cube = []
>>> for i in range(10):
...     cube.append(i**2)
...
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> for i in range(20):
...     cube.append(i**3)
...
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> for i in range(10):
...     cube.append(i**3)
...
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> cube.clear()
>>> cube = list(map(lambda i: i**2, range(10)))
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube.clear()
>>> cube = [i**2 for i in range(10)]
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



[(x,y)]
if x !=y
for x in [1,2,3]
	for y in [3,1,4]
>>> [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...             if x != y:
...                     combs.append((x,y))
...
>>> combs
------------------------------------------------------

from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 10)]
['3.1', '3.14', '3.142', '3.1416', '3.14159', '3.141593', '3.1415927', '3.14159265', '3.141592654']




--------------------------------------------------------------------
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(3)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11]]


>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

 list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

>>> matrix = [
...     [1, 2, 3, 4, 5],
...     [6, 7, 8, 9, 10],
...     [11, 12, 13, 14, 15],
... ]
>>> list (zip(*matrix))
[(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]