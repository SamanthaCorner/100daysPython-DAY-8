# Area Calc

You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

* number of cans = (wall height x wall width) ÷ coverage per can.

	e.g. Height = 2, Width = 4, Coverage = 5

	number of cans = (2 x 4) ÷ 5 = 1.6
                     = 1.6

* Because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# Prime Number

A Prime number can only be cleanly divided by itself and 1. For more information: https://en.wikipedia.org/wiki/Prime_number

This program checks whether or not a number is prime:

* 2 is a prime number because it's only divisible by 1 and 2.

* 4 is not a prime number because you can divide it by 1, 2 or 4.

# Caesar cipher

* In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

* Deciphering is done in reverse, with a right shift of 3.

This program was developed in steps by breaking it down in small TODO tasks which were identified in the flow chart.

* The user chooses whether to encrypt or decrypt and the cipher key is entered. The program will run again if the user wants to en/decrypt something else.

* The module art.py is in this repository - ASCII art needed for the program to run.