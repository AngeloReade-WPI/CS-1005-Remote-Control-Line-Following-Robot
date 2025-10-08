# line_sensors.py
#
# This module provides functionality for line sensors in a robot control system.
# It includes initialization and placeholder functions for reading sensor values.
#
from XRPLib.reflectance import Reflectance as Reflectance

line_reflectance_threshold = 0.8 # Threshold for detecting line. Ajust as needed.

def get_error():
    """
    Get the error value from the line sensors.
    Returns:
        float: The error value indicating deviation from the line.
    """
    reflectance = Reflectance.get_default_reflectance()
    left_reflectance = reflectance.get_left()
    right_reflectance = reflectance.get_right()
    error = left_reflectance - right_reflectance
    return error

def left_on_line():
    """
    Check if the left line sensor is on the line.
    Returns:
        bool: True if the left sensor is on the line, False otherwise.
    """
    reflectance = Reflectance.get_default_reflectance() 
    return reflectance.get_left() > line_reflectance_threshold

def right_on_line():
    """
    Check if the right line sensor is on the line.
    Returns:
        bool: True if the right sensor is on the line, False otherwise.
    """
    reflectance = Reflectance.get_default_reflectance() 
    return reflectance.get_right() > line_reflectance_threshold

def both_on_line():
    """
    Check if both line sensors are on the line.
    Returns:
        bool: True if both sensors are on the line, False otherwise.
    """
    return left_on_line() and right_on_line()  

def report_values():
    """
    Log the current reflectance values from both line sensors.
    Returns:
        None
    """
    reflectance = Reflectance.get_default_reflectance()
    left_reflectance = reflectance.get_left()
    right_reflectance = reflectance.get_right()
    print(f"Left Reflectance: {left_reflectance}, Right Reflectance: {right_reflectance}")

# End of file.