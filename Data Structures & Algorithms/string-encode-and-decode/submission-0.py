class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for s in strs:
            x = x + str(len(s)) + "#" + s

        return x

    def decode(self, s: str) -> List[str]:
        y = []
        max_length = len(s)
        i = 0
        length = ""
        while i != max_length:
            char = s[i]
            
            if char != "#":
                length = length + char
                i = i + 1
            elif  char == "#":
                length = int(length)
                i = i+1
                y.append(s[i:i+length])
                i = i+length
                length = ""

        return y


"""
list of string values -> turn into a single string

string value and returns a list

Problem is, how to know where the spaces are

["Hello", " World"] -> HelloWorld
Hello World -> ["Hello", "World"]


ENCODE
x = ""
for s in strs:
    x = x + str(len(s)) + "#" + s

return x


5#Hello5#World
DECODE

y = []
max_length = len(s)
i = 0
length = ""
while i != max_length:
    char = s[i]
    
    if char != "#":
        length = length + char
        i = i + 1
    elif  char == "#":
        length = int(length)
        i = i+1
        y.append(s[i:i+length])
        i = i+length
        length = ""

return y

    


    




"""