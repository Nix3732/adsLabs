import math
# << - битовый сдвиг влево, >> - битовый сдвиг вправо


def hidden_salesman(matrix, origin):
    cities = len(matrix)                                # кол-во городов
    full_route = (1 << cities) - 1                      # битовая маска посещенных городов

    cost_table = [[math.inf] * cities for _ in range(full_route + 1)]  # таблица весов
    prev_city = [[-1] * cities for _ in range(full_route + 1)]         # восстановление пути
    cost_table[1 << origin][origin] = 0                 # нулевая стоимость для начального города

    for route_mask in range(full_route + 1):
        for current in range(cities):
            if not (route_mask & (1 << current)):     # обновляем стоимость маршрута, если найден более оптимальный путь
                continue

            for next_city in range(cities):
                if route_mask & (1 << next_city):
                    continue

                new_cost = cost_table[route_mask][current] + matrix[current][next_city]
                if new_cost < cost_table[route_mask | (1 << next_city)][next_city]:
                    cost_table[route_mask | (1 << next_city)][next_city] = new_cost
                    prev_city[route_mask | (1 << next_city)][next_city] = current

    best_cost = math.inf    # подсчитываем минимальную стоимость полного цикла
    final_stop = -1
    for city in range(cities):
        if city == origin:
            continue
        complete_cost = cost_table[full_route][city] + matrix[city][origin]
        if complete_cost < best_cost:
            best_cost = complete_cost
            final_stop = city

    journey = []            # восстанавливаем маршрут по таблице prev_city
    current_mask = full_route
    current_city = final_stop
    while current_city != -1:
        journey.append(current_city)
        previous = prev_city[current_mask][current_city]
        current_mask ^= (1 << current_city)         # ^ - XOR
        current_city = previous
    journey.reverse()
    journey.append(origin)

    return best_cost, journey


# 4 города
example1 = [
    [0, 12, 18, 24],
    [12, 0, 36, 28],
    [18, 36, 0, 32],
    [24, 28, 32, 0]
]
cost1, path1 = hidden_salesman(example1, 0)
print(f"Маршрут: {' - '.join(map(str, path1))}, Стоимость: {cost1}")

# Треугольник с неравными сторонами
example2 = [
    [0, 5, 9],
    [5, 0, 6],
    [9, 6, 0]
]
cost2, path2 = hidden_salesman(example2, 1)
print(f"Маршрут: {' - '.join(map(str, path2))}, Стоимость: {cost2}")

# 5 городов с асимметричными путями
example3 = [
    [0, 3, 1, 5, 8],
    [3, 0, 6, 7, 9],
    [1, 6, 0, 4, 2],
    [5, 7, 4, 0, 3],
    [8, 9, 2, 3, 0]
]
cost3, path3 = hidden_salesman(example3, 2)
print(f"Маршрут: {' - '.join(map(str, path3))}, Стоимость: {cost3}")

# Невозможный маршрут (изолированный город)
example4 = [
    [0, 1, math.inf],
    [1, 0, 1],
    [math.inf, 1, 0]
]
cost4, path4 = hidden_salesman(example4, 0)
print(f"Маршрут: {' - '.join(map(str, path4))}, Стоимость: {cost4}")