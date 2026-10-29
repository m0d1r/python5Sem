from task3 import HashTable


text = input("Введите текст: ")
table = HashTable()
result = []

for word in text.split():
    count = table.get(word)
    count = 1 if count is None else count + 1
    table[word] = count
    result.append(str(count))

print(" ".join(result))
