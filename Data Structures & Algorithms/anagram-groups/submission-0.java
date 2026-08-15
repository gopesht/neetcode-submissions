class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramKeyReverseMap = new HashMap<>();

        for (int i = 0; i<strs.length; i++) {
            char[] str = strs[i].toCharArray();
            Arrays.sort(str);
            String sortedStr = new String(str);
            var lst = anagramKeyReverseMap.getOrDefault(sortedStr, new ArrayList());
            lst.add(strs[i]);
            anagramKeyReverseMap.put(sortedStr, lst);
        }

        return anagramKeyReverseMap.values().stream().collect(Collectors.toList());

    }
}
