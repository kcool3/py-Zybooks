input_numbers = list(map(int, input().split()))
input_range = list(map(int, input().split()))

for number in input_numbers:
    if input_range[0] <= number <= input_range[1]:
        print('{}'.format(number), end=' ')