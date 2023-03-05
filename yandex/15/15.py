class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, toople):
        self.stack.append(toople)
        self.length += 1
        return "ok"

    def pop(self):
        if self.length == 0:
            return "error"
        self.length -= 1
        return self.stack.pop(-1)

    def back(self):
        if self.length == 0:
            return -1, -1
        return self.stack[-1]


with open("input.txt") as f:
    text = f.read()
    total, seq = text.splitlines()
total = int(total)
seq = list(map(int, seq.split()))
s = Stack()
res = ["-1"] * total

s.push((seq[0], 0))
for i in range(1, total):
    while s.back()[0] > seq[i]:
        idx = s.pop()[1]
        res[idx] = str(i)
    s.push((seq[i], i))
print(" ".join(res))

