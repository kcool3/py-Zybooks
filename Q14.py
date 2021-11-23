"""
The Fibonacci sequence begins with 0 and 1,
with all subsequent terms formed as the sum of the previous two values. For
example, the first terms of the Fibonacci sequence are 0,1,1,2,3,5,8,13...
Complete the fibonacci() method, which has an index, n, as parameter and returns
the nth term in the sequence. Any negative index values should return -1.
Ex. If the input is: 7 The output is: fibonacci(7) is 13
Note: Use a for loop abd DO NOT use recursion.
"""

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    index = int(input())
    print("fibonacci("+str(index)+") is "+str(fibonacci(index)))
    
    
    
    
    
    
