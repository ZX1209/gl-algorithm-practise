def setlist(nums):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    l = len(nums)

    i = l - 1
    while i >= 0:
        if nums[i-1] == nums[i]:
            nums.pop(i-1)
            i = i - 1

        i -= 1

    return len(nums)
