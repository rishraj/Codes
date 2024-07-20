def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 2 pass hashmap soln.
    """ d = {}
    for i in range(len(nums)):
        if nums[i] not in d: d[nums[i]] = [i]
        else: d[nums[i]].append(i)
    for i in range(len(nums)):
        if target - nums[i] in d and len(d[target - nums[i]]) > 1:
            return [i, d[target - nums[i]][1]]
        elif target - nums[i] in d and target - nums[i] != nums[i]:
            return [i, d[target - nums[i]][0]] """
            
    # 1 pass hashmap soln.
    # pair will always be found once 1st element gets added to the dict, also solves duplicate no. issue
    d = {}
    for i, n in enumerate(nums):
        if target - n in d: return [d[target - n], i]
        d[n] = i