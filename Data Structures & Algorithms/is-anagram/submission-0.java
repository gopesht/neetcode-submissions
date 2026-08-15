class Solution {
    public boolean isAnagram(String s, String t) {
        int[] charactersCountS = new int[27];
        int[] charactersCountT = new int[27];

        for (int i=0; i<s.length(); i++) {
            charactersCountS[s.charAt(i) - 97]++;
        }

        for (int i=0; i<t.length(); i++) {
            charactersCountT[t.charAt(i) - 97]++;
        }
        

        for (int i = 0; i<27; i++) {
            if (charactersCountT[i]!= charactersCountS[i]) return false;
        }

        return true;
    }
}
