from collections import defaultdict
class Solution(object):
    def minimumTotalCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        conflict_indices = []
        freq = defaultdict(int)
        
        total_cost = 0
        dominant_num = -1
        dominant_freq = 0

        for i in range(n):
            if nums1[i] == nums2[i]:
                conflict_indices.append(i)
                freq[nums1[i]] += 1
                total_cost += i
                if freq[nums1[i]] > dominant_freq:
                    dominant_freq = freq[nums1[i]]
                    dominant_num = nums1[i]
        if dominant_freq * 2 <= len(conflict_indices):
            return total_cost
        required = dominant_freq * 2 - len(conflict_indices)
        extra_cost = 0
        count = 0

        for i in range(n):
            if nums1[i] != nums2[i] and nums1[i] != dominant_num and nums2[i] != dominant_num:
                extra_cost += i
                count += 1
                if count == required:
                    break

        if count < required:
            return -1

        return total_cost + extra_cost
        