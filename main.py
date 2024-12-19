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

# import tkinter as tk

# window = tk.Tk()
# window.geometry("300x200")
# label = tk.Label(window, text = "Centered Label")
# label.place(relx=0.5), rely=0.5, anchor=tk.CENTER
# window.mainloop()
# arr = np.array


# degree = 0.00
# x = 0
# y = 0
# seconds = 0


def turn(seconds):
    # global degree
    # global x
    # global y
    turn_clock = str(input("Do you want me to turn clockwise or counter-clockwise?"))
    if turn_clock == "clockwise":
        x = -1
        y = 1
        # degree = float(degree - (seconds/58.8%360))
        robot.motors(x, y, seconds)
        ask_question = input(str("Do you want to do something else?(yes/no)"))
        if ask_question == "yes" or ask_question == "Yes":
            robot.motors(-x, -y, seconds)
            start()
        else:
            quit()
    elif  turn_clock == "counter-clockwise":
        x = 1
        y = -1
        # degree = degree + (seconds/58.8%360)
        robot.motors(x, y, seconds)
        # return degree != 0
        ask_question = input(str("Do you want to do something else?(yes/no)"))
        if ask_question == "yes" or ask_question == "Yes":
            robot.motors(-x, -y, seconds)
            start()
        else:
            quit()
    else:
        print("Sorry, that's not a valid input! Please try again.")
        turn()
   
    
def stay():
    # print(degree)
    # print(x)
    # print(y)
    # if  degree != 0:
    #     robot.motors(seconds * degree)
    robot.motors(0,0,5)
    print("Now I'm staying in the same place and I'm bored!")
    action = (input("Should I turn, dance, move, do something random, or stay?"))
    if action == "turn" or action == "Turn":
        seconds = input(("For long do you want me to go"))
        turn(seconds)
    elif action == "dance" or  action == "Dance":
        dance()
    elif action == "move" or  action == "Move":
        move()
    elif action == "random" or  action == "random":
        random_action()
    elif action == "stay" or  action == "Stay":
        print("I don't want to stay here :( I'm bored! Please pick something else for me to do.")
        start()
    else:
        "I can't do that! try again!"
        stay()

def random_action():
    import random
    list1 = [move, dance, stay, turn]
    your_choice = random.choice(list1)
    your_choice()
    
    
def dance():
    # if degree != 0:
    #     robot.motors(-x,-y,degree)
    print("Lets dance!!!")
    dancing = float(input("For long do you want me to go (number of seconds)"))
    while dancing > 0:
        robot.motors(1,1,1)
        dancing=dancing-1.5
        robot.motors(-1,1,1)
        dancing=dancing-1.5
        robot.motors(-1,-1,1)
        dancing=dancing-1.5
        robot.motors(-1,1,1)
        dancing=dancing-1.5
def main():
  print("Hi! My name is RoboBunny!")
  start()

def start():
    # global seconds
    # # print(x,y)
    # # print(degree)
    # print(seconds)
    # if degree < 0:
    #     robot.motors(-x,-y, seconds * degree)
    # robot.motors(-1,1, 5)
    action = input(f"What would you like me to do? The options are turn, move, dance, do something random, or stay.")
    left, right = robot.sonars()
    print(left, right)
    if action ==  "turn" or action == "Turn":
        seconds = float(input(("For long do you want me to go?")))
        turn(seconds)
    elif action == "move" or action == "Move":
        move()
    elif action == "random"  or action == "Random":
        random_action() 
    elif action == "dance" or action == "Dance":
        dance()
    elif action == "stay" or action == "Stay":
        stay()
    else:
            print("Sorry! That is not a valid input. Please try again!")
            start()
 

def sonar(left, right):
    left_distance, right_distance = robot.sonars()
    print(left_distance, right_distance)
    remainder = float(input("For long do you want me to go {number of seconds}"))
    while remainder >0.1:
        left_distance, right_distance = robot.sonars()
        robot.motors(left, right, 0.1)
        remainder=remainder-0.2
        if left_distance<100 and right_distance<100:
            robot.motors (0, 0, 1)
            print("Oh no! I don't want to crash! Try again by pressing 'Run' and playing the code again!")
            # I have been working on code to center the robot in order for it to be able to complete other actions after moving but the code is not done so I haven't included it in this rough draft. It will be ready for the final draft
            quit()
            return
    if left_distance<100 and right_distance<100:
        robot.motors (0, 0, 1)
        print("Oh no! I don't want to crash! Try again by pressing 'Run' and playing the code again!")
       # I have been working on code to center the robot in order for it to be able to complete other actions after moving but the code is not done so I haven't included it in this rough draft. It will be ready for the final draft
        quit()
        return

def move():
    direction = str(input("Do you want me to move forward or backward?"))
    if direction == "forward":
         go = sonar
         go(1,1)
    if direction == "backward":
         robot.motors(1,-1, 3.05)
         go = sonar
         go(1,1)(1,1)

# goes 58.8 per second

#          take value (spin_duration/58.8%360)
# 180 degrees = 3.06

main()


robot.exit()





