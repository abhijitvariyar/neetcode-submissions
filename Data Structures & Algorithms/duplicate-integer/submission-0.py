class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl_set = set()

        for num in nums:
            if num in dupl_set:
                return True
            else:
                dupl_set.add(num)

        return False