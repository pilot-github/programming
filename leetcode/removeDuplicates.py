######################################################################
## Given a sorted array nums, remove the duplicates in-place such that 
## each element appear only once and return the new length.
##
## Do not allocate extra space for another array, you must do this 
## by modifying the input array in-place with O(1) extra memory.
##
## Given nums = [1,1,2],
##
## Your function should return length = 2, with the first two elements 
## of nums being 1 and 2 respectively.
##
## It doesn't matter what you leave beyond the returned length.
##
######################################################################
def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

def my_removeDuplicates(nums):
    index = 1
    while index < len(nums):
        print(index, nums[index], nums[index-1])
        if nums[index] == nums[index-1]:
            del nums[index]
            index -= 1
        index += 1

    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
