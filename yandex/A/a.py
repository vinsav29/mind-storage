from collections import Counter

class Stack:
    def __init__(self):
        self.stack = []
        self.labels = {}
        self.length = 0

    def add(self, n, label):
        n = int(n)
        self.stack.append([label, n])
        self.labels[label] = self.labels.get(label, 0) + n
        self.length += n

    def delete(self, n):
        n = int(n)
        i = n
        while self.stack:
            k, v = self.stack[-1]
            if v >= i:
                self.labels[k] -= i
                self.stack[-1][1] -= i
                break
            else:
                k, v = self.stack.pop()
                self.labels[k] -= v
                i -= v
        self.length -= n

    def get(self, label):
        print(self.labels.get(label, 0))


f = open("input.txt")
lines = f.read().splitlines()
f.close()

n = int(lines[0])
s = Stack()
for event in lines[1:]:
    items = event.split()
    cmd = items[0]
    foo = getattr(s, cmd)
    ans = foo(*items[1:])

# def main():
#     n = int(input())
#     stat = defaultdict(int)
#     st = []
#     for q in range(n):
#         s = input()
#         try:
#             cmd, num, name = s.split()
#             stat[name] += int(num)
#             st.append([name, int(num)])
#         except:
#             cmd, ss = s.split()
#             if cmd == "delete":
#                 ss = int(ss)
#                 while st:
#                     if st[-1][1] >= ss:
#                         stat[st[-1][0]] -= ss
#                         st[-1][1] -= ss
#                         break
#                     else:
#                         pp = st.pop()
#                         stat[pp[0]] -= pp[1]
#                         ss -= pp[1]
#             else:
#                 print(stat[ss])
#
# main()