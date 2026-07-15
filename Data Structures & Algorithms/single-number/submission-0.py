class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        req=0
        for num in nums:
            req=req^num

        return req
        