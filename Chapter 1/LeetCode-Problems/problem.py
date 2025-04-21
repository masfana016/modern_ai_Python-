# 26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: if array is empty
        if not nums:
            return 0
            
        # Initialize pointer for position to place next unique element
        k = 1
        
        # Iterate through array starting from second element
        for i in range(1, len(nums)):
            # If current element is different from previous element
            if nums[i] != nums[i-1]:
                # Place current element at position k
                nums[k] = nums[i]
                k += 1
                
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)
print(nums[:result])  # Print the modified array up to k elements


        