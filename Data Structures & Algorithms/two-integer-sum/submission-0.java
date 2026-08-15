class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numbers = new HashMap<>();
        int[] result = new int[2];
        for (int i = 0; i<nums.length; i++) {
            if (numbers.containsKey(target-nums[i])) {
                int otherIdx = numbers.get(target-nums[i]);
                result[0] = i < otherIdx ? i : otherIdx;
                result[1] = result[0] == i ? otherIdx : i;
                
            }

            numbers.put(nums[i], i);

        }
        return result;
    }
}
