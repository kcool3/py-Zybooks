""" A palindrome is a word or a phrase that is the same when read both forward and backward.
Examples are: "bob", "sees", or "never odd or even"(ignoring spaces). Write a program whose input is a word or a phrase, and that
outputs whether the input is a palindrome. Ex. If the input is: bob
The output is: bob is a palindrome."""

word = input()
reverseString = ""
for i in range(len(word)):
    if(word[i]!= ' '):
        reverseString = word[i] + reverseString
if (word == reverseString):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
    
    
