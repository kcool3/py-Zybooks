'''Complete the calc_average() method that has an integer list parameter and returns the average value of the elements in the array as a double.
Ex. If input array is:
1 2 3 4 5
then the returned average will be:
3.0'''

def calc_average(nums):
    return sum(nums) / len(nums) # this is only code that you need to enter for this question to get correct.
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))

    # this should return 3.0.
