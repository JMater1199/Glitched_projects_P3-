import turtle as t
t1 = t.Turtle()
t1.shape('arrow')





#seetup

t1.pencolor('gold')
t1.pensize(3)
t.bgcolor('black')

def strange(x,y,l):

 
 t1.penup()
 t1.goto(x,y)
 t1.pendown()
 
 t1.penup()
 t1.goto(0,-x)
 t1.pendown()
 t1.circle(x)
 t1.penup()
 t1.goto(x/5*4,-x/5*3)
 t1.pendown()
 t1.goto(0,x)
 t1.goto(-x/5*4,-x/5*3)
 t1.goto(x/5*4,-x/5*3)
 
 
 if l > 10:
    strange(x + 3/4*l, y+ 1/4*l, l/2)
    #strange(x - 1/4*l, y+ 1/4*l, l/2)
    #strange(x + 1/4*l, y- 1/2*l, l/2)
#t.bgcolor('white')
#t.clear
#t.mainloop
t1.goto(0,0)
t1.color('black')
t1.clear
t1.color('gold')


def branch(sz, level):
  if level > 0:
    t1.forward(sz)
    t1.right(30)
    branch(0.8*sz, level -1)
    t1.right(-60)
    branch(0.8*sz, level -1)
    t1.right(30)
    t1.forward(-sz)


t1.goto(0, 0)
strange(-100, -100, 200)

input()
t1.speed(0)
t1.clear()
t1.penup()
t1.goto(0, -150)
t1.pendown()
t1.setheading(90)

branch(80, 10)


