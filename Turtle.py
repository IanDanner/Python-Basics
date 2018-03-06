import turtle
colors=['red','yellow','green','red','yellow','green']
turtle.bgcolor('black')
DIST = 5
for x in range(0,45):
    print "x", x
    turtle.pencolor(colors[x%6])
    turtle.left(45)
    for y in range(1,20):
        print "y", y
        turtle.right(15)
        
        turtle.forward(DIST)
    DIST += 1