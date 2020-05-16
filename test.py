def four(act = None):
    if act is None:
        return 4
    x = act[0]
    if x == 'plus':
        return 4 + act[1]

def nine(act = None):
    if act is None:
        return 9
    x = act[0],
    if x == 'plus':
        return 9 + act[1]


def plus(var):
    return ['plus', var]

print(nine(plus(four())))
print(four(plus(nine())))