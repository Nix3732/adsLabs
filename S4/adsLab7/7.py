def kadan(nums):
    if not nums:            # проверка на пустой массив
        return 0

    max_sum = current_sum = nums[0]     # макс и текущая сумма
    start = end = 0                     # начало и конец подходящего массива

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            start = i   # начало массива с текущего символа
        else:
            current_sum += nums[i]

        if current_sum > max_sum:       # обновляем макс сумму и границы подмассива
            max_sum = current_sum
            end = i

    return nums[start:end + 1]


# Пример использования
nums = [1, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadan(nums))