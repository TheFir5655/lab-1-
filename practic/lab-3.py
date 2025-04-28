nums = [1, 3, 1, 4, 1, 7, 1, 7, 1, 8, 5, 10]
print(nums)
def dubl(stuff):
    return len(stuff)!=len(set(stuff))

print(dubl(nums))