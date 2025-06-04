def container_packing(item_sizes, container_limit):
    min_containers = float('inf')
    current_containers = []

    def recursive_pack(start_idx: int) -> None:
        nonlocal min_containers, current_containers

        # все предметы упакованы
        if start_idx == len(item_sizes):
            min_containers = min(min_containers, len(current_containers))
            return

        # пробуем положить предмет в каждый контейнер
        for i in range(len(current_containers)):
            if current_containers[i] + item_sizes[start_idx] <= container_limit:
                current_containers[i] += item_sizes[start_idx]
                recursive_pack(start_idx + 1)
                current_containers[i] -= item_sizes[start_idx]

        # пробуем создать новый контейнер для текущего предмета
        if len(current_containers) < min_containers:
            current_containers.append(item_sizes[start_idx])
            recursive_pack(start_idx + 1)
            current_containers.pop()

    # рекурсивный перебор с первого предмета
    recursive_pack(0)
    return int(min_containers)


test1 = container_packing([4, 5, 2, 1, 3], 6)
print(f"{test1}")

test2 = container_packing([2, 2, 2, 2, 2, 1, 3, 4], 4)
print(f"{test2}")
