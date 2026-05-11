from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        maxLen=0
        maxFreq=0
        left=0

        for right in range(len(s)):
            freq[s[right]]+=1
            maxFreq=max(maxFreq,freq[s[right]])
            if (right-left+1)-maxFreq >k:
                freq[s[left]]-=1
                left+=1

            maxLen=max(maxLen, right-left+1)

        return maxLen
        