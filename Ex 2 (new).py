result = []

def func(a):
    global result
    if isinstance(a, int):
        print(".".join(result), "=", a)
        result.pop(len(result) - 1)

    else:
        for key in a:
            result.append(key)
            func(a[key])
        if result:
            result.pop(len(result) - 1)

X = {"a": 1, "b": 2, "c": {"d": 3, "e": {"h": 4, "g": 5}, "k": 7}}
Y = {"a": {"z": 8, "x": {"u": 9, "w": {"ww": {"www": 3}}},"y": 13}, "b": 2, "c": {"d": 3, "e": {"h": 4, "g": 5}, "k": 7}}
Z = {"a": 1, "b": 2}
test = [X, Y, Z]
for t in test:
    func(t)
    print()