#1 вариант простая регулярка, которая сплитит все символы, кроме слов и чисел (дробных и отрицательных тоже)


import re


def main(s):
    split_list = re.findall(r'-?\d*\.?\d+|\w+', s) # ['def', 'esenre_30', '-7469', 'def', 'isinre_824', '-2867']
    res = [(split_list[i + 1], split_list[i + 2]) for i in range(
        0, len(split_list), 3)] # делаем шаг 3, 1 слово def, потом переменная и значение
    return dict(res)


print(main("[ def @'esenre_30' <=-7469 def @'isinre_824'<= -2867]"))


#2 вариант через сплит

from re import split


def main(s):
    split_list = list(filter(None, split(
        " |def|@|[[]|[]]|<=|\n", s)))
    print(split_list)
    res = [(split_list[i], split_list[i + 1]) for i in range(
        0, len(split_list), 2)]
    return dict(res)
print(main("[ def @'esenre_30' <=-7469 def @'isinre_824'<= -2867]"))

