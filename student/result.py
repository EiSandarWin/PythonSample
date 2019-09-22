import student
import mary

x = student.a["code"]
y = student.b["code"]
z = student.a["student"]
e = student.a["father"]
f = student.a["mother"]
print(x)
print(y)
print(z)
print(e)
print(f)

for i in range(len(mary.a)):
	print(i,mary.a[i])