class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        Lmax=[0]*n
        Rmax=[0]*n
        Lmax[0]=height[0]
        Rmax[n-1]=height[n-1]

        for i in range(1,n):
            Lmax[i]=max(height[i],Lmax[i-1])

        for j in range(n-2,-1,-1):
            Rmax[j]=max(height[j],Rmax[j+1])

        totalTrapped=0

        for i in range(n):
            currTrapped=min(Lmax[i],Rmax[i])-height[i]
            totalTrapped+=currTrapped

        return totalTrapped
        