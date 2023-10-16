# This file was created by: Ryan McElroy

'''
Goals:
When a user click on their choice, the computer randomly chooses and displays the result 

'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os

print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170


# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
cpu_rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
cpu_paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
cpu_scissors_instance = turtle.Turtle()


def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def rock(x,y):
    # add the cpu_rock image as a shape
    screen.addshape(cpu_rock_image)
    # attach the cpu_rock_image to the cpu_rock_instance
    cpu_rock_instance.shape(cpu_rock_image)
    # remove the pen option from the cpu_rock_instance so it doesn't draw lines when moved
    cpu_rock_instance.penup()
    # set the position of the cpu_rock_instance
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def paper(x,y):
    # add the cpu_paper image as a shape
    screen.addshape(cpu_paper_image)
    # attach the cpu_paper_image to the cpu_paper_instance
    cpu_paper_instance.shape(cpu_paper_image)
    # remove the pen option from the cpu_paper_instance so it doesn't draw lines when moved
    cpu_paper_instance.penup()
    # set the position of the cpu_paper_instance
    cpu_paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)

def scissors(x,y):
    # add the cpu_scissors image as a shape
    screen.addshape(cpu_scissors_image)
    # attach the cpu_scissors_image to the cpu_scissors_instance
    cpu_scissors_instance.shape(cpu_scissors_image)
    # remove the pen option from the cpu_scissors_instance so it doesn't draw lines when moved
    cpu_scissors_instance.penup()
    # set the position of the cpu_scissors_instance
    cpu_scissors_instance.setpos(x,y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)

# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup()

# this function uses and x y value, an obj, and width and height to find where the object is
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

text.setpos(0,150)
text.write("Choose rock or paper or scissors", False, "left", ("Arial", 24, "normal"))

# function that passes through wn onlick

hideturtle

import time 
import random
cpu_paper_instance.penup()
cpu_rock_instance.penup()
cpu_scissors_instance.penup()  
my_list = ["paper", "rock", "scissors"]
cpu_action = random.choice(my_list)

def mouse_pos(x, y):
    if collide(x,y,rock_instance, rock_w, rock_h):
        user_action = "rock"
        print('You chose rock!')
        text.clear()
        text.setpos(0,150)
        text.write("You chose rock!", False, "left", ("Arial", 24, "normal"))
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        time.sleep(1.5)
        text.clear()

    elif collide(x,y,paper_instance, paper_w, paper_h):
        user_action = "paper"
        print('You chose paper!')
        text.clear()
        text.setpos(0,150)
        text.write("You chose paper!", False, "left", ("Arial", 24, "normal"))
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        time.sleep(1.5)
        text.clear()
        time.sleep(1.5)
        text.clear()
        
    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        user_action = "scissors"
        print('You chose scissors!')
        text.clear()
        text.setpos(0,150)
        text.write("You chose scissors!", False, "left", ("Arial", 24, "normal"))
        paper_instance.hideturtle()
        rock_instance.hideturtle()
        time.sleep(1.5)
        text.clear()
        time.sleep(1.5)
        text.clear()
    else:
        print("Ur dumb!")
        text.clear()
        text.setpos(0,150)
        text.write("Ur dumb!", False, "left", ("Arial", 24, "normal"))
        time.sleep(2)
        text.clear()    

        

    if cpu_action == user_action:
        text.write(f"Cpu chose {cpu_action}!", False, "left", ("Arial", 24, "normal"))
        if cpu_action == "rock":
            rock(300,0)
            show_rock(0,0)
            rock(0,0)
            text.clear()
            text.write(f"You tied!", False, "left", ("Arial", 24, "normal"))
        elif cpu_action == "paper":
            paper(300,0)
            show_paper(0,0)
            paper(0,0)
            text.clear()
            text.write(f"You tied!", False, "left", ("Arial", 24, "normal"))
        elif cpu_action == "scissors":
            scissors(300,0)
            show_scissors(0,0)
            scissors(0,0)
            text.clear()
            text.write(f"You tied!", False, "left", ("Arial", 24, "normal"))
        else:
            print("error")
    elif user_action == "rock":
        if cpu_action == "scissors":
            text.write(f"Cpu chose scissors!", False, "left", ("Arial", 24, "normal"))
            scissors(300,0)
            time.sleep(1)
            show_rock(0,0)
            scissors(0,0)
            text.clear()
            text.write(f"You win!", False, "left", ("Arial", 24, "normal"))
        else:
            text.write(f"Cpu chose paper!", False, "left", ("Arial", 24, "normal"))
            paper(300,0)
            time.sleep(1)
            show_rock(0,0)
            paper(0,0)
            text.clear()
            text.write(f"You lose!", False, "left", ("Arial", 24, "normal"))

    elif user_action == "paper":
        if cpu_action == "rock":
            text.write(f"Cpu chose rock!", False, "left", ("Arial", 24, "normal"))
            rock(300,0)
            time.sleep(1)
            show_paper(0,0)
            rock(0,0)
            text.clear()
            text.write(f"You win!", False, "left", ("Arial", 24, "normal"))
        else:
            text.write(f"Cpu chose scissors!", False, "left", ("Arial", 24, "normal"))
            scissors(300,0)
            time.sleep(1)
            show_paper(0,0)
            scissors(0,0)
            text.clear()
            text.write(f"You lose!", False, "left", ("Arial", 24, "normal"))

    elif user_action == "scissors":
        if cpu_action == "paper":
            text.write(f"Cpu chose paper!", False, "left", ("Arial", 24, "normal"))
            paper(300,0)
            time.sleep(1)
            show_scissors(0,0)
            paper(0,0)
            text.clear()
            text.write(f"You win!", False, "left", ("Arial", 24, "normal"))
        else:
            text.write(f"Cpu chose rock!", False, "left", ("Arial", 24, "normal"))
            rock(300,0)
            time.sleep(1)
            show_scissors(0,0)
            rock(0,0)
            text.clear()
            text.write(f"You lose!", False, "left", ("Arial", 24, "normal"))











    if random.choice(my_list) == "rock":
        text.write(f"Cpu chose {cpu_action}!", False, "left", ("Arial", 24, "normal"))
        time.sleep(1)


# user this to get mouse position
screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()