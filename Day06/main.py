# This is the solution to Reeborg's World's Maze Problem (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

# Creating dummy functions below to prevent undefined function issue. They are not required on Reeborg's World site. 

def turn_left():
    pass

def right_is_clear():
    pass

def move():
    pass

def front_is_clear():
    pass

def at_goal():
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def follow_right_wall():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
while front_is_clear():
    move()
turn_left()

while not at_goal():
    follow_right_wall()