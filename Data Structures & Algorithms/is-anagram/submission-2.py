class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_prd, t_prd = 1, 1
        s_sum, t_sum = 0, 0

        for i in range(len(s)):
            # print(f'ord(s[i]): {ord(s[i])}')
            # print(f'ord(t[i]): {ord(t[i])}')
            s_prd *= ord(s[i]) ** 2
            t_prd *= ord(t[i]) ** 2

            s_sum += ord(s[i]) ** 2
            t_sum += ord(t[i]) ** 2

        # print(f's_prd: {s_prd}\tt_prd: {t_prd}')
        # print(f's_sum: {s_sum}\tt_sum: {t_sum}')
        if s_prd == t_prd and s_sum == t_sum:
            return True

        return False

        # s_freq, t_freq = {}, {}

        # for i in range(len(s)):
        #     s_char = s[i]
        #     t_char = t[i]

        #     if s_char in s_freq:
        #         s_freq[s_char] += 1
        #     else:
        #         s_freq[s_char] = 1

        #     if t_char in t_freq:
        #         t_freq[t_char] += 1
        #     else:
        #         t_freq[t_char] = 1
            
        # for s_char in s_freq:
        #     if s_char in t_freq:
        #         if s_freq[s_char] != t_freq[t_char]:
        #             return False
        #     else:
        #         return False

        # return True