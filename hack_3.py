"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""



def fn_hack_3(s):
    result = s
    for i in range(len(s)):
        if s[i] == 'a':
            result = result.replace('a', '@', 1)
        elif s[i] == 'e':
            result = result.replace('e', '3', 1)
        elif s[i] == 'i':
            result = result.replace('i', '¡', 1)
        elif s[i] == 'o':
            result = result.replace('o', '0', 1)
        elif s[i] == 'u':
            result = result.replace('u', 'v', 1)
        elif s[i] == 'f':
            result = result.replace('f', 'F', 1)
        elif s[i] == 'b':
            result = result.replace('b', 'B', 1)
        elif s[i] == 'n':
            result = result.replace('n', 'N', 1)
        elif s[i] == 'q':
            result = result.replace('q', 'Q', 1)
        elif s[i] == 'x':
            result = result.replace('x', 'X', 1)
    return result
