def recursive_poly(word):
    # базовый случай
    if len(word) <= 1:
        return "YES"
    # рекурсивный случай
    if word[0] != word[-1]:
        return "NO"
    return recursive_poly(word[1:-1])


print(recursive_poly("шалаш"))
print(recursive_poly("hello"))
print(recursive_poly(""))