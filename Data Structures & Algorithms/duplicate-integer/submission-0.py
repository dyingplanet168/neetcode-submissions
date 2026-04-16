class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Iterate through the nums list and put each element in a hashmap/dictionary
        # While you're putting in hashmap, you want to check if that element exists in the hashmap
        # If it exists, return true because that means we've already put that element in the hashmap (there's a duplicate)
        # Keep going and if we don't see a duplicate return false
        
        # Create a hashmap/dictionary
        nums_hashmap = {}
        for i in nums:
            if i in nums_hashmap:
                print(f"Duplicate found {i}")
                return True
            else:
                nums_hashmap[i] = 1
        return False
