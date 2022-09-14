def check(x):
    l0 = list(isinstance(i, list) for i in x)
    l1 = list()
    if any(l0) == True:  # проверяем условие на наличие вложенных списков
        while any(l0) == True:  # если есть вложенный список (любой по степени вложенности), то распаковываем список
            l1.clear()
            l1.extend(x[:l0.index(True)])
            l1.extend(x[l0.index(True)])
            l1.extend(x[l0.index(True)+1:])
            # l1.extend(x[l0.index(True)])
            # x = x[:l0.index(True)] + x[l0.index(True)+1:]
            # l1.extend(x)
            l0 = list(isinstance(i, list) for i in l1)
            x = l1.copy()
    else:
        l1 = x.copy()

    l0.clear()
    for i in l1:  # цикл перебора значений основного списка
        if type(i) == int and i < 40:  # если целое число и меньше 40
            l0.append(i)
        elif type(i) == str and i.isdigit() and int(i) < 40:  #если числовое представление строки и меньше 40
            l0.append(int(i))

    return l0


a = [1, 2, 3, 45, "7", "sfddf", 23, [1, 2, 88], "56"]
b = [1, 2, 3, 45, "7", "sfddf", 23, [1, 2, 88, [2, 5]], "56", [2, 5, 6, [4, 5, [2, 1, 7, [0, 0]]]]]
c = [[1, 2, 3, 45, "7", "sfddf", 23, ["39", "sdas", "sad32", [2, 5]], "56", ["3", 5, "asd", [4, 5, ["sa4", "4", 7, ["sa", 0]]]]]]
test = [a, b, c]
for t in test:
    print(*(check(t)))

