"""
Complete the get_num_of_characters() method to return the number of characters
in the users input string. Note: Use of a for loop is recommended in this function.
In main(), call the get_num_of_characters() method and then output both the original
string and the returned results. Implement the output_without_whitespace() method,
 which outputs the strings characters except for whitespace (spaces, tabs).
 Call the output_without_whitespace() method in main().
 Note: A tab is \t.
 Ex. If the input is: The only thing we have to fear is fear itself.
 the output is:
 Enter a sentence or phrase:
 The only thing we have to fear is fear itself.
 You entered: The only thing we have to fear is fear itself.
 Number of characters: 46
 String with no whitespace: Theonlythingwehavetofearisfearitself.
 """
def get_num_of_characters(input_str):
    num_chars = 0
    for i in range(len(input_str)):
        num_chars += 1
    return num_chars

def output_without_whitespace(input_str):
    print('String with no whitespace: ', end ='')
    for letter in input_str:
        if letter != ' ' and letter != '\t':
            print(letter, end='')
    print()
if __name__ == '__main__':
    phrase = input('Enter a sentence or phrase:\n')
    print('\nYou entered: ' + phrase)
    print('\nNumber of characters: ' + str(get_num_of_characters(phrase)))
    output_without_whitespace(phrase)
