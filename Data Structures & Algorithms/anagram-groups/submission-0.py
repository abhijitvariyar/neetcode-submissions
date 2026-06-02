class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            res[key] = res.get(key, []) + [s]

        return list(res.values())