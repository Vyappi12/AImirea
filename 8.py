from re import split


def main(s):
    split_list = list(filter(None, split(
        ' |begin|variable|[.]?end|;|:=|[.]do|,|\n', s)))
    res = [(split_list[i], split_list[i + 1]) for i in range(
        0, len(split_list), 2)]
    return res
print(main('.do begin variable edorxe:= xeinat; end,begin variable raesla :=\norce_312; end, .end'))