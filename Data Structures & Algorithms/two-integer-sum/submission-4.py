class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}
        for index, num, in enumerate(nums):
            # check for difference
            difference = target - num
            # check if the hashmap has the difference
            if difference in nums_hashmap:
                return[nums_hashmap[difference], index]
            else:
                # add num to hashmap
                nums_hashmap[num] = index