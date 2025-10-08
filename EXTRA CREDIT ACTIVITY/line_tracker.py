# line_tracker.py
#
# This module provides functionality for line tracking in a robot control system.
# It includes initialization and placeholder functions for line tracking.
#
import time
from XRPLib.differential_drive import DifferentialDrive as DifferentialDrive

import line_sensors

# Adjust these variables as needed for your robot and environment

# Post intersection turn point cm for XRP beta model size


# Speed variables for different movements. Maintain reliable values for low, medium, and high speeds here.
turn_speed_low = 0.35
turn_speed_med = 0.5
default_turn_speed = turn_speed_low  # Adjust as needed

track_speed_low = 0.3
track_speed_med = 0.5  
track_speed_high = 0.7  
track_speed_full = 1.0
default_track_speed = track_speed_med  # Adjust as needed

# Proportional control gain for line tracking, adjust as needed for your robot and environment
prop_control_gain = 0.9

# Set the drivetrain object variable once for use in all functions in this module.
drivetrain = DifferentialDrive.get_default_differential_drive()

def stop():
    """
    Stop the robot's movement.
    Parameters:
        None
    Returns:
        None
    """
    drivetrain.stop()

def at_intersection():
    """
    Check if both line sensors are on the line (intersection detected).
    Parameters:
        None
    Returns:
        bool: True if both sensors are on the line, False otherwise.
    """
    return line_sensors.both_on_line()

def stop_pause(sleep_ms=500):
    """
    Stop the robot and pause for a specified duration.
    This can be useful to observe separate sequential calls to movement functions.
    Parameters:
        sleep_ms (int): Time to pause in milliseconds. Default is 500 ms.
    Returns:
        None
    """
    drivetrain.stop()
    time.sleep_ms(sleep_ms)

def track_line_step(track_speed, step_ms=10): 
    """
    Step function called repeatedly to follow the line using proportional control.
    A small delay is included to allow time for the movement to update before the function returns.
    Parameters:
        track_speed (float): The forward speed for tracking the line.
    Returns:
        None
    """
    correction = line_sensors.get_error() * prop_control_gain
    drivetrain.arcade(track_speed, correction)

def turn_left_step(step_ms=10):
    """
    Step function called repeatedly to turn left.
    A small delay is included to allow time for the movement to update before the function returns.
    Parameters:
        None
    Returns:
        None
    """
    drivetrain.arcade(0, default_turn_speed)
    time.sleep(0.001) # Millisecond delay each step to update movement

def turn_right_step(step_ms=10):
    """
    Step function called repeatedly to turn right.
    A small delay is included to allow time for the movement to update before the function returns.
    Parameters:
        None
    Returns:
        None
    """
    drivetrain.arcade(0, -default_turn_speed)
    time.sleep(0.001) # Millisecond delay each step to update movement

#
# NOTE: Extra Credit Point: a "Refactoring Task" (quality improvement not required for basic functionality): 
# 
# Create a new similar funciton to those above, so you can delete the above two functions, reducing code.
# Think back to your generalized polygon drawing function from a previous module.
#
# What is the only real difference between the functions in the above 20+ lines of code? 
#
# Use a parameter in your new function to reduce code duplication.
# You can test it by replacing the calls to the above two functions with calls to your new generalized function.
# 
# Extra credit define your generalized turn step function here: 
# def track_turn_step(...

def track_forward_to_intersection():
    """
    Move the robot forward until both line sensors are on the line (at intersection).
    Assumes the robot is currently on the current line, but not yet at the intersection.
    Uses a while loop to call track_line_step() repeatedly until at intersection.
    Parameters:
        None
    Returns:
        None
    """
    while not at_intersection(): # While not at intersection
        track_line_step(track_speed_med) # Follow the current line one step
    stop()

def track_forward_past_intersection():
    """
    Move the robot forward a small amount more until past intersection.
    Assumes the robot is currently stopped over intersection, not on the current line.
    Uses a while loop to call drivetrain.arcade() repeatedly until off the intersection.
    Parameters:
        None
    Returns:
        None
    """
    while line_sensors.both_on_line(): # While at intersection
        drivetrain.arcade(track_speed_low, 0) # Move forward one step until off the intersection
    stop()

def track_forward_to_turn_point():
    """
    Move the robot forward one grid space, past the intersection point, to the point it is ready to turn.
    Assumes the robot is currently past an intersection, on the current line, but not yet at the turn point.
    Uses a for loop to call track_line_step() repeatedly a set number of times to reach the turn point.
    Parameters:
        None
    Returns:
        None
    """
    # NOTE Extra Credit Point: test the other track_speed variable values for reliably getting to turn point.
    # Add new variables for making different speeds work and add comments here. Should any speeds be avoided?

    # Iterate using steps to move to turning point after passing intersection
    forward_low_steps_ms = 300 # Rough constant for 90 degree amount of space needed (marker column over intersection)

    for __ in range(forward_low_steps_ms): # Adjust the range value as needed for your robot and environment
        track_line_step(track_speed_low) # Follow the line one step
        time.sleep(0.001) # Millisecond delay each step to update movement
    stop()


