class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_dict:
                output = [index_dict[diff], i]
                return [min(output), max(output)]
            else:
                if num not in index_dict:
                    index_dict[num] = i
        
        return []