class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        def linearRob(start:int, end:int)->int:
            prev1=0
            prev2=0
            for i in range(start,end+1):
                curr=max(prev1, prev2+nums[i])
                prev2=prev1
                prev1=curr

            return prev1

        max1=linearRob(0,n-2)
        max2=linearRob(1,n-1)
        return max(max1,max2)        