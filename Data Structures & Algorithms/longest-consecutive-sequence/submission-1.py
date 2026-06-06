class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set()
        mem = {}
        for num in nums:
            vals.add(num)

        longest = 0
        for num in nums:
            seq_len = 1
            i = num
            while True:
                if i-1 not in vals:
                    break
                seq_len += 1
                i -= 1
            if seq_len > longest:
                longest = seq_len

        return longest