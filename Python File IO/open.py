
 # Week 4A 28.9.2019

# f = open('test.txt', 'r') # r - read
# print(f.name)

# f.close()

# with open('test.txt', 'a') as g:

	
# 	print( g.write('6.This is line number 6'+"\n"),end='')

# with open('test.txt', 'r') as f:

# # 	f_text = f.readline()
# # 	print(f_text, end='')

# # 	f_text = f.readline()
# # 	print(f_text, end='')

# 	c

	# f_text = f.read(500)
	# print(f_text,end='')

# with open('test.txt','a') as g:
	# i = g.write("\n" + '6.This is Line Number 6')
# 	print(g.write("\n" + '6.This is Line Number 6'), end='')

# with open('test.txt','a') as g:
# 	 i = g.write("\n" + '6.This is Line Number 6')
# 	print(i, end='')

with open('test.txt', 'r') as f:

	size_to_read =500
	f_text = f.read(size_to_read)

	while len(f_text)>0:
		print(f_text,end='')