class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_dict = {}  # Dictionary to store values and their indices
        
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            
            # If the complement exists in the dictionary, return its index along with the current index
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Add the current number to the dictionary with its index
            num_dict[num] = i
        
        # If no solution is found, return an empty list or handle the error as per your requirement
        return []
