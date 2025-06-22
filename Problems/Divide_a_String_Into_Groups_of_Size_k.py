""" 
Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"] 
"""
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        l = []
        filler = len(s)
        if filler % k !=0:
            s += fill * (k - filler % k)
        for i in range(0, len(s), k):
            l.append(s[i:i+k])
        return l
# Example usage
print(Solution().divideString("abcdefghi", 3, "x"))  # Output: ["abc", "def", "ghi"]
print(Solution().divideString("abcdefgh", 3, "x"))   # Output: ["abc", "def", "ghx"]
print(Solution().divideString("mynameistba", 4, "x"))    # Output 