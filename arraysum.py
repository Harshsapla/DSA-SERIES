# # # # # # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# # # # # # You may assume that each input would have exactly one solution, and you may not use the same element twice.

# # # # # # You can return the answer in any order.
# # # # # from typing import List

# # # # # class Solution:
# # # # #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# # # # #         dic = {}
# # # # #         for i, num in enumerate(nums):
# # # # #             complement = target - num
# # # # #             if complement in dic:
# # # # #                 return [dic[complement], i]
# # # # #             dic[num] = i

# # # # # # Example usage
# # # # # solution = Solution()
# # # # # nums = [2, 7, 11, 15]
# # # # # target = 9
# # # # # print(solution.twoSum(nums, target))
# # # # # # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# # # # # # Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# # # # # # Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# # # # # # Return k.
# # # # class Solution:
# # # #     def removeDuplicate(self, nums):
# # # #         if not nums:
# # # #             return 0
# # # #         k = 1
# # # #         for i in range(1, len(nums)):
# # # #             if nums[i] != nums[k - 1]:  # Compare with nums[k-1], not nums[k]
# # # #                 nums[k] = nums[i]      # Place the new unique element at nums[k]
# # # #                 k += 1                 # Increment k
# # # #         return k

# # # # # Instantiate the Solution class
# # # # solution = Solution()
# # # # nums = [2, 2, 11]
# # # # result = solution.removeDuplicate(nums)
# # # # print(result)       # Prints the number of unique elements
# # # # print(nums[:result])  # Prints the array with unique elementsSS
# # # # Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# # # # Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# # # # Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# # # # # Return k
# # # class Solution:
# # #     def removeElement(self, nums: List[int], val: int) -> int:
# # #         if not nums:
# # #             return 0
# # #         k =0
       
# # #         for i in range(0, len(nums)):
# # #             if nums[i]!= val:
# # #                nums[k] = nums[i]
# # #                k+=1
# # #         return k
# # Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# # You must write an algorithm with O(log n) runtime complexity
# # class Solution:
# #     def searchInsert(self, nums: List[int], target: int) -> int:
# #         if not nums:
# #             return 0
        
# #         for i in range( len(nums)):
# #             if nums[i] >= target:
# #                return i
               
# #         return len(nums),
# # this is for the plus one problem  
# class Solution:
#     def plusone(self,digits) :
#         n=len(digits)
#         for i in range(n-1 , -1 , -1):
#             if digits[i]<9:
#                 digits[i]+=1
#                 return digits
#             else :
#                 digits[i]=0
#         return [1]+digits
# solution = Solution()
# digits = [1,2]       
# result = solution.plusone(digits)
# print(result)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # Helper function to convert array to BST
        if not nums:
            return None
        
        # Find the middle element
        mid = len(nums) // 2
        root = TreeNode(nums[mid])  # The middle element becomes the root
        
        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])  # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Right half
        
        return root

# Helper function to print the BST (in-order traversal)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Example usage
solution = Solution()

# Example 1
nums1 = [-10, -3, 0, 5, 9]
root1 = solution.sortedArrayToBST(nums1)
print("In-order traversal of BST from nums1:")
inorder_traversal(root1)  # Output will be sorted order

print("\n")

# Example 2
nums2 = [1, 3]
root2 = solution.sortedArrayToBST(nums2)
print("In-order traversal of BST from nums2:")
inorder_traversal(root2)  # Output will be sorted order
                      

        