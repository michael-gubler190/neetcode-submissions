class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)

        for word in strs:
            alphabet = [0] * 26

            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1

            anagramGroup = tuple(alphabet)
            anagramGroups[anagramGroup].append(word)
        
        return list(anagramGroups.values())
