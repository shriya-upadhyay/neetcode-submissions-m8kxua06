class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            #combine length, delimeter, and string
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        ret_val = []
        curr_ind = -1
        i = 0

        while i < len(s):
            # find the '#'
            j = i
            while s[j] != '#':
                j += 1

            # get full length (not just one digit)
            curr_ind = int(s[i:j])

            # extract the string
            start = j + 1
            end = start + curr_ind
            ret_val.append(s[start:end])

            # move pointer
            i = end

        return ret_val

