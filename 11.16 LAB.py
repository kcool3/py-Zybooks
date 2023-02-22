#11.16 LAB: Varied amount of input data
user_input = input()

tokens = user_input.split()  # Split into separate strings

nums = []                    
for token in tokens:         # Convert strings to integers
    nums.append(int(token))

avg = sum(nums) / len(nums)  # Calculates average of all integers in nums
print(int(avg), max(nums))   # Prints avg as an Integer instead of a Float
