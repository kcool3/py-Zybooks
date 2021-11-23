"""Driving is expensive. Write a program with a car's miles/gallons and gas dollars/gallons(both doubles) as input,
and output the gas cost for 20 miles, 75 miles, and 500 miles.
Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f} {:.2f} {:.2f}' .format(dollars_20_miles, dollars_75_miles, dollars_500_miles))
Ex. If the input is: 20.00  3.1599
The output is: 3.16  11.85  79.00
Note: Real per-mile cost would also include maintenance and depreciation."""

miles_per_gallon = float(input())
dollars_per_gallon = float(input())
unit_cost = dollars_per_gallon / miles_per_gallon

dollars_20_miles = unit_cost * 20
dollars_75_miles = unit_cost * 75
dollars_500_miles = unit_cost * 500

print('{:.2f} {:.2f} {:.2f}' .format(dollars_20_miles, dollars_75_miles, dollars_500_miles))
