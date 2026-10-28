class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [0] * n
        pref_prod = [0] * n
        suff_prod = [0] * n
        
        pref_prod[0] = suff_prod[n - 1] = 1
        for i in range(1, n):
            pref_prod[i] = nums[i - 1] * pref_prod[ i - 1]
        for i in range(n - 2, -1, -1):
            suff_prod[i] = nums[i + 1] * suff_prod[i + 1]
        for i in range(n):
            r[i] = pref_prod[i] * suff_prod[i]
 
        return r
