class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for c in s:
            map1[c] += 1
        
        for c in t:
            map2[c] += 1
        if len(map1) != len(map2):
            return False
        for k, v in map1.items():
            if map1[k] != map2[k]:
                return False
        

        return True
