class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)

        for l in s:
            letters[l] += 1

        for l in t:
            letters[l] -=1

        print(letters)

        for val in letters.values():
            if val != 0:
                return False

        return True
        
        