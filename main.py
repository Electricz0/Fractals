"""
turtle graphics
"""

import turtle
import math

def koch_draw(t,i=0,sl=100):
    """
    start drawing a koch snowflake\n
    t - turtle to command\n
    i - recursion level\n
    sl - initial side length in pixels
    """
    # start algorithym #
    def koch(t,i=0,sl=100):
        if i == 0:
            t.fd(sl)
        elif i > 0:
            koch(t,i=i-1,sl=sl/3)
            t.rt(60)
            koch(t,i=i-1,sl=sl/3)
            t.lt(120)
            koch(t,i=i-1,sl=sl/3)
            t.rt(60)
            koch(t,i=i-1,sl=sl/3)
    # end algorithym #

    # positioning #
    # put the center of the triangle on the center of the canvas
    # vector to the appropriate start position
    t.pu()
    t.rt(150)
    t.fd( sl / math.sqrt(3))
    t.lt(150)
    # end positioning #

    # draw the snowflake #
    t.pd()
    koch(t,i=i,sl=sl)
    t.lt(120)
    koch(t,i=i,sl=sl)
    t.lt(120)
    koch(t,i=i,sl=sl)
    t.lt(120)
    # end draw snowflake #

    # return home
    t.pu()
    t.lt(30)
    t.fd( sl / math.sqrt(3))
    t.rt(30)

def tree_draw(t,i=0,sl=100,fctr=.8,theta=20):
    """
    will draw a tree fractal

    t - turtle to command\n
    i - recursion depth\n
    sl - stem length\n
    fctr - size of deeper stem related to current stem
    theta - angle of branches
    """
    if i > 0:
        t.pd()
        t.fd(sl)
        t.lt(theta)
        tree_draw(t,i=i-1,sl=sl*fctr,fctr=fctr,theta=theta)
        t.pu()
        t.rt(2 * theta)
        t.pd()
        tree_draw(t,i=i-1,sl=sl*fctr,fctr=fctr,theta=theta)
        t.pu()
        t.lt(theta)
        t.bk(sl)
    elif i == 0:
        t.fd(sl)
        t.bk(sl)


def main():
    """
    program start function
    """
    # screen setup #
    # create screen
    s = turtle.Screen()

    # initialize screen
    s.setup(
        width=600,
        height=600,
        startx=0,
        starty=0
    )

    # set screen title
    s.title("Fractals")
    # end screen setup #

    # turtle setup #
    # create turtle
    t = turtle.RawTurtle(s)

    # show the turtle
    t.showturtle()
    # t.hideturtle()

    # set turtle speed
    t.speed(0)

    # start with the pen up
    t.pu()
    # end turtle setup #

    # draw here #
    # sl=150
    # t.setpos(-200,100)
    # koch_draw(t, i=0, sl=sl)
    # t.setpos(0,100)
    # koch_draw(t, i=1, sl=sl)
    # t.setpos(200,100)
    # koch_draw(t, i=2, sl=sl)
    # t.setpos(-200,-100)
    # koch_draw(t, i=3, sl=sl)
    # t.setpos(0,-100)
    # koch_draw(t, i=4, sl=sl)
    # t.setpos(200,-100)
    # koch_draw(t, i=5, sl=sl)

    t.seth(90)
    t.setpos(0,-100)
    tree_draw(t,i=15)
    # end drawing #
    

    # halt till input
    input()
main()