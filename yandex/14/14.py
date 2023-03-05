class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, n):
        self.stack.append(n)
        self.length += 1
        return "ok"

    def pop(self):
        if self.length == 0:
            return "error"
        self.length -= 1
        return self.stack.pop(-1)

    def back(self):
        if self.length == 0:
            return "error"
        return self.stack[-1]


# total = int(input())
# seq = list(map(int, input().split()))
with open("input.txt") as f:
    text = f.read()
    total, seq = text.splitlines()
total = int(total)
seq = list(map(int, seq.split()))

s = Stack()
seek = 1
for i in range(total):
    if seq[i] == seek:
        seek += 1
        # try get from stack
        while s.back() == seek:
            s.pop()
            seek += 1
    else:
        s.push(seq[i])

if s.length == 0:
    print("YES")
else:
    print("NO")