import turtle
t = turtle.Turtle()

a = 123

clr = 'red'

def draw_sq(x, y, clr):
  t.penup()
  t.goto(x, y)
  t.setheading(0)
  t.pendown()
  t.fillcolor(clr)
  t.begin_fill()
  for _ in range(4):
    t.forward(20)
    t.left(90)
  t.end_fill()
  t.penup()

#draw_sq(0, 0, 'red')
t.speed(0)
a = 234
import time

ts = turtle.Screen()
ts.tracer(0)


t.penup()

sty = 3

if sty == 0:
  pat = 0b000000011
if sty == 1:
  pat = 0b11000000
if sty == 2:
  pat = 0b11000011
if sty == 3:
  pat = 0b00000001

for cnt in range(1000):
  if sty == 0:
    pat = pat << 2
    if pat > 0b11111111: 
      pat = 0b00000011
  if sty == 1:
    pat = pat >> 2
    if pat == 0b00000000:
      pat = 0b11000000
  if sty == 2:
    pat = pat ^ 0b11111111
  if sty == 3:
    if pat == 0b11111111:
      pat = 0b00000000
    pat = pat | (1 << cnt%8)
  if sty == 5:
    pat = 0b01111111
    
  ts.tracer(0)
  for jj in range(8):
    b = (pat & (2**jj)) >> jj
    t.goto(100 - 40*jj, 40)
    t.write('b' + str(jj))
    if b == 1:
      draw_sq(100- 40*jj, 0, 'red')
    else:
      draw_sq(100 - 40*jj, 0, 'white')
  ts.update()
  time.sleep(0.5)

'''
ts.tracer(0)

x = 7 << 5

for _ in range(5):
  x = x >> 1
  for kk in range(8):
    b = (x & (2**kk)) >> kk
    if b == 1:
      draw_sq(0- 20*kk, 0, 'red')
    else:
      draw_sq(0 - 20*kk, 0, 'white')
  ts.update()
  time.sleep(0.5)

'''