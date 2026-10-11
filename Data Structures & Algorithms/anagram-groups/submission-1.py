class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_reverse_map = defaultdict(list)

        for s in strs:
            sorted_string = "".join(sorted(s))
            lst = anagram_reverse_map[sorted_string]
            lst.append(s)
            anagram_reverse_map[sorted_string] = lst
        result = []
        for k, v in anagram_reverse_map.items():
            result.append(v)
        

        return result
        