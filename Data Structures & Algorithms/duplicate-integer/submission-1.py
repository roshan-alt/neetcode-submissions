class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictNum = {}
        for num in nums:
            if num in dictNum:
                dictNum[num]+=1
            else:
                dictNum[num] = 1
        
        for num in dictNum.values():
            if num > 1:
                # print(True)
                return True
        return False
        