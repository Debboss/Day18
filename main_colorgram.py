# import colorgram

# rgb_colors = []

# colors = colorgram.extract('syndra.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(29, 26, 59), (59, 42, 115), (48, 21, 60), (80, 65, 155), (121, 64, 138), (121, 83, 206), (90, 39, 105), (168, 85, 203), (194, 124, 209), (248, 215, 250), (253, 251, 249), (230, 156, 241), (162, 129, 218), (228, 228, 247), (242, 251, 246), (186, 161, 239), (192, 144, 137), (122, 84, 77), (60, 42, 35), (134, 175, 148), (167, 108, 102), (75, 104, 85), (231, 173, 164), (87, 52, 49), (35, 54, 43), (155, 214, 181), (95, 150, 111), (74, 146, 168), (48, 74, 57), (206, 198, 162)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

