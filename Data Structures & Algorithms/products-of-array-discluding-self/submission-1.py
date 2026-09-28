class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix_product=[0]*n
        suffix_product=[0]*n
        prefix_product[0]=1
        suffix_product[n-1]=1

        productArray=[0]*n

        for i in range(1,n):
            prefix_product[i]=prefix_product[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suffix_product[j]=suffix_product[j+1]*nums[j+1]

        for i in range(n):
            productArray[i]=suffix_product[i]*prefix_product[i]

        return productArray

        