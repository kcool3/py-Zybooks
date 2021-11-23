"""
Mad Libs are activities that have a person provide various words,
which are then used to complete a short story in unexpected( and funny ways).
Complete the program to read the needed values from input, that the existing
output statement(s) can use to output a short story. Ex. If the input is:
Eric Chipotle 12 cards The output is: Eric went to Chipotle to buy 12 different
types of cars
"""
#This will allow user to input anything.
first_name = input()
location = input()
whole_number = input()
plural_noun = input()
#This will print out the Mad Lib with user inputs.
print(first_name, 'went to', location, 'to buy', whole_number, 'different types of', plural_noun)
