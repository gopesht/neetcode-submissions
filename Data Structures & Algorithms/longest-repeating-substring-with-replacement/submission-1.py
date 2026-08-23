class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        result = 0
        chars = {}
        maxChars = 0
        for j in range(len(s)):
            chars[s[j]] = 1 + chars.get(s[j], 0)
            maxChars = max(maxChars, chars[s[j]])
            while ((j - i + 1) - maxChars) > k:
                chars[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
        return result



                

                

        