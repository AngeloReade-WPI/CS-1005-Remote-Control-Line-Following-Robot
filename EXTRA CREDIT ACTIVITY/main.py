#This File Contains the main loop that manages the flow the Checkers and handlers
#
import checkers_and_handlers
ch = checkers_and_handlers
import input_prompting
ip = input_prompting
'''
This main function continually checks the state of 
the user_input variable. It has a large elif statement 
that checks the values with the valid commands for each 
iteration of the loop. When it detects that the input 
matches one of the valid keys by using the check_pressed
functions. It calls the appropriate handler to move in 
the correct way.

'''

def main_function():
    while True:
        user_input = ip.get_input()
        if ch.check_w_pressed(user_input):
            ch.handle_w_pressed()

        elif ch.check_a_pressed(user_input):
            ch.handle_a_pressed()

        elif ch.check_s_pressed(user_input):
            ch.handle_s_pressed()

        elif ch.check_d_pressed(user_input):
            ch.handle_d_pressed()

        elif ch.check_x_pressed(user_input):
            ch.handle_x_pressed()


main_function()
