class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        uniq_chars = set()

        max_size = 0
        while r < len(s):
            # print(f"l: {l}\tr: {r}")
            if s[r] in uniq_chars:
                uniq_chars.discard(s[l])
                l += 1
            else:
                uniq_chars.add(s[r])
                r += 1
                size = r - l

                if size > max_size: max_size = size

        return max_size