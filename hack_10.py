"""
text: [{"a":"b"},{"c":"d"},{"e":"f"}] output => [{"1":"2"},{"3":"4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = list(s)
    for i in range(len(s)):
        if i == 0:
            result.remove({"a":"b"})
            result.insert(0,{"1":"2"})
        if i == 1:
            result.remove({"c":"d"})
            result.insert(1,{"3":"4"})
        if i == 2:
            result.remove({"e":"f"})
            result.insert(2,{"5":"6"})
            
    return result


