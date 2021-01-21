"""
100 days of Python course
DAY 8
"""

# user defined function using the modulo for comparison
def prime_checker(number):
    """
    Parameters
    ----------
    number : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# this input gets passed into the function where the
# number is checked
n = int(input("Check this number: "))
prime_checker(number=n)
