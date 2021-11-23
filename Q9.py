"""
A pedometer treats walking 2,000 steps as walking 1 miles. Write a steps_to_miles() function that takes the number
of steps as a parameter and returns the miles walked. The steps_to_miles() functions throws a ValueError object with
the message of:
"Exception: Negative step count entered." when the number of steps is negative. Complete the main() program that reads
the number of steps from a user, call the steps_to_miles() function, and outputs
the returned value from the steps_to_miles() function. Use a try-except block to catch
any ValueError object thrown by the steps_to_miles() function and output the exception message.
Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:,2f}')
Ex. if the input is: 5345 The output is: 2.67
if the input is: -3850 The output is: Exception: Negative step count entered.
"""

#my code below(be careful with indentation!)
#define method below
def steps_to_miles(steps):
  return steps / 2000
if __name__ == '__main__':
    steps = float(input())
# my code below
    if steps < 0:
       print("Exception: Negative step count entered.")
    else:
        print('{:.2f}'.format(steps_to_miles(steps)))

    
