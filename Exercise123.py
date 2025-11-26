# Find Minimum in Rotated Sorted Array in LeetCode
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0 
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        if left == right:
            return nums[left]
arr = [4,5,6,7,5,1,2]       
s = Solution()
print(s.findMin(arr))