class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for s in strs:
            letter_counts = [0] * 26

            for c in s:
                letter_counts[ord('a') - ord(c)] += 1
            
            if tuple(letter_counts) in dictionary:
                dictionary[tuple(letter_counts)].append(s)

            else:
                dictionary[tuple(letter_counts)] = [s]


        return list(dictionary.values())

        