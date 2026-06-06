class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(char for char in s if char.isalnum())
        ptr_l, ptr_r = 0, len(s)-1

        while ptr_l < ptr_r:
            char_l = s[ptr_l]
            char_r = s[ptr_r]
            if not s[ptr_l].isalnum():
                ptr_l += 1
                continue
            
            if not s[ptr_r].isalnum():
                ptr_r -= 1
                continue
            
            if s[ptr_l].lower() == s[ptr_r].lower():
                ptr_l += 1
                ptr_r -= 1
                continue
            return False
        return True