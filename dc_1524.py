def first_missing_positive(nums):
    n = len(nums)

    j = 0
    for i in range(n):
        if nums[i] > 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    for i in range(j):
        val = abs(nums[i])
        if val - 1 < j and nums[val - 1] > 0:
            nums[val - 1] = -nums[val - 1]
    for i in range(j):
        if nums[i] > 0:
            return i + 1
    return j + 1

print(first_missing_positive([3, 4, -1, 1]))  # 2
print(first_missing_positive([1, 2, 0]))  # 3