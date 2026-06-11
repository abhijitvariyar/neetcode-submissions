class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind = {}
        for i in range(len(numbers)):
            num = numbers[i]
            diff = target - num
            # print(f"num: {num}")
            # print(f"diff: {diff}")

            if diff in ind:
                return [ind[diff]+1, i+1]
            else:
                ind[num] = i

        
