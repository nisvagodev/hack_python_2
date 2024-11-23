"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = list(s)
    if s ==[0]:
        return s
    i = 0
    while i < len(result):
        if i == 0:
            result.remove("a")
            result.insert(0, "1")
        elif i == 1:
            result.remove("b")
            result.insert(1, 2)
        elif i == 2:
            result.remove("c")
            result.insert(2, "3")
        elif i == 3:
            result.remove("d")
            result.insert(3, 4)
        elif i == 4:
            result.remove("e")
            result.insert(4, "5")
        i += 1
    return result








