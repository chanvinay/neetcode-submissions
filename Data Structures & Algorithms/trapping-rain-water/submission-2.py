class Solution:
    def trap(self, heights: List[int]) -> int:
        n=len(heights)
        Lmax=[0]*n
        Rmax=[0]*n

        Lmax[0]=heights[0]
        Rmax[n-1]=heights[n-1]

        for i in range(1,n):
            Lmax[i]=max(heights[i],Lmax[i-1])

        for j in range(n-2,-1,-1):
            Rmax[j]=max(heights[j],Rmax[j+1])

        totalTrapped=0
        for i in range(n):
            currTrapped=min(Lmax[i],Rmax[i])-heights[i]
            totalTrapped+=currTrapped

        return totalTrapped

        