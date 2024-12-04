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


def turn():
    direction = str(input("Do you want me to turn clockwise or counter-clockwise?"))
    if direction == "clockwise":
        x = -1
        y = 1
        seconds = float(input("For long do you want me to go {number of seconds}"))
        robot.motors(x, y, seconds)
    elif  direction == "counter-clockwise":
        x = 1
        y = -1
        seconds = seconds = float(input("For long do you want me to go {number of seconds}"))
        robot.motors(x, y, seconds)
    else:
        move()

def move():
    direction = str(input("Do you want me to move forward or backward?"))
    seconds = float(input("For long do you want me to go {number of seconds}"))
    if direction == "forward":
        robot.motors(1,1,seconds)
    elif direction == "backward": 
        robot.motors(-1,-1,seconds)
    else:
        start()

def stay():
    robot.motors(0,0,5)
    print("Now I'm staying in the same place and I'm bored!")
    action = (input("Should I turn, dance, move, or stay?"))
    if action == "turn" or action == "Turn":
        turn()
    if action == "dance" or  action == "Dance":
        dance()
    if action == "move" or  action == "Move":
        move()
    if action == "stay" or  action == "Stay":
        print("I don't want to stay here :( I'm bored! Please pick something else for me to do.")
        start()
    else:
        "I can't do that! try again!"
        stay()


def dance():
    print("Lets dance!!!")
    for i in range(20):
        robot.motors(1,1,2)
        robot.motors(-1,-1,2)
        robot.motors(-1,1,5)
        robot.motors(1,-1,5)
        robot.motors(1,1,2)

def start(): 

    print("Hi! My name is RoboBunny!")
    action = input(f"What would you like me to do? The options are turn, move, dance, or stay.")
    if action ==  "turn" or action == "Turn":
            turn()
    elif action == "move" or action == "Move":
            move()
    elif action == "dance" or action == "Dance":
            dance()
    elif action == "stay" or action == "Stay":
            stay()
    else:
            print("Sorry! That is not a valid input. Please try again!")
            start()

    left, right = robot.sonars()
    print(left, right)

    if left <= 1 or right <= 1:
        robot.motors(0,0,1)
        todo = input("Oops! We hit a corner! Let's do something else. Options are turn, move, stay, or dance")
        if todo == "stay":
            stay()
        if todo == "turn":
            turn()
        if todo == "move":
            move()
        if todo == "dance":
            dance()



start()
robot.exit()

