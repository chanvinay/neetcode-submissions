class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=n*[0]
        stack=[]

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                previous_index=stack.pop()
                result[previous_index]=i-previous_index

            stack.append(i)

        return result
        