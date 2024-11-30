class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]  # Инициализируем таблицу списками

    def _hash(self, key):
        """Хеш-функция для получения индекса."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Вставка нового ключа-значения в хеш-таблицу."""
        index = self._hash(key)
        # Проверяем, существует ли ключ, и обновляем значение, если он существует
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        # Если ключ не найден, добавляем новую пару
        self.table[index].append([key, value])

    def search(self, key):
        """Поиск значения по ключу."""
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]  # Возвращаем значение
        return None  # Если ключ не найден

    def delete(self, key):
        """Удаление ключа из хеш-таблицы."""
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]  # Удаляем элемент из списка
                return

    def save(self, path):
        """Сохранение хеш-таблицы в файл."""
        with open(path, 'w') as f:
            for bucket in self.table:
                for item in bucket:
                    f.write(f"{item[0]},{item[1]}\n")  # Сохраняем ключ и значение

ht = HashTable()
f = open('input.txt', 'r', encoding="utf-8")
m = [i.lower() for i in sum([k.split('\n') for k in f.read().split(' ')], [])]
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] in '.,-—!?…>":«»':
            m[i] = m[i].replace(m[i][j], ' ')
m = [x for x in [x.strip() for x in m if x] if x]

for i in m:
    ht.insert(i, ht._hash(i))
ht.save('output.txt')

