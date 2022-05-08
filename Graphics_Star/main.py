from graphics_trial import *
from turtle import Turtle


y = 0
speed('fastest')
whichOne = input('Which one \n dot_circle \n random_lines \n spirograph \n different_shape \n cross \n star: \n')
if whichOne == 'random_lines':
    random_lines()
elif whichOne == 'dot_circle':
    dot_circle()
elif whichOne == 'star':
    star()
elif whichOne == 'dashed_line':
    dashed_line()
elif whichOne == 'cross':
    cross()
elif whichOne == 'spirograph':
    # Loop for Spirograph
    for z in range(360):
        spiral_circle(z)
    spiral_circle(z)
elif whichOne == 'different_shape':
    # Loop for different shapes
    for i in range(3, 11):
        multiple_shape(i)
    multiple_shape(i)
else:
    print('Unknown!')

Screen().exitonclick()
# while True:
#     forward(200)
#     left(170)
#     print(pos())
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
