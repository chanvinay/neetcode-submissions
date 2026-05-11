from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=defaultdict(int)
        if len(s) != len(t):
            return False
        for char in s:
            freq[char]+=1
        for char in t:
            freq[char]-=1

        for value in freq.values():
            if value>0:
                return False

        return True
        