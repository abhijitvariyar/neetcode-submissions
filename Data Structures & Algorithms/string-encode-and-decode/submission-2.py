class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            encoded_str += string
            encoded_str += "\\$"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        words = []
        new_word = ""

        for char in s:
            # print(f"curr_char: {char}")
            if char == "$":
                if new_word[-1] == "\\":
                    words.append(new_word[:-1])
                    new_word = ""
                    continue
            
            new_word += char

        return words

                