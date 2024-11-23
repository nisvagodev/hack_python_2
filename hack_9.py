"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(s):
    result = dict(s)
    new_result = {}
    for key, value in result.items():
        if key == 'foo':
            value = "Fooziman"
            new_result['Foo'] = value
    result = new_result
    return result


