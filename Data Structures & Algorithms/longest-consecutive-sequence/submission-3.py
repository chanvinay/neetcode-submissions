class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0

        if len(nums)==1:
            return 1

        numset=set(nums)
        for num in numset:
            if num-1 not in numset:
                curr=num
                length=1
                while curr+1 in numset:
                    curr=curr+1
                    length+=1

                longest=max(longest,length)

        return longest
        