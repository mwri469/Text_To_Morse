"""
Functions for morse_led.py
"""

# Imports
import time
import RPi.GPIO as gpio

# Set up GPIO board
gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.OUT)
gpio.setwarnings(False)

# Print out a dot/dash in morse on request thru gpio circuit
def dot():
    """ Print a dot thru led """
    print(".")
    gpio.output(4, True)
    time.sleep(0.5)
    gpio.output(4, False)
    time.sleep(0.5)

def dash():
    """ Print a dash thru led """
    print("_")
    gpio.output(4, True)
    time.sleep(1.5)
    gpio.output(4, False)
    time.sleep(0.5)
    
# Letters/numbers to print
def A():
    dot()
    dash()

def B():
    dash()
    for i in range(3):
        dot()

def C():
    for i in range(2):
        dash()
        dot()

def D():
    dash()
    dot()
    dot()

def E():
    dot()

def F():
    dot()
    dot()
    dash()
    dot()

def G():
    dash()
    dash()
    dot()

def H():
    for i in range(4):
        dot()

def I():
    dot()
    dot()

def J():
    dot()
    for i in range(3):
        dash()

def K():
    dash()
    dot()
    dash()

def L():
    dot()
    dash()
    dot()
    dot()

def M():
    dash()
    dash()

def N():
    dash()
    dot()

def O():
    for i in range(3):
        dash()

def P():
    dot()
    dash()
    dash()
    dot()

def Q():
    dash()
    dash()
    dot()
    dash()

def R():
    dot()
    dash()
    dot()

def S():
    dot()
    dot()
    dot()

def T():
    dash()

def U():
    dot()
    dot()
    dash()

def V():
    for i in range(3):
        dot()

    dash()

def W():
    dot()
    dash()
    dash()

def X():
    dash()
    dot()
    dot()
    dash()

def Y():
    dash()
    dot()
    dash()
    dash()

def Z():
    dash()
    dash()
    dot()
    dot()

def Zero():
    for i in range(5):
        dash()

def One():
    dot()
    for i in range(4):
        dash()

def Two():
    dot()
    dot()
    for i in range(3):
        dash()

def Three():
    dot()
    dot()
    dot()
    dash()
    dash()

def Four():
    for i in range(4):
        dot()

    dash()

def Five():
    for i in range(5):
        dot()

def Six():
    dash()
    for i in range(4):
        dot()

def Seven():
    dash()
    dash()
    dot()
    dot()
    dot()

def Eight():
    dash()
    dash()
    dash()
    dot()
    dot()

def Nine():
    for i in range(4):
        dash()

    dot()

# Make a dictionary to make functions callable
letter_funs = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G":G,
               "H": H, "I": I, "J": J, "K": K, "L": L, "M": M, "N": N,
               "O": O, "P": P, "Q": Q, "R": R, "S": S, "T": T, "U": U,
               "V": V, "W": W, "X": X, "Y": Y, "Z": Z, "0": Zero,
               '1': One, '2': Two, '3': Three, '4': Four, '5': Five,
               '6': Six, '7': Seven, '8': Eight, '9': Nine
               }
