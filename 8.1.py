from re import split


def main(s):
    split_list = list(filter(None, split(
        " |def|@|[[]|[]]|<=|\n", s)))
    print(split_list)
    res = [(split_list[i], split_list[i + 1]) for i in range(
        0, len(split_list), 2)]
    return dict(res)
print(main("[ def @'esenre_30' <=-7469 def @'isinre_824'<= -2867]"))