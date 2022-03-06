
from datetime import datetime as time

j = [z for z in range(10)]

# Nested for loop (5 lines)
res = []
m1_0 = time.now()
for a in j:
	temp_res = []
	for b in j:
		temp_res.append(b)
	res.append(temp_res)
m1_1 = time.now()
print("Method 1: %s" % repr(res))
print("Executed in: %s seconds" % str(m1_1 - m1_0))

# Double list comprehension
m2_0 = time.now()
res  = [[b for b in [a for a in j]] for z in j]
m2_1 = time.now()

print("Method 2: %s" % repr(res))	
print("Executed in: %s seconds" % str(m2_1 - m2_0))
