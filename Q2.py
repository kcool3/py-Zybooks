"""Write a program whose inputs are three integers,
and whose output is the smallest of the three values.
Ex. If the input is: 7  15  3"""
# The expected output should be 3.
# This reads the three integers that are input by the user.
first = int(input())
second = int(input())
third = int(input())
#Now calculate the smallest number of the three values.
smallest = first
if second < smallest:
    smallest = second
if third < smallest:
    smallest = third
#Print the smallest number.
print(smallest)



