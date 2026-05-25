class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index_dict:
                output = [index_dict[diff], i]
                return [min(output), max(output)]
            else:
                if nums[i] not in index_dict:
                    index_dict[nums[i]] = i
        
        return []