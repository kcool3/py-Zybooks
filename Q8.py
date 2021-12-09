"""Complete main() to read dates from input, one date per line. Each date's format
must be as follows: March 1, 1990. Any date not following that format is incorrect and
should beignored. Use the substring() method to parse the string and extract the date.
The input ends with -1 on a line alone. Output each correct date as: 3/1/1990.
Ex. if input is: March 1, 1990  April 2, 1995  7/15/20  December 13, 2003  -1
The output is: 3/1/1990  12/13/2003"""
def get_month_as_int(month_str):
    if month_str == 'January':
        month_int = 1
    elif month_str == 'February':
        month_int = 2
    elif month_str == 'March':
        month_int = 3
    elif month_str == 'April':
        month_int = 4
    elif month_str == 'May':
        month_int = 5
    elif month_str == 'June':
        month_int = 6
    elif month_str == 'July':
        month_int = 7
    elif month_str == 'August':
        month_int = 8
    elif month_str == 'September':
        month_int = 9
    elif month_str == 'October':
        month_int = 10
    elif month_str == 'November':
        month_int = 11
    elif month_str == 'December':
        month_int = 12
    else:
        month_int = 0
    return month_int

def main():
    user_str = []
    status = True
    while(status == True):
        user_str.append(input())
        if (user_str[-1] == '-1'):
            status = False
    print('\n')
    for strings in user_str:
        if(',' in strings):
            month_str = strings.split(',')[0].split()[0]
            month_int = str(get_month_as_int(month_str))
            date = strings.split(',')[0].split()[1]
            year = strings[-5:]
            final_date = month_int + '/' + date + '/' + year
            print(final_date)
        else:
            pass
main()
        
        
