class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_int , max_count = max(nums) , 0
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == max_int:
                max_count += 1
            while max_count == k:
                if nums[l] == max_int:
                    max_count -= 1
                l += 1
            res += l                 
        return res   

     

        
