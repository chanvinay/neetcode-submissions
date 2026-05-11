from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=defaultdict(int)

        for num in nums:
            count[num]+=1
        for value in count.values():
            if value>1:
                return True
        return False