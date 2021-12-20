"""Write a program whose input is two integers, and whose output is the first integer and
subsequent increments of 5 as long as the value is less than or equal to the second integer.
Ex. If the input is: -15 10 The output is: -15 -10 -5 0 5 10
Ex. If the second integer is less than the first. The output is: Second integer can't be less than the first.
"""

start = int(input())
end = int(input())
if start > end:
    print("Second integer can't be less than the first.")
else:
    while start <= end:
        print(start, end=' ') #<---- this one keeps getting new line errors when outputting
        start += 5
