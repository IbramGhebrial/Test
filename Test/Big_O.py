def search_algo(num, items):
    for item in items:
        if item == num:
            return True
        else:
            pass
nums = [2, 4, 6, 8, 10]

print(search_algo(2, nums))
