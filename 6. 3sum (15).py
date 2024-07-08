class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # keeping a set to keep result list unique is slower (though same time complexity)
        
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if not total:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # if next element is the same, skip it to avoid adding it again
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total < 0:
                    l += 1
                    # no need to skip anything since these elements are anyways not added
                else:
                    r -= 1
        return res
    
n = int(input("Enter size of array: "))
print("Enter the array")
nums = []
for i in range(n):
    nums.append(int(input()))

print(Solution().threeSum(nums))