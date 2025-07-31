class Solution(object):
    def subarrayBitwiseORs(self, arr):
        result = set()
        prev = set()

        for num in arr:
            curr = {num}
            for val in prev:
                curr.add(val | num)
            prev = curr
            result.update(curr)

        return len(result)

        