import turtle
import random

screen = turtle.Screen

colors = ["red", "blue", "green", "orange", "purple"]
turtles = []


start_y = 180

for i in range(4):
    t: turtle = turtle.Turtle()
    t.speed(10)
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-500, start_y - i * 100)
    turtles.append(t)

draw = turtle.Turtle()
draw.penup()
draw.goto(600, 250)
draw.pendown()
draw.right(90)
draw.forward(400)

winner = None
while not winner:  # keep looping until we find a winner
    for t in turtles:  # go through each turtle one by one
        distance = random.randint(1, 10)  # pick a random step
        t.forward(distance)  # move turtle forward by that step

        # check if the turtle has crossed the finish line
        if t.xcor() >= 600:
            winner = t.pencolor()  # save the winner's color
            break  # stop checking others
print(f"{winner} has won the race!!!")



#screen = turtle.Screen()

#def get_click_coordinates(x, y):

#    print(f"You clicked at: ({x}, {y})")

#screen.onscreenclick(get_click_coordinates)

turtle.done()