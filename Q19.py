'''
If the input of your program is:
10
0
the output of the program is:
Zero Division Exception: integer division or modulo by zero
'''

try:
    user_num=int(input())
    div_num=int(input())
    print(' {}'.format(user_num/div_num))

except ZeroDivisionError:
    print("Zero Division Exception: integer division or modulo by zero")

except ValueError:
    print("Input Exception: invalid literal for int() with base 10: '15.5'")

    
