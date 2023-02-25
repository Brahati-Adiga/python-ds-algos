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
             word = file.readlines()
             index = self.hash_function(word)
             if self.table[index] is None:
                 # print("Entered")
                self.table[index] = Node(word)
                print("Bucket ", index, ":", end="")
                print(word)
             else:
                current = self.table[index]
                while current.next is not None:
                     current = current.next
                current.next = Node(word)
                cur=self.table[index]
                print("Bucket ",index,":",end=" ")
                while cur is not None:
                    print(cur.word,'-->',end=' ')
                    cur=cur.next
                    # print(current.word, "-->", current.next.word)
                    # print('end')
                    print(' ')

table = HashTable()
filename = "tt.txt"
table.read_file(filename)