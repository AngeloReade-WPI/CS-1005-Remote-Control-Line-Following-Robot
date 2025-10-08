#This File contains the function that prompts user to input keyboard presses for robot control

'''By asking the user to enter W, A, S, D; and storing it 
in the user_input variable, it allows the other functions
 to easily access the value'''

def get_input():
    user_input = input("Please enter one of the following to control robot W, A, S, D: ")
    return user_input

