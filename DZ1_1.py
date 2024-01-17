class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_value = None
        for elem in self.table:
            if elem != []:
                for pair in elem:
                    if pair[0] == key:
                        key_value = pair
                if key_value != None:
                    elem.remove(key_value)
                    print(f"'{key}' deleted from the hush table")
                    return
        print(f"There is no '{key}' in the hash table")
        return

if __name__ == "__main__":
    # testing the code:
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)
    print(H.table)

    H.delete("plum")  # no such element
    H.delete("orange")  # orange deleted
    print(H.table)
    H.delete("banana")  # banana deleted
    print(H.table)
