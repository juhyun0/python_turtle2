import turtle
t=turtle.Turtle()

#n-각형을 그리는 함수 정의
def n_polygon(n, length):
	for i in range(n):
		t.forward(length)
		t.left(360//n) #정수 나눗셈은 //

for i in range(10):
	t.left(20)
	n_polygon(6,100)

