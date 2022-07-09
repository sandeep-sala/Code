"""
A prefix tree/Trie has three main operations:
    1. Inserting a word into the tree.
    2. Searching for a node that matches a given string exactly.
    3. Returning a list of all nodes (if any) that begin with a given string prefix.
"""


class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True


    def find(self, word):
        '''
        Returns the TrieNode representing the given word if it exists
        and None otherwise.
        '''
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word

    def __child_words_for(self, node, words):
        '''
        Private helper function. Cycles through all children
        of node recursively, adding them to words if they
        constitute whole words (as opposed to merely prefixes).
        '''
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)


    def starts_with(self, prefix):
        '''
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        '''
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                return list()
            current = current.children[char]

        self.__child_words_for(current, words)
        return words

    def size(self, current = None):
        '''
        Returns the size of this prefix tree, defined
        as the total number of nodes in the tree.
        '''
        # By default, get the size of the whole trie, starting at the root
        if not current:
            current = self.root
        count = 1
        for letter in current.children:
            count += self.size(current.children[letter])
        return count

if __name__ == '__main__':
    trie = PrefixTree()
    trie.insert('apple')
    trie.insert('app')
    trie.insert('aposematic')
    trie.insert('appreciate')
    trie.insert('book')
    trie.insert('bad')
    trie.insert('bear')
    trie.insert('bat')
    print(trie.starts_with('app'))
