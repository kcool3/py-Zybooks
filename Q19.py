'''
If the input of your program is:
10
0
the output of the program is:
Zero Division Exception: integer division or modulo by zero
'''

try:
    user_num = int(input())
    div_num = int(input())
    quotient = user_num//div_num
    print(quotient)

except ZeroDivisionError as zero:
   print("Zero Division Exception:", zero)

except ValueError as Val:
   print("Input Exception:",Val)

    
