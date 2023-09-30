# Construct a Trie from a Collection of Patterns

class TrieNode:
    def __init__(self, id):
        self.children = [None for _ in range(26)]
        self.isEndOfWord = True
        self.id = id


class Trie:
    def __init__(self):
        self.root = TrieNode(0)
        self.number_of_nodes = 0

    def insert(self, word):
        current_node = self.root
        for char in word:
            index = ord(char) - ord('A')
            if not current_node.children[index]:
                self.number_of_nodes = self.number_of_nodes + 1
                current_node.children[index] = TrieNode(self.number_of_nodes)
                print(str(current_node.id), "->", str(current_node.children[index].id), ":", str(char), sep="")
            current_node = current_node.children[index]
        current_node.isEndOfWord = True


trie = Trie()
file = open('rosalind_ba9a.txt', 'r')
lines = file.readlines()

for line in lines:
    trie.insert(line[:-1])
