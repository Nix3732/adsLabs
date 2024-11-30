import os
import tempfile
import heapq

def merge_sorted_files(srtd_files, output):
    """Слияние отсортированных файлов."""
    with open(output, 'w') as out:
        # создание генераторов
        file_iters = [open(file, 'r') for file in srtd_files]
        min_heap = []

        # первый элемент из файла в кучу
        for i, file_iter in enumerate(file_iters):
            line = file_iter.readline()
            if line:
                min_heap.append((int(line.strip()), i))

        heapq.heapify(min_heap)

        # извлечение элементов из кучи
        while min_heap:
            smallest, file_index = heapq.heappop(min_heap)
            out.write(f"{smallest}\n")  # запись отсортированного числа

            next_line = file_iters[file_index].readline()
            if next_line:
                min_heap.append((int(next_line.strip()), file_index))

    for file_iter in file_iters:
        file_iter.close()


def external_sort(input, output, chunk=1000):
    """Внешняя сортировка файла."""
    sorted_files = []

    # чтение и сортировка
    with open(input, 'r') as infile:
        while True:
            lines = infile.readlines(chunk)
            if not lines:
                break

            numbers = [int(line.strip()) for line in lines]
            numbers.sort()  # сортировка

            # временный файл
            temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')
            temp_file.writelines(f"{num}\n" for num in numbers)
            temp_file.close()
            sorted_files.append(temp_file.name)

    # cлияние
    merge_sorted_files(sorted_files, output)


input = 'random_numbers.txt'
output = 'output.txt'
external_sort(input, output)
