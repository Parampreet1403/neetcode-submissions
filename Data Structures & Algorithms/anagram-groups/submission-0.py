class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for item in strs:
            length = len(item)
            ss = tuple(sorted(item))
            pair = (ss, length)
            if pair in myDict:
                myDict[pair].append(item)
            else:
                myDict[pair] = [item]

        ans = []
        for value in myDict.values():
            ans.append(value)

        return ans


        
        """
Same length
Same number of characters

take single item of the list
compute length
sort string
dict check
append to dictionary

dict check:
check length and sorted string pair in dict
append else create new entry

return values of dict in a list

act

act, 3: [act]


cat
item 
length check
sort 
check dictionary
append


        """