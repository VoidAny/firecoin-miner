#!/usr/bin/python3
import sys
import pynput
from time import sleep
import random

# These varibles are used to make sure I don't 
# sleep the same amount of time twice in a row
current_sleep: int = 60
last_sleep: int = 0

# This controls how long before any mining occurs, 
# so that you can get into the discord channel
inital_sleep: int = 20

# Ajust these to ajust time inbetween sleeps
min_time: int = 60
max_time: int = 60
assert min_time <= max_time

times_mined: int = 0

keyboard = pynput.keyboard.Controller()
Key = pynput.keyboard.Key

def enter() -> None:
    keyboard.press(Key.enter)
    sleep(0.04)
    keyboard.release(Key.enter)

def enter_slash_command() -> None:
    enter()
    sleep(0.3)
    enter()
    sleep(0.3)

def real_type(phrase: str) -> None:
    for char in phrase:
        keyboard.press(char)
        sleep(0.04)
        keyboard.release(char)
        sleep(0.1)


def mine():
    global times_mined, current_sleep
    sleep(inital_sleep)
    while True:
        real_type("/mine")
        enter_slash_command()
        times_mined += 1
        sleep(current_sleep)

def print_help() -> None:
    help_message = """
    Welcome to the Firecoin miner, v2
    
    This program was intended to be used to be run in a virtual machine. 
    It is recommend to do this because it allows you to still use your computer like normal while mining.

    If you ever need to exit, please type ctrl+c to exit.

    For more information, see README.md
    """
    print(help_message)
    sys.exit(0)

def main():
    """This is just a wraper for the mine function"""
    print("Welcome to the Firecoin miner, v2")
    print("\nTo learn more about how to use this program, please pass --help")
    print("To exit, please type ctrl+c into the console this is running in")
    try:
        mine()
    except KeyboardInterrupt:
        print(f"You mined {times_mined} times!")
        sys.exit(0)


if __name__ == "__main__":
    try:
        if sys.argv[1] in ("--help", "-h"): print_help()
    except:
        main()