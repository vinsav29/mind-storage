# class TrieNode:
#     def __init__(self):
#         # you can store data at nodes if you wish
#         self.end = False
#         self.children = {}
#
#
# class Trie:
#
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word: str) -> None:
#         node = self.root
#         for w in word:
#             if w not in node.children:
#                 node.children[w] = TrieNode()
#             node = node.children[w]
#         node.end = True
#
#     def search(self, word: str) -> bool:
#         node = self.root
#         for w in word:
#             if w not in node.children:
#                 return False
#             node = node.children[w]
#         return node.end
#
#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for w in prefix:
#             if w not in node.children:
#                 return False
#             node = node.children[w]
#         return True
#
# # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("word")
#
# param_2 = obj.search("word")
# param_3 = obj.search("wor")
#
# param_4 = obj.startsWith("wo")
# print(obj)
