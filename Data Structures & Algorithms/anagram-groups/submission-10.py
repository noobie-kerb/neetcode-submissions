class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for str in strs:
            temp = "".join(sorted(str))
            groupings[temp] = [str] + groupings.get(temp, [])
        
        return list(groupings.values())