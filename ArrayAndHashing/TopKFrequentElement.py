"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

"""
def topKFrequent(nums, k):
    from collections import Counter
    import heapq
    count = Counter(nums)
    min_heap = []

    for val, freq in count.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, val))
        elif freq > min_heap[0][0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (freq, val))

    return [val[1] for val in min_heap]
