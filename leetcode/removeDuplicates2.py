def removeDuplicates1(self, nums: List[int]) -> int:
    i=2
    while i < len(nums):
        if len(nums) <3:
            break
        if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
            del nums[i]
            i -= 1
        i += 1
    return len(nums)
    
def removeDuplicates2(self, nums: List[int]) -> int:
    maxCount = 2
    runner = 0
    cacher = -1
    prototypePos = 0
    for runner in range(len(nums)):
        # Caching
        # new element? update prototypePos
        if nums[runner] != nums[prototypePos]:
            prototypePos = cacher + 1

        # Can we afford this dup?
        if nums[runner] == nums[prototypePos] and cacher - prototypePos >= maxCount - 1:
            continue

        # put in cache
        cacher = cacher + 1
        # nums[runner], nums[cacher] = nums[cacher], nums[runner]
        nums[cacher] = nums[runner]
    return cacher + 1
