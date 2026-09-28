class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        j = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[j]:
                return True
            else:
                j+=1
        return False