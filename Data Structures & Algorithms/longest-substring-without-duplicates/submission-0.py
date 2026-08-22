class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        result = 0
        i, j = 0, 0
        while j<len(s):
            if s[j] not in chars:
                chars.add(s[j])
                result = max(result, j - i + 1)
                j += 1
            else:
                chars.remove(s[i])
                i += 1
        return result