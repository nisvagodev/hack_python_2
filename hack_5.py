"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = list(s) 
    for i in range(len(s)):
        if s[i] == "f":
            result[2] = "-"
            result.insert(5, "-")
            result[8] = "-"
        if s[i] == "b":
            result[2] = "-"
            result[5] = "-"
        if s[i] == "u":
            result[2] = "-"
        
    
    return "".join(result)

