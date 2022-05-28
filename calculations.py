#!/usr/bin/env python3
import logging as log


def ship_speed():
    """Gives the ability to calculate speed, distance or time using those variables."""
    while True:
        # Speed = Distance / Time
        try:
            distance = float(input("Enter distance in meters\n>"))
        except ValueError:
            log.error("ValueError.")
            print("Enter a number and try again.")
            break
        try:
            time = float(input("Enter time in seconds\n>"))
        except ValueError:
            log.error("ValueError.")
            print("Enter a number and try again.")
            break
        break
    speed = float((distance / time) * 1.944)
    print(f"Target speed is {round(speed, 5)} knots.")
    return speed


def ship_distance():
    """Gives the ability to calculate distance using height and centiradians."""
    # Distance = Height / Centiradian
    height = float(input("Enter height\n>"))
    centiradians = float(input("Enter centiradians\n>"))
    distance = height / centiradians
# ------------------------------------------------------------------------------
    zoom = str(input("Is periscope zoomed? (Y / N)\n>"))
    zoom.lower()
    if zoom == "y":
        distance = distance * 4
    distance = distance / 100
    print(f"Target is {round(distance, 5)} hectometers away.")
    return distance


def ship_targeting():
    """Calculates both speed and time."""
    # Combines both distance and speed calculations
    ship_speed()
    ship_distance()
