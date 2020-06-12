"""
turtle graphics
"""

import turtle
import tkinter

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

def koch_draw(t,i=0,sl=100):
    """
    start drawing a koch snowflake\n
    t - turtle to command\n
    i - iterations\n
    sl - initial side length in pixels
    """
    # positioning #
    # put the center of the triangle on the center of the canvas

    # end positioning #

    # draw the snowflake #
    t.pd()
    koch(t,i=i,sl=sl)
    t.lt(120)
    koch(t,i=i,sl=sl)
    t.lt(120)
    koch(t,i=i,sl=sl)
    t.lt(120)
    t.pu()
    # end draw snowflake #

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
    # t.showturtle()
    t.hideturtle()

    # set turtle speed
    t.speed(0)
    # end turtle setup #

    # draw snowflake
    koch_draw(t,i=3,sl=400)


main()
input()