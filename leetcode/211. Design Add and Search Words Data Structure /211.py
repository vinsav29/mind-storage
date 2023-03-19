class Node:
    def __init__(self):
        # you can store data at nodes if you wish
        self.data = None
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
        node.end = True

    def dfs(self, node, word) -> bool:
        if not word:
            # if '.' is the last char, any char in children gives us True answer
            # check current char is end of the word
            return node.end

        for i, w in enumerate(word):
            # current char is "."
            if w == ".":
                for char in node.children:
                    if self.dfs(node.children[char], word[i+1:]):
                        return True
                    else:
                        continue
                else:
                    return False
            # current char is not "."
            if w not in node.children:
                return False

            # go next iteration
            node = node.children[w]

        return node.end

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)
        # node = self.root
        # for i, w in enumerate(word):
        #     if w == ".":
        #         return self.dfs(node, word[i:])
        #     if w not in node.children:
        #         return False
        #     node = node.children[w]
        # return node.end

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
assert not wordDictionary.search("pad") # return False
assert wordDictionary.search("bad") # return True
assert wordDictionary.search(".ad") # return True
assert wordDictionary.search("b..") # return True