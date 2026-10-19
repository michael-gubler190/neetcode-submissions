class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabet = [0] * 26
        
        for letter in s:
            alphabet[ord(letter) - ord('a')] += 1
        
        for letter in t:
            alphabet[ord(letter) - ord('a')] -= 1
        
        return alphabet == ([0] * 26)
