import random

while True:
	x=random.randint(1,100)
	y=random.randint(1,100)
	print(x,"+",y,"=",end="")
	answer=int(input())
	if answer == x+y:
		print("good")
	else:
		print("next")

