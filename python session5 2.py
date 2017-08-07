from turtle import*
speed(-1)
length = int(input("What's the length of your square"))
colors = input("What's the color")
shape("turtle")
def draw_square(a,b):
    color(b)
    for n in range(4):
     forward(a)
     left(90)
     
draw_square(length,colors)


for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
