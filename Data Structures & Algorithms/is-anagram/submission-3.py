class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dctS: dict[str,int] = {}
        dctT: dict[str,int] = {}
        for idx in range(len(s)):
            dctS[s[idx]] = 1 + dctS.get(s[idx],0)
            dctT[t[idx]] = 1 + dctT.get(t[idx],0)

        return dctS == dctT