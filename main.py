import logging as log
import math


def logging_setup():
    while True:
        logging_level = str(input("Enter logging level\n> "))
        logging_level.lower()
        if logging_level == "debug":
            log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.DEBUG,
                           format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S")
            log.debug("Debug mode set")
            break
        if logging_level == "info":
            log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.INFO,
                           format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S")
            break
        if logging_level == "warn":
            log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.WARNING,
                           format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S")
            break
        if logging_level == "error":
            log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.ERROR,
                           format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S")
            break
        else:
            print("Not recognised, restarting.")
            log.info("logging_level input not recognised.")

    log.info("Logging created/changed successfully")
    print("Logging set.")
    input()


def console():
    log.debug("Console launched successfully")
    print("MCA Wolfpack Calculator")
    while True:
        console_input = str(input(">"))
        console_input.lower()
        if console_input == "logging":
            logging_setup()
        else:
            log.info("Nothing entered, rerunning console")


def main():
    logging_setup()
    console()


main()
