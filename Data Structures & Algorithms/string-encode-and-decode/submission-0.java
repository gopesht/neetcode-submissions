class Solution {

    public String encode(List<String> strs) {
        StringBuilder result = new StringBuilder();
        for (String str: strs) {
            result.append(str.length());
            result.append("#");
            result.append(str);
        }
        return result.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        String length = "";
        int i = 0;
        while(i < str.length()) {
            if (str.charAt(i) != '#') {
                length += str.charAt(i);
                i++;
            }
            else {
                String actualString = str.substring(i+1, Math.min(i+1+Integer.parseInt(length), str.length()));
                result.add(actualString);
                i += Math.min(1+Integer.parseInt(length), str.length());
                length = "";
            }
            
        }

        return result;
    }
}
