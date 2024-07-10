def firstMissingPositive(nums: list[int]) -> int:
    # O(n) time and O(n) space: store list in set and check if it contains (1-len(nums))
    """ s = set(nums)
    for i in range(1, len(nums)+1):
        if i not in s:
            return i
    return len(nums)+1 """
    
    # O(n) time and  O(1) space: using index of nums like a hash
    len_nums = len(nums)
    # convert -ve nos. to 0, since they're useless and interfere with below logic
    for i in range(len_nums):
        if nums[i] < 0:
            nums[i] = 0
    # convert index of elements of nums between 1 to len(nums) to a -ve no.
    for i in range(len_nums):
        val = abs(nums[i]) # to not skip checking any index (eg. edge case nums = [3,4,-1,1])
        if 1 <= val <= len_nums:
            if not nums[val - 1]:
                nums[val - 1] = float("-inf")
            elif nums[val - 1] > 0:
                nums[val - 1] = nums[val - 1] * -1
            
    # return the index of first +ve no. since it's not present
    for i in range(len_nums):
        if nums[i] >= 0:
            return i + 1
    
    return len_nums + 1
    
    
    
nums = [3,4,-1,1]

print(firstMissingPositive(nums))