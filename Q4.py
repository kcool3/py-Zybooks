"""Given a long integer representing a 10-digit phone number,
output the area code, prefix,
and line number using the format (800)555-1212. Ex. If the input is:
8005551212. Hint: Use % to get the desired rightmost digits."""
phone_num = int(input())
line_num = phone_num % 10000
phone_num //= 10000
prefix = phone_num % 1000
area_code = phone_num // 1000
#This will print out the entire phone number in the correct format.
com_phone_num = '(%s) %s-%s' % (area_code, prefix, line_num)
print(com_phone_num)

