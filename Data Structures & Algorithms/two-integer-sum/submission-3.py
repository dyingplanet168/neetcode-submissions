class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmaps. How
        # numbers larger than the target are cancelled
        nums_hashmap = {}
        for index, num in enumerate(nums):
            # find the difference number
            difference = target - num
            # check if that difference exists in the hashmap or if we have to keep iterating
            # does difference exist in hashmap
            if nums_hashmap.get(difference):
                return [nums_hashmap.get(difference)[0], index]
            # add the number to the hashmap with the value of its smallest index
            # if the number already exists in the hashmap make it an array of indices
            if num not in nums_hashmap:
                nums_hashmap[num] = [index]
            else:
                nums_hashmap[num] = nums_hashmap[num].add(index)  # how to add onto array?
