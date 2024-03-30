class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingwindow(nums, k) - self.slidingwindow(nums, k-1)
    def slidingwindow(self, nums: List[int], m: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while len(count) > m:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1
            res += r - l + 1           
        return res
        
