class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(char for char in s if char.isalnum())
        # ptr_l, ptr_r = 0, len(s)-1

        # while ptr_l < ptr_r:
        #     char_l = s[ptr_l]
        #     char_r = s[ptr_r]
        #     if not s[ptr_l].isalnum():
        #         ptr_l += 1
            
        #     if not s[ptr_r].isalnum():
        #         ptr_r -= 1
            
        #     print(f"ptr_l: {ptr_l}")
        #     print(f"ptr_r: {ptr_r}")
        #     print(f"s[ptr_l]: {s[ptr_l].lower()}")
        #     print(f"s[ptr_r]: {s[ptr_r].lower()}")
        #     if s[ptr_l].lower() != s[ptr_r].lower():
        #         return False

        #     ptr_l += 1
        #     ptr_r -= 1

        # return True
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue 
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                continue
            return False
        return True