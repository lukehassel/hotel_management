__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

"""
This module contains functions which are called upon by the hotel_management project
"""


def get_duty_roster():
    """
    Reads the File Duty_Roster.txt and returns it.

    The function takes no arguments.

    The return is a string.
    """
    duty_roster = ""
    try:
        duty_roster = open("Duty_Roster.txt", "r+")
    except:
        pass
    duty_roster_rows = ""
    for row in duty_roster:
        duty_roster_rows += str(row)
    try:
        duty_roster.close()
    except:
        duty_roster_rows = "Duty_Roster.txt ist nicht lesbar. Es wurde vermutlich an einen anderen Pfad verschoben"
    return duty_roster_rows


def set_duty_roster(content):
    """
    Saves the inputfield of the plan administration page to Duty_Roster.txt.

    The function takes the content of the inputfield(string) as an argument.

    The function has no return.
    """
    # Opening the file with the parameter 'w' deletes all of its previous content
    duty_roster = open('Duty_Roster.txt', 'w')
    duty_roster.writelines(content)
    duty_roster.close()
