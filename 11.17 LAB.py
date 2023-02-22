#11.17 LAB: Filter and sort a list
nums = input()
list = nums.split()
new_list = []
for i in list:
    if int(i) >= 0:
        new_list.append(int(i)) 
new_list.sort() 
for x in new_list:
    print(x, end=' ') 