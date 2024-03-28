class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count , add = 0 , 0
        l = 0
        for r in range(len(nums)):
            add += nums[r]
            length = r - l + 1
            score = add * length
            while l <= r and score >= k:
                add -= nums[l]
                l += 1
                length = r - l + 1
                score = add * length
            count += r - l + 1    
        return count


        
