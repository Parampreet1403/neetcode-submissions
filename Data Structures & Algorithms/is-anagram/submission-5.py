class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
        
        # if len(s) is not len(t):
        #     return False
        
        # x = sorted(s)
        # y = sorted(t)

        # for a,b in zip(x, y):
        #     if a is not b:
        #         return False

        # return True
"""
Loop over string and store it in a hashmap
Loop over 2nd string
check to see if its the 2nd dict


Sort both strings and then go over each
"""


      