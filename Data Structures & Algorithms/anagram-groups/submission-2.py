class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_reverse_map = defaultdict(list)

        for s in strs:
            sorted_string = "".join(sorted(s))
            lst = anagram_reverse_map[sorted_string].append(s)

        return list(anagram_reverse_map.values())
        