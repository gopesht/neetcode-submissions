class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = 0
        tMap = {}
        sMap = {}
        tLen = len(t)
        sLen = len(s)
        i, j = 0, 0
        low, high, length = -1, -1, float("infinity")
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        totalChars = len(tMap)
        for j in range(sLen):
            sMap[s[j]] = 1 + sMap.get(s[j], 0)
            if s[j] in tMap and sMap[s[j]] == tMap[s[j]]:
                target += 1
            while i<=j and target == totalChars:
                if (j - i + 1) < length:
                    high = j
                    low = i
                    length = j - i + 1
                sMap[s[i]] -= 1
                if s[i] in tMap and sMap[s[i]] < tMap[s[i]]:
                    target -= 1
                i += 1
                
        return s[low:high + 1] if length != float("infinity") else ""


                

        