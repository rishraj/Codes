def nextPermutation(nums: list[int]) -> None:
    # just a freaking pattern to memorize (next perm is going to be the next
    # greater no. formed using the elements of the list)
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i-1]:
            tmp_index = i
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i-1]:
                    tmp_index = j
                    break
            nums[i-1], nums[tmp_index] = nums[tmp_index], nums[i-1]
            nums[i:] = nums[i:][::-1]
            #print(nums)
            return
    nums.reverse()
    #print(nums)
    return
    


nums = [1, 3, 2]
nextPermutation(nums)
