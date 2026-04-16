class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams are strings that contain exact same characters
        # racecar carrace are anagrams
        # we need to use set/dict. can't use set because it doesn't account for duplicate characters.
        # convert the str to dicts/hashmaps

        # racecar
        # a: 2
        # c: 2
        # e: 1
        # r: 2

        # carrace
        # a: 2
        # c: 2
        # e: 1
        # r: 2

        # convert string s to hashmap
        string_s_dict = {}
        string_t_dict = {}

        for char in s:
            if char not in string_s_dict:
                # add char to the string_s_dict
                string_s_dict[char] = 1
            else: 
                # add 1 to the number of occurences of that char
                string_s_dict[char] += 1
            string_s_dict[char]
        
        for char in t:
            if char not in string_t_dict:
                string_t_dict[char] = 1
            else:
                string_t_dict[char] += 1


        print(f"string_s_dict: {string_s_dict}")
        print(f"string_t_dict: {string_t_dict}")

        # check that both string_s_dict and string_t_dict have the same length, if not, then they have different unique characters
        if len(string_s_dict) != len(string_t_dict):
            return False
        
        # now iterate through each dict.
        # the dicts aren't sorted though. 
        for key in string_s_dict:
            # you can't access element that doesn't exist. What's a work around here?
            # first check if the key is in both dicts, then check that the value is the same
            if key not in string_t_dict:
                return False
            if string_s_dict[key] != string_t_dict[key]:
                return False
        
        return True