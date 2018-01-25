def test():
	import random

	num_list = [1, 2, 3, 4, 5]
	unique = num_list[random.randint(0, 4)]
	
	return num_list[unique]

	#I added this code. 

x = test()
print(x)