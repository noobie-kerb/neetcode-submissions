class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        c = 1
        ans = 1
        nums.sort()
        #-1 -1 0 1 3 4 5 6 7 8 9
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            elif nums[i + 1] - nums[i] == 1:
                c += 1
                ans = max(c, ans)
            else:
                c = 1
        
        return ans