# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0

#         k = 1
#         for i in range(1, len(nums)):
#             print(i)
#             if nums[i] != nums[i - 1]:
#                 print(nums)
#                 nums[k] = nums[i]
#                 print(nums)
#                 k += 1

#         # overwrite remaining elements with '_' to match example output
#         for i in range(k, len(nums)):
#             nums[i] = '_'

#         return k

# # Example usage
# nums = [0,1,1,2,2,3]
# ob = Solution()
# k = ob.removeDuplicates(nums)

# print("Output:", k, ", nums =", nums)

