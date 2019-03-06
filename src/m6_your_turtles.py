"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Yoshio.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
yoshio = rg.SimpleTurtle('turtle')
yoshio.pen = rg.Pen('red',4)
yoshio.speed = 100

size = 150

for k in range(50):


    yoshio.forward(75)
    yoshio.backward(75)
    yoshio.right(360/50)

yoshio2 = rg.SimpleTurtle('turtle')
yoshio2.pen = rg.Pen('blue', 10)
yoshio2.speed = 10

yoshio2.pen_up()
yoshio2.forward(50)
yoshio2.left(90)
yoshio2.pen_down()

for k in range (8):
    yoshio.draw_circle(100)
    yoshio.forward(10)
    yoshio.right(45)

window.close_on_mouse_click()