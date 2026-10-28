class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        table = {}
        for i in nums:
            table[i] = table.get(i, 0) + 1

        by_value = dict(sorted(table.items(), key=lambda item: item[1], reverse=True))
        for key in by_value.keys():
            if k == 0:
                return ans
            else:
                ans.append(key)
                k = k - 1
        
        return ans

        


        """
loop over the array
keep track of unique elements and the number of times they appear
order them by frequency
find the k most

1 : 1
2 : 2
3 : 3
        """



