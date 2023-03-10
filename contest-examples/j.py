class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
        self.vocab = set()

    def insert(self, word):
        """Insert a word into the trie"""
        self.vocab.add(word)
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix, first=False):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if len(self.output) > 1:
            return
        if node.is_end:
            self.output.append(prefix if first else prefix + node.char)

        for child in node.children.values():
            self.dfs(child, prefix if first else prefix + node.char)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root
        pref = ""

        # Check if the prefix is in the trie
        for ind, char in enumerate(x):
            if char in node.children:
                if pref and not node.children[char].children and ind + 1 == len(x):
                    break
                node = node.children[char]
                pref += char
            else:
                break
        # Traverse the trie to get all candidates
        self.dfs(node, pref, True)
        if len(self.output) == 1 and self.output[0] == x:
            return (self.vocab - {x}).pop()[::-1]

        if self.output[0] == x:
            return self.output[1][::-1]
        return self.output[0][::-1]


n = int(input())
trie = Trie()
for _ in range(n):
    s = input()
    trie.insert(s[::-1])
q = int(input())
for _ in range(q):
    s = input()[::-1]
    print(trie.query(s))
