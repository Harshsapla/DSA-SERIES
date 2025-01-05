# # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# # You may assume that each input would have exactly one solution, and you may not use the same element twice.

# # You can return the answer in any order.
# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dic = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in dic:
#                 return [dic[complement], i]
#             dic[num] = i

# # Example usage
# solution = Solution()
# nums = [2, 7, 11, 15]
# target = 9
# print(solution.twoSum(nums, target))
# # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# # Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# # Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# # Return k.
class Solution:
    def removeDuplicate(self, nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:  # Compare with nums[k-1], not nums[k]
                nums[k] = nums[i]      # Place the new unique element at nums[k]
                k += 1                 # Increment k
        return k

# Instantiate the Solution class
solution = Solution()
nums = [2, 2, 11]
result = solution.removeDuplicate(nums)
print(result)       # Prints the number of unique elements
print(nums[:result])  # Prints the array with unique elementsSS
