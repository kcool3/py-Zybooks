"""
Write a program that takes in a line of text as input, and outputs that line of
text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.
Ex. If input is: Hello there  Hey   done
The output is: ereht olleH yeH
"""

def reverse_txt(line):
    r_txt = line[::-1]
    #print the reversed text
    print(r_txt)
lines = []
#input line
l = input()
while not(l == "done" or l=="Done" or l=="d"):
    lines.append(l)
    #Input again
    l = input()
#call function for all lines
for s in lines:
    reverse_txt(s)
