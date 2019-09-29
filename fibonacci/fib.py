 def fibo(n):
 	a, b = 0, 1
 	while a < n:
		print(a,end=' ')
		a, b = b, a + b
 	print()

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

# def fibo(n):
#  	a, b = 3, 4
#  	while a < n:
#  		print(a,end=' ')
#  		a, b = b, a + b
#  	print()



def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result