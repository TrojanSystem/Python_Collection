from turtle import *

color('red', 'yellow')
begin_fill()
left(36)
while True:
    forward(200)

    left(144)

    if abs(pos()) < 1:
        break

left(-36)
forward(162)

left(90)
forward(190)

left(90)
forward(200)

left(90)
forward(190)

left(90)
home()

end_fill()
done()
Screen().exitonclick()
# while True:
#     forward(200)
#     left(170)
#     print(pos())
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
