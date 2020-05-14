#########################################################################
## Given nums = [1,1,1,2,2,3],

## Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

## It doesn't matter what you leave beyond the returned length.
#########################################################################

def my_removeDuplicates(self, nums: List[int]) -> int:
    i=2
    while i < len(nums):
        if len(nums) <3:
            break
        if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
            del nums[i]
            i -= 1
        i += 1
    return len(nums)
    
def removeDuplicates(self, nums: List[int]) -> int:
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
