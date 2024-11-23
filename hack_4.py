"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    for i in range(len(s)):
        if s[i] == 'f' or s[i] == 'b' or s[i] == 'n':
            result = result.replace('f', "")
            result = result.replace('b', "")
            result = result.replace('n', "")
            
    return result