#
# The following (and above) helper functions are only used internally in this module.
# After completing them, the three public functions at the very bottom offer high level functionality.
#

# TODO - implement this function
def derail_left():
    """
    Move the robot left (counter-clockwise) off the current line fully, and stop.
    Parameters:
        None
    Returns:
        None
    """
    while line_sensors.right_on_line() == False:
        turn_left_step()
    stop()
    print("Hello")
    while line_sensors.right_on_line() == True:
        turn_left_step()
    


    # TODO Iterate with left step turns until a sensor finds current line. Think about which sensor it should be.
    # TODO Use a while loop. Call a line_sensors helper function for the boolean expression that controls the loop.

    # TODO Iterate (again) with left step turns until right sensor is off the current line. Think about which sensor it should be.
    # TODO Use a while loop. Call a line_sensors helper function in the boolean expression that controls the loop. 

    stop() # Stop movement now off left of the current line
 
# TODO - implement this function
def derail_right():
    """
    Move the robot right (clockwise) off the current line fully, and stop.
    Parameters:
        None
    Returns:
        None
    """
    while line_sensors.left_on_line() == False:
        turn_right_step()
    stop()
    
    while line_sensors.left_on_line() == True:
        turn_right_step()
    
    # TODO Iterate with step turns until a sensor finds current line. Think about which sensor it should be.
    # TODO Use a while loop. Call a line_sensors helper function for the boolean expression that controls the loop

    # TODO Iterate (again) with step turns until a sensor is off the current line. Think about which sensor it should be.
    # TODO Use a while loop. Call a line_sensors helper function for the boolean expression that controls the loop.

    stop() # Stop movement, now off right of the current line

def find_line_left():
    """
    Assumes the robot is currently derailed from a line.
    Turn left until the new line is found, and stop.
    Iterate and count how many steps it takes to find the line.
    Once the right sensor detects the new line, print the count to the console, and stop.
    Parameters:
        None
    Returns:
        None
    """
    # TODO add an iteration variable to count how many steps it takes to find the line.
    iteration_left = 0
    

    # TODO Iterate with step turns until one of the sensors finds current line. 
    #      Which sensor should detect the line?
    #      Use a while loop and control it by calling one of your a line_sensors helper function.
    #      Within the loop, increment the iteration variable during each loop iteration.
    while line_sensors.right_on_line() == False:
        turn_left_step()
        iteration_left += 1
    print(f'It took {iteration_left} iterations to find line left')

    # TODO Print the iteration variable to the console in a meaninful message, using an f-string. 

    stop() # Stop motors

def find_line_right():
    """
    Assumes the robot is currently derailed from a line.
    Turn right until the new line is found, and stop.
    Iterate and count how many steps it takes to find the line.
    Once the left sensor detects the new line, print the count to the console, and stop.
    Parameters:
        None
    Returns:
        None
    """
    # TODO add an iteration variable to count how many steps it takes to find the line.
    iteration_right = 0
    # TODO Iterate with step turns until one of the sensors finds current line.
    #      Which sensor should detect the line?
    #      Use a while loop and control it by calling one of your a line_sensors helper function.
    #      Within the loop, increment the iteration variable during each loop iteration.
    while line_sensors.left_on_line() == False:
        turn_right_step()
        iteration_right += 1
        print(f'It took {iteration_right} iterations to find line left')
    # TODO Print the iteration variable value to the console in a meaninful message, using an f-string.

    stop() # Stop motors

#
# These high level functions can be called from other modules. Details are handled internally inside this module.
# This creates modular design and organized functionality.
#
# After completing the above helper functions, these three public functions can be called from main.py.
# This is the "public interface" for this module, to offer high level functionality.
#

def track_forward_to_grid_turn_point():
    """
    Move the robot forward one grid space, past the intersection point, to the point it is ready to turn.
    Parameters:
        None
    Returns:
        None
    """
    track_forward_to_intersection() # Move forward until intersection
    print("found intersection")
    stop_pause() # Optional pause to check functionality
    track_forward_past_intersection() # Move forward a small amount more until past intersection
    print("driving past intersection")
    stop_pause() # Optional pause to check functionality
    track_forward_to_turn_point() # Move forward until turn point
    stop_pause() # Optional pause to check functionality


def turn_left_grid():
    """7
    Assumes the robot is currently stopped at at a turn point.
    Derail left off line, and turn until finding new line, and stop.
    Parameters:
        None
    Returns:
        None
    """
    derail_left()
    find_line_left()
    print("found left line")
    stop_pause()
    stop()

def turn_right_grid():
    """
    Assumes the robot is currently stopped at at a turn point.
    Derail right off line, and turn until finding new line, and stop.
    Parameters:
        None
    Returns:
        None
    """
    derail_right()
    find_line_right()
    stop_pause()
    stop()


