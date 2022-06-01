#!/usr/bin/env python3
import logging as log
import math

def ship_speed():
    """Gives the ability to calculate speed, distance or time using those variables."""
    while True:
        # Speed = Distance / Time
        try:
            distance = float(input("Enter length in meters\nS >"))
            log.debug(f"Distance entered: {distance}")
            time = float(input("Enter time in seconds\nS >"))
            log.debug(f"Time entered: {time}")
            speed = float((distance / time) * 1.944)
            log.debug(f"Calculation done: {distance} / {time} * 1.944 = {speed}")
            print(f"Target speed is {round(speed, 5)} knots.")
            return speed
        except ValueError:
            log.error("ValueError with input!")
            print("Enter a number and try again.")
            break


def ship_range():
    """Gives the ability to calculate distance using height and centiradians."""
    while True:
        try:
            # Distance = Height / Centiradian
            height = float(input("Enter height\nR >"))
            log.debug(f"Height entered: {height}")
            centiradians = float(input("Enter centiradians\nR >"))
            log.debug(f"Centiradians entered: {centiradians}")
            distance = height / centiradians
            log.debug(f"Calculation entered: {height} / {centiradians} = {distance}")
            zoom = str(input("Is periscope zoomed? (Y / N)\nR >"))
            zoom.lower()
            if zoom == "y":
                distance = distance * 4
                log.debug(f"Periscope zoomed.")
            print(f"Target is {round(distance, 5)} hm away.")
            return distance
        except ValueError:
            log.error("ValueError with input!")
            print("Enter a number and try again.")
            break


def ship_targeting():
    """Calculates both speed and , and writes to a file."""
    # Combines both distance and speed calculations
    while True:
        try:
            target_name = str(input("Enter ship target name\nC >"))
            log.debug("Target name inputted.")
            target_speed = ship_speed()
            target_range = ship_range()
            target_info = open("Target Info.txt", "a")
            log.debug("File opened.")
            target_info.write(f"""SHIP NAME: {target_name}
SHIP SPEED: {target_speed}
SHIP RANGE: {target_range}
--------------------------
""")
            log.debug("File written.")
            target_info.close()
            log.debug("File closed.")
            print("Info saved to 'Target Info.txt'")
            break

        except ValueError:
            log.error("ValueError with input!")
            break
