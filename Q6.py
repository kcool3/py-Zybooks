"""Write a program with the total change amount in pennies as an integer input, and output the change
using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes,
Nickels, and Pennies. Use singular and plural coint names as appropriate, like 1 Penny vs. 2 Pennies.
Ex. If the input is: 0 The output is: No change.
If the input is: 45 the output is: 1 Quarter 2 Dimes"""

def main():
    input_val = int(input())
    if input_val <= 0:
        print('No change')
    else:
        Dollars = input_val // 100
        input_val %= 100
        Quarters = input_val // 25
        input_val %= 25
        Dimes = input_val //10
        input_val %= 10
        Nickels = input_val // 5
        input_val %= 5
        Pennies = input_val
        
    if Dollars > 1:
        print(' %d Dollars' % Dollars)
    elif Dollars == 1:
        print(' %d Dollar' % Dollars)
    
    if Quarters > 1:
        print(' %d Quarters' % Quarters)
    elif Quarters == 1:
        print(' %d Quarter' % Quarters)
    if Dimes > 1:
        print(' %d Dimes' % Dimes)
    elif Dimes == 1:
        print(' %d Dime' % Dimes)
    if Nickels > 1:
        print(' %d Nickels' % Nickels)
    elif Nickels == 1:
        print(' %d Nickel' % Nickels)
    if Pennies > 1:
        print(' %d Pennies' % Pennies)
    elif Pennies == 1:
        print(' %d Penny' % Pennies)
main()

        

