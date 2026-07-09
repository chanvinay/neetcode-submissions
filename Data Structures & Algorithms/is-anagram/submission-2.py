from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        freq=defaultdict(int)
        for char in s:
            freq[char]+=1
        for char in t:
            freq[char]-=1

        for count in freq.values():
            if count!=0:
                return False

        return True
        