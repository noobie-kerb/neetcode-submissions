class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list) 
        for str in strs:
            key = ''.join(sorted(str))
            my_dict[key].append(str)
        
        return list(my_dict.values())
        