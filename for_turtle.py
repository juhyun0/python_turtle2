#2부터 100사이의 모든 짝수 출력

x=2
for x in range(100):
	x=x+1
	if x%2 == 0:
		print(x,end="")





#눈모양

color=["red","blue","green","yellow","black","pink"]

x=1
for x in range(6):
	t.forward(100)
	t.forward(-30)
	t.left(60)
	t.forward(30)
	t.forward(-30)
	t.right(120)
	t.forward(30)
	t.forward(-30)
	t.goto(0,0)
	t.pencolor(color[x%6])
	x=x+1

t.forward(100)
t.width(3)
t.right(120)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)


t.left(60)

st=1
x=1

for x in range(10):
	t.forward(20)
	if st==1 :
		t.right(90)
		st=0
	else :
		t.left(90)
		st=1
	t.forward(200)
	if st==0 :
		t.left(90)
	else :
		t.right(90)
	x=x+1





