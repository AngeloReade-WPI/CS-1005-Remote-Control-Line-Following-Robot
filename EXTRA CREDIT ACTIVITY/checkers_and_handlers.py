#This File has the checkers and handlers that manage user inputted button presses
import sys
import input_prompting
import grid_driver
import line_tracker
ip = input_prompting
gd = grid_driver
lt = line_tracker


#####Checkers#####

"""
The checkers take the user_input as a parameter and 
uses "or" to see if the user input is either an uppercase 
or lowercase of the correct letter. If it is, they 
return true. if not, they return false.
"""
def check_w_pressed(user_input):
    if user_input == "w" or user_input =="W":
        return True
    else:
        return False
    
def check_a_pressed(user_input):
    if user_input == "a" or user_input =="A":
        return True
    else:
        return False
    
def check_s_pressed(user_input):
    if user_input == "s" or user_input =="S":
        return True
    else:
        return False
    
def check_d_pressed(user_input):
    if user_input == "d" or user_input =="D":
        return True
    else:
        return False
    
def check_x_pressed(user_input):
    if user_input == "x" or user_input =="X":
        return True
    else:
        return False


#####Handlers#####
'''The handlers are responsible for controlling the correct movement.
 W is mapped to forward, A is mapped to left turn, S is mapped to backward,
   D is mapped to right turn, and X is mapped to terminate program'''

def handle_w_pressed():
        gd.forward_one()
        print("robot has successfully moved forward")
        lt.stop()
        

def handle_a_pressed():
        gd.turn_left()
        print("robot has successfully turned left")
        lt.stop()
        

def handle_s_pressed():
        gd.back_one()
        print("robot has successfully moved backward")
        lt.stop()
        

def handle_d_pressed():
        gd.turn_right()
        print("robot has successfully turned rights")
        lt.stop()

def handle_x_pressed():
        print("Terminating program")
        sys.exit()






