# Import the robot control commands from the library


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

from simulator import robot

import time
 
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
        print("Sorry, that's not a valid input! Please try again.")
        turn()
   
    
def stay():
    robot.motors(0,0,5)
    print("Now I'm staying in the same place and I'm bored!")
    action = (input("Should I turn, dance, move, or stay?"))
    if action == "turn" or action == "Turn":
        turn()
    elif action == "dance" or  action == "Dance":
        dance()
    elif action == "move" or  action == "Move":
        move()
    elif action == "stay" or  action == "Stay":
        print("I don't want to stay here :( I'm bored! Please pick something else for me to do.")
        start()
    else:
        "I can't do that! try again!"
        stay()

def dance():
    print("Lets dance!!!")
    dancing = float(input("For long do you want me to go (number of seconds)"))
    while dancing != 0:
        for i in range(4):
          robot.motors(1,1,1)
          robot.motors(-1,1,1.5139)
        for i in range(4):
             robot.motors(-1,1,1.5139)


       

def main():
  print("Hi! My name is RoboBunny!")
  start()

def start(): 
    action = input(f"What would you like me to do? The options are turn, move, dance, or stay.")
    left, right = robot.sonars()
    print(left, right)
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
def sonar(left, right):
    # forward_backward = str(input("Do you want me to move forward or backward?"))
    left_distance, right_distance = robot.sonars()
    print(left, right)
    remainder  = float(input("For long do you want me to go {number of seconds}"))
    while remainder >1:
        left_distance, right_distance= robot.sonars()
        robot.motors(left, right, 0.1)
        remainder=remainder-0.2
        if left_distance<100 and right_distance<100:
            robot.motors (0, 0, 1)
            print("Oh no! I don't want to crash into the wall, so please pick something else.")
            start()
    if left_distance<100 and right_distance<100:
            robot.motors (0, 0, 1)
            print("Oh no! I don't want to crash into the wall, so please pick something else.")
            start()
def move():
    direction = str(input("Do you want me to move forward or backward?"))
    if direction == "forward":
         sonar(1,1)
    if direction == "backward":
         robot.motors(1,-1, 3)
         sonar(1,1)
    

main()


robot.exit()

