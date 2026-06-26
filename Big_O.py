import random

n = 100
max_val = 100
data_list = [random.randint(1, max_val) for i in range(n)]
data_list.sort()
# print(data_list)
# print(len(data_list))
target = 50
lower_bound = 0
upper_bound = len(data_list) - 1
found = False

while not found and lower_bound <= upper_bound:
    mid_point = (lower_bound + upper_bound) // 2
    if data_list[mid_point] == target:
        print("You number has been found at position ", mid_point)
        found = True
    elif data_list[mid_point] < target:
        lower_bound = mid_point + 1
    else:
        upper_bound = mid_point - 1
if not found:
    print("Your number is not in the list.")
