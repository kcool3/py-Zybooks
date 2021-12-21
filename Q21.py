'''
The contents of the input1.csv are hello,cat,man,hey,dog,boy,Hello,man, cat,woman,dog,
Cat,hey,boy
Ex. If the input is:
input1.csv
the output is:
hello 1
cat2
man2
hey2
dog2
boy2
Hello1
woman1
Cat1
'''
import csv
input_file = input()
with open(input_file) as csv_file:
    data = csv.reader(csv_file, delimiter = ',')
    dictionary = {}
    for row in data:
        for string in row:
            if string in dictionary:
                dictionary[string] += 1
            else:
                dictionary[string] = 1

for key in dictionary:
    print(f"{key} {dictionary[key]}")
    
