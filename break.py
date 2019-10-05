#week 4B 29.9.2017

#if break statement
# for n in range(2,10):
# 	for x in range(2,n):
# 		if n % x ==0:
# 			print(n,'equals', x, '*', n//x)
# 			break
# 		else:
# 			print(n,'is a prime number')

for n in range(3,12):
	for x in range(3,n):
		if n % x == 0:
			print(n,'equals',x , '*', n//x)
			break
		else:
			print(n, 'is a prime number')





#if continue statement
# for num in range(2, 10):
# 	if num % 2 == 0:
# 		print("found a number",num)
# 		continue
# 	print("found a number",num)