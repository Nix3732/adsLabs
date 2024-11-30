class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def save(self, path):
        """Сохранение хеш-таблицы в файл."""
        with open(path, 'w') as f:
            for bucket in self.table:
                for item in bucket:
                    f.write(f"{item[0]},{item[1]}\n")

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

