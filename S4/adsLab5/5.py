def bad_character_table(pattern):
    table = {}
    for i, char in enumerate(pattern):
        table[char] = i
    return table


def boyer_moore_search(text, pattern):
    bc_table = bad_character_table(pattern)
    n = len(text)
    m = len(pattern)
    matches = []

    i = 0
    while i <= n - m:
        j = m - 1                                           # Сравниваем с конца образца

        while j >= 0 and text[i + j] == pattern[j]:         # Поиск несовпадения справа налево
            j -= 1

        if j == -1:                                         # Если совпало
            matches.append(i+1)
            i += 1
        else:                                               # Если не совпало
            bad_char = text[i + j]                          # Правило плохого сдвига (Берём несовпавший символ из текста
                                                            # (bad_char). Ищем последнее вхождение этого символа
                                                            # в образце. Сдвигаем образец так, чтобы этот символ
                                                            # выровнялся с найденной позицией.)
            shift = j - bc_table.get(bad_char, -1)
            i += max(1, shift)

    return matches


if __name__ == "__main__":
    text = "ABAAABCDBBABCDDEBCABC"
    pattern = "ABC"

    matches = boyer_moore_search(text, pattern)

    print(f"Образец найден на позициях: {matches}")
