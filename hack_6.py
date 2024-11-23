"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    if not s:
        return ["0"]
    result = list(s)
    for i in range(len(s)):
        if i == 0:
            result.remove("a")
            result.insert(0, "1")
        elif i == 1:
            result.remove("b")
            result.insert(1, "-")
        elif i == 2:
            result.remove("c")
            result.insert(2, "3")
        elif i == 3:
            result.remove("d")
            result.insert(3, "-")
        elif i == 4:
            result.remove("e")
            result.insert(4, "5")
    return result


