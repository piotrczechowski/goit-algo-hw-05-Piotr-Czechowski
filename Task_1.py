class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

# Testing the HashTable with delete functionality
hash_table = HashTable()

# Adding key-value pairs
hash_table.put('key1', 'value1')
hash_table.put('key2', 'value2')
hash_table.put('key3', 'value3')

print("Initial table state:")
print(hash_table.table)

# Deleting a key-value pair
print("\nDeleting 'key2':", hash_table.delete('key2'))

print("Table state after deleting 'key2':")
print(hash_table.table)

# Trying to delete a non-existing key
print("\nDeleting 'key4' (non-existing):", hash_table.delete('key4'))

print("Table state after attempting to delete 'key4':")
print(hash_table.table)

# Fetching values to ensure the table integrity
print("\nValue for 'key1':", hash_table.get('key1'))
print("Value for 'key2':", hash_table.get('key2'))
print("Value for 'key3':", hash_table.get('key3'))
