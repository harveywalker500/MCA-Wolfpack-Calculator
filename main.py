import logging as log
import os


def logging_setup():
    """Sets up a logging system with variable degrees of logging. Allows looping in case of error.
Possible inputs: debug, info, warn, error, cancel"""
    while True:
        logging_level = str(input("Enter logging level\n> "))
        logging_level.lower()
        if logging_level == "debug":
            log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.DEBUG,
                            format="%(asctime)s %(message)s", datefmt="%I:%M:%S")
            log.debug("Debug mode set")
            break
        elif logging_level == "info":
            log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.INFO,
                            format="%(asctime)s %(message)s", datefmt="%I:%M:%S")
            break
        elif logging_level == "warn":
            log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.WARNING,
                            format="%(asctime)s %(message)s", datefmt="%I:%M:%S")
            break
        elif logging_level == "error":
            log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.ERROR,
                            format="%(asctime)s %(message)s", datefmt="%I:%M:%S")
            break
        elif logging_level == "cancel":
            break
        else:
            print("Not recognised, restarting.")
            log.info("logging_level input not recognised.")

    log.info("Logging created/changed successfully")
    print("Logging set.\nPress enter to continue.")
    input()


# Simple clear system for multiple OSes
def clear():
    """Clears the console. Should work for any OS."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def help_with_cmd(help_input):
    """If the user just types help, it provides a list of commands available. If they type 'help [command], it provides
the docstrings to the user, allowing them to learn what the commands mean."""
    console_input_list = help_input.split()
    if console_input_list[1] == "logging":
        print(logging_setup.__doc__)
    elif console_input_list[1] == "clear":
        print(clear.__doc__)
    elif console_input_list[1] == "quit":
        print("Exits the program.")
    elif console_input_list[1] == "help":
        print(help_with_cmd.__doc__)
    else:
        log.warn(f"help_with_cmd, INVALID INPUT: {console_input_list}")


# Main console
def console():
    log.debug("Console launched successfully")
    print("MCA Wolfpack Calculator")
    while True:
        console_input = str(input(">"))
        console_input.lower()
        if console_input == "logging":
            log.debug("Logging command given.")
            logging_setup()
        elif console_input == "quit":
            log.debug("Quit command given.")
            quit()
        elif console_input == "clear":
            log.debug("Clear command given.")
            clear()
        elif console_input.__contains__("help"):
            log.debug("Help command given.")
            if len(console_input.split()) > 1:
                help_with_cmd(console_input)
            else:
                print('''
Available commands:
logging
clear
quit
help
''')

        else:
            log.info(f"Nothing entered, rerunning: {console_input}")
            print("Invalid or empty command.")


def main():
    log.basicConfig(filename="LogFile.log", filemode="w", encoding="utf-8", level=log.INFO,
                    format="%(asctime)s %(message)s", datefmt="%I:%M:%S")
    console()


main()
