class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            bits_1 = bin(i).count('1')
            result.append(bits_1)
        
        return result