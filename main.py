from microbit import *

# Pins used to control the motors
# Assuming P0 and P1 are connected to the motor driver's input pins
# If your motor driver has additional enable pins, make sure they are connected and set high
LEFT_MOTOR = pin0  # Left motor control pin
RIGHT_MOTOR = pin1  # Right motor control pin

# Function to move the car forward
def move_forward():
    LEFT_MOTOR.write_digital(1)   # Turn on the left motor
    RIGHT_MOTOR.write_digital(1)  # Turn on the right motor

# Function to stop the car
def stop():
    LEFT_MOTOR.write_digital(0)  # Turn off the left motor
    RIGHT_MOTOR.write_digital(0)
