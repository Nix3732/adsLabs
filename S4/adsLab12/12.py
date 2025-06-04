def hidden_knapsack(capacity, item_weights, item_values, item_count):
    solution_table = [[0 for _ in range(capacity + 1)] for _ in range(item_count + 1)]  # таблица решения

    for current_item in range(1, item_count + 1):
        for current_weight in range(capacity + 1):
            if item_weights[current_item - 1] <= current_weight:    # проверка на превышение лимита по весу
                solution_table[current_item][current_weight] = max(  # макс между не брать предмет или брать но с оптимальным решением для оставшегося места
                    solution_table[current_item - 1][current_weight],
                    solution_table[current_item - 1][current_weight - item_weights[current_item - 1]] + item_values[
                        current_item - 1]
                )
            else:   # предмет не поместился
                solution_table[current_item][current_weight] = solution_table[current_item - 1][current_weight]

    return solution_table[item_count][capacity]


test1 = hidden_knapsack(10, [2, 3, 5, 7], [10, 15, 20, 25], 4)
print(f"{test1}")

test2 = hidden_knapsack(10, [1, 2, 3, 4, 10], [2, 3, 7, 9, 20], 5)
print(f"{test2}")

