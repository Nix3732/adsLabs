def build_finite_automaton(pattern, alphabet):                  # построение конечного автомата
    if alphabet is None:
        alphabet = set(pattern)

    m = len(pattern)
    transition = [{} for _ in range(m + 1)]                     # таблица переходов

    for q in range(m + 1):
        for char in alphabet:
            k = min(m, q + 1)
            while k > 0 and pattern[:k] != (pattern[:q] + char)[-k:]:       # поиск совпадения префикса образца длины k
                k -= 1
            transition[q][char] = k

    return transition


def search_fa(text, pattern):                       # поиск образца
    alphabet = set(text) | set(pattern)

    m = len(pattern)
    n = len(text)

    transition = build_finite_automaton(pattern, alphabet)

    q = 0
    results = []

    for i in range(n):
        char = text[i]
        q = transition[q].get(char)
        if q == m:
            results.append(i - m + 1)

    return results


if __name__ == "__main__":
    text = "abababababacababacaba"
    pattern = "ababaca"
    matches = search_fa(text, pattern)
    print(f"Найдены совпадения на позициях: {matches}")