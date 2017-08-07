from turtle import *
speed(-1)
x = int(input("X?"))
y = int(input("Y?"))

length = int(input("What's the length?"))
def draw_star(a,b):
      forward(a)
      left(90)
      forward(b)
      right(54)
      for i in range (5):
           forward(length)
           left(144)
           
draw_star(x,y)
