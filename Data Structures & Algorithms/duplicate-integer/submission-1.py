from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        for count in freq.values():
            if count>1:
                return True

        return False
        