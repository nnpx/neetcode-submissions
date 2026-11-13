from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Every word is followed by '&', even if empty
        # []      -> ""
        # [""]    -> "&"
        # ["", ""]-> "&&"
        # ["a"]   -> "97&"
        encoded = []
        for word in strs:
            codes = [str(ord(c)) for c in word]
            encoded.append(",".join(codes) + "&")
            # print(encoded)
        # print("".join(encoded))
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoded_strs = []
        # Remove trailing '&' before splitting to avoid an extra phantom element
        words = s[:-1].split("&")
        # print(words)

        for word in words:
            if not word:
                decoded_strs.append("")
            else:
                decoded_strs.append(
                    "".join(chr(int(c)) for c in word.split(","))
                )

        # print(decoded_strs)
        return decoded_strs