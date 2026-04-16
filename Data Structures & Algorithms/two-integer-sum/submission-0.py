class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # every input has exactly one pair of indices i and j that satisfy the condition

        # return the answer with the smaller index first

        # ex 1
        # could do a double for loop. # ensure that the array is sorted first
        # iterating through each element in the nums array twice. Summing the elements. i!=j
        
        # actually we shouldn't sort it! because we want the original indices of the two

        for i, num_one in enumerate(nums):
            # how to iterate starting with the next element?
            if i == len(nums): # this means that we're at the end of the num array, meaning we haven't found any matching indices
                # we shouldn't actually reach here since we should have already/always found the indices i and j
                return []
            for j, num_two in enumerate(nums):
                if i == j:
                    # do nothing
                    pass
                else: 
                    two_sum = num_one + num_two
                    if two_sum == target:
                        return [i, j]


# Time complexity is O(n^2) because we are doing a double for loop
# Space complexity is 