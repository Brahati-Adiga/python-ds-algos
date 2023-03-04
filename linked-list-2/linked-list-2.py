class Node:
    def __init__(self, word):
        self.word = word
        self.next = None


class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.table = [None] * size

    def hash_function(self, word):
        return sum(ord(literal) for literal in word) % self.size

    def read_file(self, filename):
        with open(filename, 'r+') as file:
            words = file.readlines()
            for word in words:
                index = self.hash_function(word.strip())
                if self.table[index] is None:
                    self.table[index] = Node(word.strip())
                    print("Bucket ", index, ":", end="")
                    print(word.strip())
                else:
                    current = self.table[index]
                    while current.next is not None:
                        current = current.next
                    current.next = Node(word.strip())
                    cur = self.table[index]
                    print("Bucket ", index, ":", end=" ")
                    while cur is not None:
                        print(cur.word, '-->', end=' ')
                        cur = cur.next
                    print(' ')


table = HashTable()
file_name = "tt.txt"
table.read_file(file_name)
