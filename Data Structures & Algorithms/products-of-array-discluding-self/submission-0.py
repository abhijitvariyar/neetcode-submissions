class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            
            prod *= num

        if zero_count > 1:
            return [0] * len(nums)
        
        for i in range(len(nums)):
            num = nums[i]
            if zero_count == 1:
                if num != 0:
                    nums[i] = 0
                else:
                    nums[i] = prod
            else:
                nums[i] = prod // nums[i]
        
        return nums