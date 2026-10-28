class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if (n in s):
                return True
            s.add(n)
        
        return False
        

        """
        set s
        for i in nums:
            if i in s:
                return false
            s.insert(i)
        
        return true
        
        """