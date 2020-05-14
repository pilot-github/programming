####################################################################################
## Given a non-empty array of integers, every element appears three times except 
## for one, which appears exactly once. Find that single one.
## Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
## 
## Example 1:
## Input: [2,2,3,2]
## Output: 3
####################################################################################

def my_singleNumber(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
            return nums[i]
