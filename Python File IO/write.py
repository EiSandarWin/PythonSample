# with open('test.txt', 'r') as rf:
# 	with open('testCOPY.txt', 'w') as wf:

# 		for line in rf:
# 			wf.write(line)

 with open('img', 'rb') as rf:
 	with open('catCOPY.png', 'wb') as wf:

		arr = [[] for i in range (4)]
		arr
			[['img1.jpg'],['img2.jpg'], ['img3.jpg'],[]


# with open('img1.jpg','rb') as rf:
# 	with open('catCOPY.jpg','wb') as wf:
# 		chunk_size = 4096
# 		rf_chunk = rf.read(chunk_size)

# 		while len(rf_chunk) > 0:
# 			wf.write(rf_chunk)
# 			rf_chunk = rf.read(chunk_size)

