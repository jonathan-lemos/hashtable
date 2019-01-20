import sys
from functools import reduce


class HashTable:
    def __init__(self, capacity):
        self.arr = [None] * capacity

    def hash(self, string):
        return reduce(lambda a, c: (a * 31 + ord(c)) % len(self.arr), string, 0)

    def insert(self, key, data):
        index = self.hash(key)
        print("Inserting [" + key + "," + str(data) + "]")
        for i in list(range(index, len(self.arr))) + list(range(index)):
            if self.arr[i] is not None:
                print("Insert: Collision at index " + str(i))
                continue
            self.arr[i] = [key, data]
            print("Inserting [" + key + "," + str(data) + "] at index " + str(i))
            return
        print("Could not insert [" + key + "," + str(data) + "] because the hashtable is full")

    def search(self, key):
        print("Searching for " + key)
        index = self.hash(key)
        for i in list(range(index, len(self.arr))) + list(range(index)):
            if self.arr[i] is None:
                return []
            if self.arr[i][0] == key:
                return self.arr[i]
            print("Search: Collision at index " + str(i))
        return []


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage " + sys.argv[0] + " filename")
        sys.exit(0)

    ht = HashTable(100)
    contents = []
    try:
        contents = [[x[0], x[1]] if len(x) == 2 else [x[0]] for x in [line.split() for line in open(sys.argv[1])]]
    except IOError:
        print("File " + sys.argv[1] + " does not exist")
        sys.exit(0)

    for val in contents:
        if len(val) == 1:
            res = ht.search(val[0])
            if len(res) == 0:
                print("Could not find an entry for key " + val[0])
            else:
                print("Found key " + res[0] + " with val " + str(res[1]))
        else:
            ht.insert(val[0], val[1])
