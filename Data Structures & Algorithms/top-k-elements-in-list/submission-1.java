class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequency = new HashMap<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> frequency.get(b) - frequency.get(a));

        for (int i = 0; i<nums.length; i++) {
            frequency.put(nums[i], frequency.getOrDefault(nums[i], 0) + 1);
        }

        frequency.entrySet().stream().forEach(entry -> {
            pq.offer(entry.getKey());
        });

        List<Integer> result = new ArrayList<>();
        while(!pq.isEmpty() && k > 0) {
            result.add(pq.poll());
            k--;
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}
