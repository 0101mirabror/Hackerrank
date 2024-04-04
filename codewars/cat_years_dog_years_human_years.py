def func(human_year):
    if human_year == 1:
        return [1, 15, 15]
    elif human_year == 2:
        return [2, 24, 24]
    elif human_year == 0:
        return [0, 0, 0]
    return [human_year, (human_year - 2) * 4 + 24, (human_year-2) * 5 + 24]