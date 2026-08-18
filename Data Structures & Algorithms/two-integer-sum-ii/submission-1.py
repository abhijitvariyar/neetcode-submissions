class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind = {}
        for i, num in enumerate(numbers):
            diff = target - num

            if diff in ind:
                return [ind[diff]+1, i+1]
            else:
                ind[num] = i

        
