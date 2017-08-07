
from turtle import *
speed(-1)
x = int(input("X?"))
y = int(input("Y?"))

length = int(input("What's the length?"))
def draw_star(a,b,c):
      forward(a)
      left(90)
      forward(b)
      right(54)
      for i in range (5):
           forward(c)
           left(144)
           
draw_star(x,y,length)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
