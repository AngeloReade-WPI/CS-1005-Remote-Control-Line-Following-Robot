# grid_driving.py
# 
# Version 1.1
#
# This module provides basic movement functions for a grid-based navigation system.
#

#
# TODO - Enable by uncommenting (when not unit testing) to test main on your XRP.
# After unit tests pass, import your line tracker and test the main code on your XRP.
import line_tracker

# TODO
# Review and test your prior activity functions you completed.
# Test them independently for physical reliability outside of additional complexity.
#   line_tracker.track_forward_to_grid_turn_point()
#   line_tracker.turn_left_grid()
#   line_tracker.turn_right_grid()
# These grid driving functions are built upon for the next level of grid navigation.
#
# After your unit testing, import your line_tracker to continue
# 

current_action_list = []  # The current list of actions to iterate through.

""" You don't need to modify this function. """
def forward_one():
    """
    Move forward one grid space to the next turn point and stop.
    Parameters:
        None
    Returns:
        None
    """
    line_tracker.track_forward_to_grid_turn_point() # type: ignore

""" You don't need to modify this function. """
def turn_left():
    """
    Turn left while at a turn point until finding new line, and stop.
    Parameters:
        None
    Returns:
        None
    """
    line_tracker.turn_left_grid() # type: ignore

""" You don't need to modify this function. """
def turn_right():
    """
    Turn right while at a turn point until finding new line, and stop.
    Parameters:
        None
    Returns:
        None
    """
    line_tracker.turn_right_grid() # type: ignore

""" You don't need to modify this function. """
def back_one():
    """
    Move backward one grid space to the previous turn point and stop, facing the original direction.
    Parameters:
        None
    Returns:
        None
    """
    turn_left()
    turn_left()
    forward_one()
    turn_right()
    turn_right()

# TODO - Implement the following function.
def get_valid_action_list():
    """
    Get the list of valid grid driving actions.
    The valid actions are "FORWARD", "LEFT", "RIGHT", and "BACKWARD".
    Use one line of code to define and return the list of valid actions.
    Parameters:
        None
    Returns:
        list: A list of valid action strings.
    """
    return [] # TODO - Implement this function

# TODO - Implement the following function.
def is_valid_action(action):
    """
    Check if the given action is a valid grid driving action.
    Use get_valid_action_list() to get the list of valid actions and check if the given
    action is in that list. 
    
    Note: Extra credit point: implement function body in exactly one line of code.
    
    Parameters:
        action (str): An action string to check.
    Returns:
        bool: True if the action is valid, False otherwise.
    """
    return None # TODO - Implement this function 

# TODO - Implement the following function.
def remove_invalid_actions(unfiltered_action_list):
    """
    Remove invalid actions from the given list of actions.
    Use is_valid_action() to check each action in the given list.
    Parameters:
        unfiltered_action_list (list): A list of action strings. Valid actions are defined by is_valid_action().
    Returns:
        list: A new list containing only valid action strings.
    """
    return None # TODO - Implement this function

# TODO - Implement the following function.
def get_next_action():
    """
    Get the next action from the current action list.
    If the current action list is empty, return None.
    Otherwise, remove and return the first action from the list.
    Parameters:
        None
    Returns:
        str or None: The next action string, or None if the list is empty.
    """
    global current_action_list # leave this line of code, this is the current action list to modify

    return None # TODO - Implement this function

""" You don't need to modify this function. """
def set_current_action_list(action_list):
    """
    Set the current action list. Assumes action_list has already been filtered.
    Parameters:
        action_list (list): A list of valid action strings. Valid actions are defined by is_valid_action().
    Returns:
        None
    """
    global current_action_list
    current_action_list = action_list
    print(f"Setting current action list to: {current_action_list}")

""" You don't need to modify this function. """
def get_current_action_list():
    """
    Get the current action list.
    Parameters:
        None
    Returns:
        list: The current list of action strings.
    """
    global current_action_list
    return current_action_list

""" You don't need to modify this function. """
def drive_action(item):
    """
    Drive a single grid driving action by calling the appropriate movement function.
    Parameters:
        item (str): A valid action string. Valid actions are defined by is_valid_action().
    Returns:
        None
    """
    print(f"Executing action: {item}")
    if item == "FORWARD":
        forward_one()
    elif item == "LEFT":
        turn_left()
    elif item == "RIGHT":
        turn_right()
    elif item == "BACKWARD":
        back_one()
    print(f"Finished executing action: {item}")

""" You don't need to modify this function. """
def drive_action_list(action_list):
    """
    Drive a list of grid driving actions in sequence by calling drive_action() for each action.
    Parameters:
        action_list (list): A list of valid action strings. Valid actions are defined by is_valid_action().
    Returns:
        None
    """
    for item in action_list:
        drive_action(item)