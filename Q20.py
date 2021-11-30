'''
Write a program that reads a text file containing synonyms for a word and outputs synonyms that
bgin with a specified letter.
Use the attached file educate.txt to help you write and test your program. This file contains synonyms for the word
"educate" listed in alphabetical order, with each row containing synonyms sharing the same first letter, separated by a
space. The contents of educate.txt are as follows:

educate.txt--------------
brainwash brief
civilize coach cultivate
develop discipline drill
edify enlighten exercise explain
foster
improve indoctinate inform instruct
mature
nurture
rear
school
train tutor
---------------------------

Your program should read input from the user in the format of a word, a line break, and a letter.
The program should open a text file associated with the input word.
The program should then store the contents of the text file into a dictionary, predefined in the program,
Finally the program should search the dictionary and outputs all the synonyms that begin with the input letter,
one synonym per line, or a message if no synonyms that begin with the output letter are found.
Hint: use the first letter of a synonym as the key when storing the synonym into the dictionary. Assume all
letters are in lowercase.

For example, if the input of the program is:
educate
c
the program opens the file educate.txt, then produces the following output:
civilize
coach
cultivate
'''
synonyms = {} # this is the dictionary to store synonyms
word = input() # user inputs word that contains the file name.
with open(word + ".txt", "r") as myFile:
    lines = myFile.readlines() # read each index as it stores the data of each line
    
for data in lines:
        data.strip()
        synonyms[data[0][0]] = data.split("")

myFile.close()

letter = input()
if letter not in synonyms.keys():
    print("No synonyms for", word, "begin with", letter + ".")
else:
    for ele in synonyms[letter]:
        print(ele)
        
    
    
        
