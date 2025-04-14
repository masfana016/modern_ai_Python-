# 26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Given a sorted array nums, remove the duplicates in-place such that each element
        appears only once and returns the new length.
        
        The first k elements of nums should contain the unique elements in sorted order.
        """
        # Edge case: if array is empty
        if not nums:
            return 0
            
        # Initialize write pointer
        write_pos = 1
        
        # Iterate through array starting from second element
        for i in range(1, len(nums)):
            # If current number is different from previous
            if nums[i] != nums[i-1]:
                # Write it to the write_pos position
                nums[write_pos] = nums[i]
                write_pos += 1
                
        return write_pos
    
nums = [0,0,1,1,1,2,2,3,3,4]
        