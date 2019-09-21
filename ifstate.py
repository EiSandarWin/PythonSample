#Week 3A 21.9.2019

#>>> x = int(input("Please enter an integer:"))
#>>> if x < 0:
#...     x = 0
#...     print('Negative changed to zero')
#... elif x == 0:
#...     print('zero')
#... elif x == 1:
#...     print('Single')
#...     print('More')
#...
#More

#x = int(input("Please enter an integer"))

#if x >= 40 and x <= 75:
#	print('Aged go to bagan')
#elif x < 40 and x >= 10:
#	print('Youth go to beach')
#elif x <= 10 and x >0:
#	print('Go to Playground')
#else:
#	print('unlisted')


#int(input("Examination Result:"))
#100 scholar
#70 destination
#50 excellent
#40 pass fail
#10 warning

x = int(input("Please enter your marks"))
if x == 100:
	print('You are scholar person', x)
elif x >= 70 and x < 100:
	print('You passed with destination', x)
elif x >= 50 and x < 70:
	print('You are excellent person', x)
elif x > 40 and x < 50:
	print('You passed' ,x )
elif x == 39 :
	x = x + 1
	print('You are modifation', x)
elif x == 38:
	x = x + 2
	print('You are modifation', x)
elif x == 37:
	x = x + 3
	print('You are modifation', x)
elif x == 36:
	x = x + 4
	print('You are modifation', x)
elif x == 35:
	x = x + 5 
	print('You are modifation', x)
elif x > 5 and x <=10:
	print('You try more and more', x)
else:
	print('I call your parents', x)


>>> words = ['cat', 'window', 'defenestrate', 'world']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
world 5
>>>

>>> words = ['cat', 'window', 'defenestrate', 'world']
>>> for w in words[:]:
...     if len(w) > 6:
...             words.append(w)
...
>>> words
['cat', 'window', 'defenestrate', 'world', 'defenestrate']

>>> words = ['cat', 'window', 'defenestrate', 'world']
>>> for w in words[:]:
...     if len(w) > 4:
...             words.insert(0, w)
...
>>> words
['world', 'defenestrate', 'window', 'cat', 'window', 'defenestrate', 'world']