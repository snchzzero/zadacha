d1 = dict()
def dicts(X):
    for key, value in X.items():  # проверка значения словаря на тип, если словарь то распаковка
        if type(value) == dict:
            for key2, value2 in value.items():
                d1[key + '.' + key2] = value2
        else:
            d1[key] = value

    # если в распакованном словаре в значениях есть словарь, то повторно вызываем функцию
    if any([isinstance(value, dict) for key, value in d1.items()]):
        X = d1.copy()
        d1.clear()
        dicts(X)
    else:
        for key, value in d1.items():  # выводим на экран если в значениях нет словарей
            print(f'{key} = {value}')
        d1.clear()


X = {"a": 1, "b": 2, "c": {"d": 3, "e": {"h": 4, "g": 5}, "k": 7}}
Y = {"a": {"z": 8, "x": {"u": 9, "w": {"ww": {"www": 3}}},"y": 13}, "b": 2, "c": {"d": 3, "e": {"h": 4, "g": 5}, "k": 7}}
Z = {"a": 1, "b": 2}
dicts(X)
print()
dicts(Y)
print()
dicts(Z)
