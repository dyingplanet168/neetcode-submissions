class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an integer array nums
        # given integer k
        # return the k most frequent elements within the array
        # hashmap baby
        # basically add every number you see to the hashmap and increment the frequency at which you see that number
        # okay but how do we get the k most frequent elements?
        # dicts aren't sorted. 
            # we can iterate through the dict and find the largest value in the dict?
            # largest = 0
            # for key, value in dict:
            #   
            #   if value > largest:
            #       return largest = value
            #       largest_index = key
        # can you sort a dict?
        # traversing dicts?

        # 1) create hashmap of num, freq from list of nums
        # 2) sort the num, freq hashmap in descending order by value
        # 3) return the first k keys in the hashmap

        num_freq_hashmap = {}
        for num in nums:
            num_freq_hashmap[num] = num_freq_hashmap.get(num, 0) + 1
        
        # how to sort by value?
        sorted_num_freq_hashmap = dict(sorted(num_freq_hashmap.items(), key=lambda item: item[1], reverse=True))
        print(sorted_num_freq_hashmap)

        top_k_frequent = []
        # how to iterate over k elements in dictionary
        # use itertools islice
        # 
        for num, freq in islice(sorted_num_freq_hashmap.items(), k):
            top_k_frequent.append(num)

        return top_k_frequent
