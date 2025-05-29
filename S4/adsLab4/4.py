def compute_lps(pattern):         # поиск lps (longest prefix suffix)
    lps = [0] * len(pattern)
    l = 0   # длина совпадения

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
    print(lps)
    return lps


def kmp_search(text, pattern):   # алгоритм Кнута-Морриса-Пратта
    m = len(pattern)
    n = len(text)

    lps = compute_lps(pattern)

    i = 0
    j = 0
    matches = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:          # при сопадении перепрыгиваем на значение lps[j - 1]
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


if __name__ == "__main__":
    text = "ABABCABABBACDABABCABAB"
    pattern = "ABABCABAB"

    matches = kmp_search(text, pattern)

    print(f"Образец найден на позициях: {matches}")
