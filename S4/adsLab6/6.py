def rabin_karp_automaton(text, pattern):
    q = 307                 # простое число для модуля
    d = 256                 # размер алфавита
    n = len(text)           # размер текста
    m = len(pattern)        # размер паттерна
    positions = []

    if m == 0 or n == 0 or m > n:
        return positions

    h = pow(d, m - 1, q)    # вычисление h по модулю q

    pattern_hash = 0        # хеш образца
    text_hash = 0         # хеш текста

    for i in range(m):      # вычисление хеша одновременно (используется формула полиномиального хэширования)
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        if text_hash == pattern_hash:           # совпадение хэшей
            if text[i: (i + m)] == pattern:     # совпадение символов
                positions.append(i)

        if i < n - m:                           # пересчитываем хэш для текста по формуле скользящего хэша
            # вычитаем вклад уходящего символа (text[i])
            # добавляем вклад нового символа (text[i+m])
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if text_hash < 0:           # хэш неотрицательный
                text_hash += q

    return positions


text = "ABABDABACDABABCABAB"
pattern = "AB"
print(rabin_karp_automaton(text, pattern))