#merge sort algoritm in leetcode
from  typing import List
class Solution:
    # divid arraye to two part left and right with recursion func
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return self.merge(left,right)
    
    # sorted with merge algoritm
    def merge(self, left: List[int] , right: List[int]):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
nums = [5,2,3,1]
sol = Solution()
print(sol.sortArray(nums))
    