##i = 3
##for number in range(10):
##    i = i + 1
##    print(i)


from turtle import*
shape("turtle")

i = 2
for side in range(4):
 i = i + 1
 for number in range(i):
    forward(100)
    left(360 / i)
    if i % 2:
        color("blue")
    else:
        color("red")
  
