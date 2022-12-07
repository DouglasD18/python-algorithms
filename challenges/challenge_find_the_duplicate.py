def iteration(nums):
    duplicates = []
    nums.sort()
    for i, num in enumerate(nums):
        numeric = type(num)
        if numeric != int or num < 1:
            return False
        if i < len(nums) - 1 and num == nums[i + 1]:
            duplicates.append(num)
    return duplicates


def find_duplicate(nums):
    if len(nums) < 2:
        return False
    duplicates = iteration(nums)
    if type(duplicates) != list or len(duplicates) < 1:
        return False
    auxiliar = duplicates[0]
    for num in duplicates:
        if num != auxiliar:
            return False
    return auxiliar


if __name__ == '__main__':
    result = find_duplicate([1, 3, 4, 2, 2])
    print(result)
