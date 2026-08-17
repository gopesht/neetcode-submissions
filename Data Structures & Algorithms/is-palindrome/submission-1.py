class Solution:
    def isPalindrome(self, s: str) -> bool:
        copyString = s.lower().replace(" ", "")
        copyString = re.sub(r'[^a-zA-Z0-9]', "", copyString)
        n = len(copyString)
        if n == 0:
            return True
        if n % 2 == 0:
            n = (n // 2) + 1
        else:
            n = n // 2

       
        print(copyString)
        print(n)
        for i in range(n):
            if copyString[i] != copyString[-(i+1)]:
                return False
        return True
        