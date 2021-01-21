"""
100 days of Python course
DAY 8
"""

# the math module is needed for the .ceil function
import math

# user defined function: all the work gets done here
# and saves extra lines of code!

# Spyder created the docstring after the function was written
def paint_calc(height, width, cover):
    """
    Parameters
    ----------
    height : TYPE
        DESCRIPTION.
    width : TYPE
        DESCRIPTION.
    cover : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

# coverage is set here and the input is used in paing_calc function
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
