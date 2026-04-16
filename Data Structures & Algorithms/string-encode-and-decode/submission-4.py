class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += s
            result += "-"

        return result

    def decode(self, s: str) -> List[str]:
        curr = ""
        ret_val = []
        for letter in s:
            if letter != "-":
                curr += letter
            else:
                ret_val.append(curr)
                curr = ""
        return ret_val

