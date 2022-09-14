def dicts(v):
    l0 = [key for key, value in v.items() if isinstance(value, dict)]  # добавляем в список ключ, где значение словарь
    d2 = dict()
    while len(l0) > 0:  # если есть вложенный словарь, то выполняем цикл
        d2.clear()
        for key, value in v.items():
            if key != l0[0]:
                d2[key] = value
            elif key == l0[0]:
                for key2, value2 in value.items():
                    d2[key + '.' + key2] = value2
        l0 = [key for key, value in d2.items() if isinstance(value, dict)]
        v = d2.copy()

    for key, value in d2.items():  # выводим на экран
        print(f'{key} = {value}')


X = {"a": 1, "b": 2, "c": {"d": 3, "e": {"h": 4, "g": 5}, "k": 7}}
Y = {"a": {"z": 8, "x": {"u": 9, "w": {"ww": {"www": 3}}},"y": 13}, "b": 2, "c": {"d": 3, "e": {"h": 4, "g": 5}, "k": 7}}
dicts(X)
print()
dicts(Y)



