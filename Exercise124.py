# Algoritm Sort Colors in leetcode 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        for i in range(ln):
            min = i
            for j in range(i + 1, ln):
                if nums[j] < nums[min]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
            
        return nums