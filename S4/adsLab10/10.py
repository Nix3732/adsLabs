def mysterious_attempts(oval_items, height_levels):
    attempt_data = [[0] * (height_levels + 1) for _ in range(oval_items + 1)]   # промежуточные рез-ы

    for h in range(1, height_levels + 1):     # одно яйцо
        attempt_data[1][h] = h

    for o in range(2, oval_items + 1):        # несколько яиц
        for h in range(1, height_levels + 1):
            attempt_data[o][h] = attempt_data[o - 1][h - 1] + attempt_data[o][h - 1] + 1  # сумма этажей с разбитым яйцом и с не разбитым + текущая попытка

    result = -1                               # поиск минимального числа попыток
    for h in range(1, height_levels + 1):
        if attempt_data[oval_items][h] >= height_levels:
            result = h
            break

    return result


print("2 яйца, 100 этажей:", mysterious_attempts(2, 100), "бросков")  # Ожидается 14
print("3 яйца, 14 этажей:", mysterious_attempts(3, 14), "бросков")  # Ожидается 4
