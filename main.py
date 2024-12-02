# Import the robot control commands from the library
from simulator import robot
import time

'''
 Project Requirements:
* [ ] robot moves
* [ ] robot does not crash into the walls of the box
* [ ] at least 5 calls to input
* [ ] at least 5 functions
* [ ] at least 2 functions have at least one parameter
* [ ] at least 2 functions have return values and at least one call to the function is assigned to a variable
* [ ] each motor moves at least once
* [ ] the robot's movement changes based on at least 5 readings of the sonar sensors**** Wait for new code update to implement this part!!
* [ ] use at least 1 while loop OR recursive function call
* [ ] at least one command (user input) causes the robot to move autonomously for at least 20 seconds

Dr. EB Todo:
* [ ] implement sonar distance in simulator
* [ ] add border to robot so you can tell when it's going to hit the wall
* [ ] add noise to simulator motors and sonars
* [ ] simplify main.py
 
 
'''

# left, right = robot.sonars()

print("Hi! My name is RoboBunny!")

def start(): 
    action = str(input("What would you like me to do? The options are move, turn, or dance."))
    if action == ("turn") or ("Turn"):
            turning()
    elif action == ("move") or ("Move"):
            moving()
    elif action == ("dance") or ("Dance"):
            dance()
    elif action == ("stay") or ("Stay"):
            stay()
    else:
            print("Sorry! That is not a valid input. Please try again!")
            start()

def turning ():
    if input("Do you want to turn right?") == "Yes" or "yes" or "YES":
        x = -1
        y = 1
        seconds = float(input("For how long do you want me turn?"))
        robot.motors(x, y, seconds)
    elif input("Do you want to turn left") == "Yes" or "yes" or "YES":
        x = 1
        y = -1
        seconds = float(input("For how long do you want me turn?"))
        robot.motors(x, y, seconds)
    else:
        moving()

def moving():
    direction = str(input("Do you want me to move forward or backward?"))
    seconds = float(f.(input("For long do you want me to go {number of seconds}")))
    if direction == "forward":
        robot.motors(1,1,seconds)
    elif direction == "backward": 
        robot.motors(-1,-1,seconds)
    else:
        start()

def stay():
    robot.motors(0,0,5)
    print("Now I'm staying in the same place and I'm bored!")
    what_to_do = (input("Should I turn, dance, move, or stay?"))
    if what_to_do == "turn" or "Turn":
        turning()
    if what_to_do == "dance" or "Dance":
        dance()
    if what_to_do == "move" or "Move":
        moving()
    if what_to_do == "stay" or "Stay":
        print("I don't want to stay here :( I'm bored! Please pick something else for me to do.")
        start()
    else:
        "I can't do that! try again!"
        stay()


def dance():
    print("Lets dance!!!")
    while True:
        robot.motors(1,1,2)
        robot.motors(-1,-1,2)
        robot.motors(-1,1,5)
        robot.motors(1,-1,5)
    
start()


    






robot.exitonclick()

