class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        result = 0
        i, j = 0, 0
        while j<len(s):
            if s[j] in chars:
                i = max(chars[s[j]] + 1, i)
            chars[s[j]] = j
            result = max(result, j - i + 1)
            j += 1
        return result