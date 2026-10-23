class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for c in s:
            char_count[c] = 1 + char_count.get(c, 0)
        for c in t:
            char_count[c] = char_count.get(c, 0) - 1
        
        return all(x == 0 for x in char_count.values())